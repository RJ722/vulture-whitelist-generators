vulture-whitelist-generators
============================

Create whitelists to tackle false positives in Vulture automatically for
frameworks using Python bindings for C and C++ libraries, for eg. PyQt.

Currently, a whitelist can only be generated for projects using ``sip``,
which is particularly useful for ``PyQt`` projects, but we plan to support
``shiboken`` for ``PySide2`` projects soon.


Installation
------------

vulture-whitelist is a standard package and can be installed using ``pip``:

::

    $ pip install vulture-whitelist

From local repository:

::

    $ git clone https://github.com/RJ722/vulture-whitelist-generators
    $ cd vulture-whitelist-generators
    $ pip install .


Usage
-----

Generate a whitelist for ``sip`` projects:

::

    $ vulture-whitelist sip /path/to/input-sip-files --sip /path/to/sip-binary
