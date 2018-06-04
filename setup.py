#! /usr/bin/env python

import setuptools

from generators.main import __version__


setuptools.setup(
    name='vulture-whitelist',
    version=__version__,
    description=(
        'Create whitelists to tackle false positives in Vulture automatically'
        ' for frameworks using Python bindings for C and C++ libraries.'),
    long_description='\n\n'.join(
        [open('README.rst').read(), open('NEWS.rst').read()]),
    keywords='dead-code-removal',
    author='Rahul Jha',
    author_email='rahul722j@gmail.com',
    url='https://github.com/RJ722/vulture-whitelist-generators',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Quality Assurance'
    ],
    entry_points={
        'console_scripts': ['vulture-whitelist = generators.main:main'],
    },
)
