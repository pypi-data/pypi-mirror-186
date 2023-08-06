# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains the dartdomain Sphinx extension.

This extension provides a Dart domain for sphinx

'''

requires = ['Sphinx>=1.0']

setup(
    name='sphinxcontrib-dartdomain',
    version='0.1.0',
    url='http://github.com/danhunsaker/sphinxcontrib-dartdomain',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-dartdomain',
    license='BSD',
    author='Hennik Hunsaker',
    author_email='hennik@insidiouslogic.systems',
    description='Sphinx "dartdomain" extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
