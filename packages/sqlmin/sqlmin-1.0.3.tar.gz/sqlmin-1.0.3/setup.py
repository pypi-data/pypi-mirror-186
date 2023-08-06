from setuptools import setup


setup(
    name='sqlmin',
    version='1.0.3',
    description='SQL Minifier',
    long_description="SQL Minifier",
    author='Enrique Rodriguez',
    author_email='rodriguez.enrique.pr@gmail.com',
    url='https://github.com/enrique-rodriguez/sqlmin',
    keywords = ['sql minifier', 'minify sql', 'sqlmin', 'minsql'],
    entry_points={
        'console_scripts': [
            'sqlmin = sqlmin:main',
        ]
    }
)