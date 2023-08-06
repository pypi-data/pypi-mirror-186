# Airflow SendGrid Provider

This is a modified version of https://github.com/apache/airflow/tree/master/airflow/providers/sendgrid

## Changelog:
* added dynamic templates support
* changed errors messages

## Usage
If `template_id` and `template_substitution` parameters is passed, 
the `html_content` and `subject` parameters will be ignored

## Example

    send_email(
            from_email='hello@example.com',
            from_name='Hello',
            subject=null,
            to='world@example.com'',
            html_content=null,
            template_id='00000000-0000-0000-0000-000000000000',
            template_substitution={
                ':number': '1337'
            }
        )