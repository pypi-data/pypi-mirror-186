from setuptools import setup, find_packages


setup(
    name="airflow-sendgrid-provider-j2",
    version="0.0.3",
    url='https://gitlab.netprotect.com/hercules/airflow-sendgrid-provider',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'apache-airflow',
        'sendgrid',
    ],
)
