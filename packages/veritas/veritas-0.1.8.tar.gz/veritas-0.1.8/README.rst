veritas
=======

Veritas is a Python library implementing a throwaway variable that attempts to return true no matter how it is called upon.

It is intended for writing tests where you must provide some variables to an interface but your particular test will never read what happens to them. Veritas attempts to make sure that whatever the side effects on these variables it will not derail program execution. It implements comparable, numeric, callable, container, iterator, binary, in-place, unary, context manager, and async interfaces.


:Code:          https://github.com/lonnen/veritas/
:Issues:        https://github.com/lonnen/veritas/issues
:License:       BSD 3-clause; See LICENSE

Install
=======

From PyPI
---------

Run::

    $ pip install veritas

For hacking
-----------

Run::

    $ git clone https://github.com/lonnen/veritas
    # Create and activate virtualenvironment, left to the reader as an excercise
    $ pip install -r requirements-dev.txt


Usage
=====

see tests for example usage
