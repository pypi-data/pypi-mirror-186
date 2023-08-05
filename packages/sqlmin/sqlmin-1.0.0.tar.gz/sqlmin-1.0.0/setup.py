from setuptools import setup


setup(
    name='sqlmin',
    version='1.0.0',
    description='SQL Minifier',
    long_description="SQL Minifier",
    author='Enrique Rodriguez',
    author_email='rodriguez.enrique.pr@gmail.com',
    entry_points={
        'console_scripts': [
            'sqlmin = sqlmin:main',
        ]
    }
)