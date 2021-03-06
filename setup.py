#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
    'Cython',
    'numpy',
    'postal==1.0',
    'scikit_learn==0.19',
    'pyfasttext'

]

setup_requirements = [
    # TODO(rdoume): put setup requirements (distutils extensions, etc.) here
'bumpversion==0.5',
'wheel==0.29',
'watchdog==0.8',
'flake8==2.6',
'Cython',
'tox==2.3',
'coverage==4.1',
'Sphinx==1.4'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='addr_detector',
    version='0.1.0',
    description="Python address detector ",
    long_description=readme + '\n\n' + history,
    author="Qwant",
    author_email='robin@qwantresearch.com',
    url='https://github.com/rdoume/addr_detector',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['*.ftz']},
    data_files=[('model', ['addr_detector/model/ft_ad.ftz'])],
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='addr_detector',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',

    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
