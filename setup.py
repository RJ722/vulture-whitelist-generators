#! /usr/bin/env python

import codecs
import os
import re
import setuptools


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setuptools.setup(
    name='vulture_whitelist',
    version=find_version("vulture_whitelist", "main.py"),
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
        'Development Status :: 3 - Alpha',
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
    install_requires=['lxml'],
    tests_require=['pytest', 'pytest-cov', 'vulture'],
    entry_points={
        'console_scripts': ['vulture-whitelist = vulture_whitelist.main:main']
    },
    packages=['vulture_whitelist'],
)
