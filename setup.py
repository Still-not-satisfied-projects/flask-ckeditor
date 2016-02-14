#!/usr/bin/env python
# encoding: utf-8

"""
Flask-CkEditor
-------------

flask后台快速集成ckeditor编辑器
"""

from setuptools import setup


setup(
    name='flaskckeditor',
    version='1.5',
    url='https://github.com/neo1218/flask-ckeditor',
    license='MIT',
    author='neo1218',
    author_email='neo1218@yeah.net',
    description='flask后台快速集成ckeditor编辑器',
    long_description=__doc__,
    py_modules=['flaskckeditor'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    # packages=['flask_sqlite3'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'flask-wtf'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

