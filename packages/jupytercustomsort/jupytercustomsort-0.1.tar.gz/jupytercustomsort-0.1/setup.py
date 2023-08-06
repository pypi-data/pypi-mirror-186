#!/usr/bin/env python

from distutils.core import setup

setup(
    name='jupytercustomsort',
    version='0.1',
    description='Custom sort order for Jupyter file list',
    long_description='This package provides both a server extension and a notebook extension to provide a custom sort order for Jupyter file lists.  When both are enabled, a `.custom_order` JSON file can be placed in any directory to determine the sort order.',
    author='Robert Schroll',
    author_email='rschroll@gmail.com',
    url='https://github.com/dataincubator/jupytercustomsort',
    packages=['jupytercustomsort'],
    package_data={'jupytercustomsort': ['nbext/*']},
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        'Framework :: Jupyter',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'
    ]
)
