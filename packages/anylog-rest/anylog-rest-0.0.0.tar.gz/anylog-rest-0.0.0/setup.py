# based on: https://towardsdatascience.com/how-to-upload-your-python-package-to-pypi-de1b363a1b3
from setuptools import setup, find_packages

setup(
    name='anylog-rest',
    version='0.0.0',
    license=None,
    author='AnyLog Co.',
    author_email='info@anylog.co',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='anylog project',
    install_requires=[
        'ast',
        'json',
        'os',
        'requests'
    ],
)
