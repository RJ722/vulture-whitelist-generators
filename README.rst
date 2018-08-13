vulture-whitelist-generators
============================

.. image:: https://codecov.io/gh/RJ722/vulture-whitelist-generators/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/RJ722/vulture-whitelist-generators


Create whitelists to tackle false positives in Vulture automatically for
frameworks using Python bindings for C and C++ libraries, e.g. PyQt.

Currently, whitelists can only be generated for projects using ``sip`` as the
binding generator, like PyQt. But, we also plan to support ``shiboken`` - the
binding generator for PySide2 projects soon.


Installation
------------

``vulture_whitelist`` is a standard PyPI package and can be installed using
``pip``::

    $ pip3 install vulture_whitelist


From local repository::

    $ git clone https://github.com/RJ722/vulture-whitelist-generators
    $ cd vulture-whitelist-generators
    $ pip3 install .


Usage
-----

To generate a whitelist for ``sip`` projects, ``cd`` into the directory
containing the ``.sip`` files for your project and run::

    $ vulture-whitelist sip --sip /path/to/sip-binary


This will create a ``whitelist.py`` into the current direcotry.

