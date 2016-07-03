# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

name = 'ntv.api'
description = (
    'N television program API'
)
version = '0.1.0'


setup(
    name=name,
    version=version,
    description=description,
    author='Marek Wywiał',
    author_email='onjinx@gmail.com',
    packages=find_packages(),
    namespace_packages=name.split('.')[:-1],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'morepath',
        'ntv>=0.4.4',
        'parsedatetime',
        'werkzeug',
    ],
    extras_require=dict(
        test=[
            'pytest',
            'pytest-cov',
            'webtest',
        ],
    ),
    entry_points=dict(
        console_scripts=[
            'ntv-ctl = ntv.api.__main__:run',
        ],
    ),
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ]
)
