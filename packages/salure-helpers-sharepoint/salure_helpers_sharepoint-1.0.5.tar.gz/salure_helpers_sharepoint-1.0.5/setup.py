from setuptools import setup


setup(
    name='salure_helpers_sharepoint',
    version='1.0.5',
    description='Sharepoint wrapper from Salure',
    long_description='Sharepoint wrapper from Salure',
    author='D&A Salure',
    author_email='support@salureconnnect.com',
    packages=["salure_helpers.sharepoint"],
    license='Salure License',
    install_requires=[
        'salure-helpers-salureconnect>=1',
        'requests>=2,<=3'
    ],
    zip_safe=False,
)