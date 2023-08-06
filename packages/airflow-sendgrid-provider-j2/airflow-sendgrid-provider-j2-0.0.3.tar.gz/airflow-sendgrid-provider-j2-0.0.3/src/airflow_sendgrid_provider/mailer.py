#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""Airflow module for email backend using sendgrid"""

import base64
import logging
import mimetypes
import os
import warnings
from typing import Dict, Iterable, Optional, Union
from urllib.error import HTTPError

import sendgrid
from sendgrid.helpers.mail import (
    Attachment,
    Category,
    Content,
    CustomArg,
    Email,
    Mail,
    MailSettings,
    Personalization,
    SandBoxMode,
)

from airflow.exceptions import AirflowException
from airflow.hooks.base import BaseHook
from airflow.utils.email import get_email_address_list

log = logging.getLogger(__name__)

AddressesType = Union[str, Iterable[str]]


def send_email(  # pylint: disable=too-many-locals
    to: AddressesType,
    subject: str = None,
    html_content: str = None,
    template_id: str = None,
    template_substitution: dict = {},
    files: Optional[AddressesType] = None,
    cc: Optional[AddressesType] = None,
    bcc: Optional[AddressesType] = None,
    sandbox_mode: bool = False,
    conn_id: str = "sendgrid_default",
    **kwargs,
) -> None:
    """
    Send an email with html content using `Sendgrid <https://sendgrid.com/>`__.

    .. note::
        For more information, see :ref:`email-configuration-sendgrid`
    """
    # Check if required parameters are missed
    error_message = None
    if not subject and not template_id:
        error_message = 'Parameter subject is missed'
    if not html_content and not template_id:
        error_message = 'Parameter html_content is missed'
    if not template_substitution and template_id:
        error_message = 'Parameter template_substitution is missed'
    if error_message:
        log.error('Error: %s', error_message)
        raise AirflowException(error_message)

    if files is None:
        files = []

    mail = Mail()
    from_email = kwargs.get('from_email') or os.environ.get('SENDGRID_MAIL_FROM')
    from_name = kwargs.get('from_name') or os.environ.get('SENDGRID_MAIL_SENDER')
    mail.from_email = Email(from_email, from_name)
    mail.subject = subject
    mail.mail_settings = MailSettings()

    if sandbox_mode:
        mail.mail_settings.sandbox_mode = SandBoxMode(enable=True)

    # Add the recipient list of to emails.
    personalization = Personalization()
    to = get_email_address_list(to)
    for to_address in to:
        personalization.add_to(Email(to_address))
    if cc:
        cc = get_email_address_list(cc)
        for cc_address in cc:
            personalization.add_cc(Email(cc_address))
    if bcc:
        bcc = get_email_address_list(bcc)
        for bcc_address in bcc:
            personalization.add_bcc(Email(bcc_address))

    if template_substitution:
        personalization.add_substitution(template_substitution)

    # Add custom_args to personalization if present
    pers_custom_args = kwargs.get('personalization_custom_args')
    if isinstance(pers_custom_args, dict):
        for key in pers_custom_args.keys():
            personalization.add_custom_arg(CustomArg(key, pers_custom_args[key]))

    mail.add_personalization(personalization)

    if template_id:
        mail.template_id = template_id
    if not template_id:
        mail.add_content(Content('text/html', html_content))

    categories = kwargs.get('categories', [])
    for cat in categories:
        mail.add_category(Category(cat))

    # Add email attachment.
    for fname in files:
        basename = os.path.basename(fname)

        with open(fname, "rb") as file:
            content = base64.b64encode(file.read()).decode('utf-8')

        attachment = Attachment(
            file_content=content,
            file_type=mimetypes.guess_type(basename)[0],
            file_name=basename,
            disposition="attachment",
            content_id=f"<{basename}>",
        )

        mail.add_attachment(attachment)
    _post_sendgrid_mail(mail.get(), conn_id)


def _post_sendgrid_mail(mail_data: Dict, conn_id: str = "sendgrid_default") -> None:
    api_key = None
    try:
        conn = BaseHook.get_connection(conn_id)
        api_key = conn.password
    except AirflowException:
        pass
    if api_key is None:
        warnings.warn(
            "Fetching Sendgrid credentials from environment variables will be deprecated in a future "
            "release. Please set credentials using a connection instead.",
            PendingDeprecationWarning,
            stacklevel=2,
        )
        api_key = os.environ.get('SENDGRID_API_KEY')
    sendgrid_client = sendgrid.SendGridAPIClient(api_key=api_key)
    try:
        response = sendgrid_client.client.mail.send.post(request_body=mail_data)
    except HTTPError as e:
        message = f"Failed to send email. With HTTPError: {e}"
        log.info(message)
        raise e
    except Exception as e:
        bare_message = f"Failed to send email. With: {e}"
        log.info(bare_message)
        raise ValueError(bare_message) from e
    # 2xx status code.

    email_info = ''
    if 'template_id' in mail_data:
        email_info = 'Template ID: {0}; '.format(mail_data['template_id'])
    elif 'subject' in mail_data:
        email_info = 'Subject: {0}; '.format(mail_data['subject'])

    if 200 <= response.status_code < 300:
        log.info(
            'Email is successfully sent. %sPersonalizations: %s',
            email_info,
            mail_data['personalizations'],
        )
    else:
        log.error(
            'Failed to send out email. %sStatus code: %s',
            email_info,
            response.status_code,
        )