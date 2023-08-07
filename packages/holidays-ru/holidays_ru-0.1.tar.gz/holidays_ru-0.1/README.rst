===============
python-holidays
===============

A fast, efficient Python library for Russia country, province and state
specific sets of holidays on the fly.
It aims to make determining whether a specific date is a holiday as fast and
flexible as possible.

:Package:
    .. image:: https://img.shields.io/pypi/pyversions/holidays-ru.svg?logo=python&label=Python&logoColor=gold
        :target: https://pypi.python.org/pypi/holidays-ru
        :alt: Python supported versions

    .. image:: http://img.shields.io/pypi/v/holidays-ru.svg?logo=pypi&label=PyPI&logoColor=gold
        :target: https://pypi.python.org/pypi/holidays-ru
        :alt: PyPI version

    .. image:: https://img.shields.io/pypi/dm/holidays-ru.svg?color=blue&label=Downloads&logo=pypi&logoColor=gold
        :target: https://pypi.python.org/pypi/holidays-ru
        :alt: Downloads

:CD/CI:
    .. image:: https://github.com/xvlady/python-holidays-ru/actions/workflows/python-package.yml/badge.svg
        :target: https://github.com/xvlady/python-holidays-ru/actions/workflows/python-package.yml

    .. image:: https://coveralls.io/repos/github/xvlady/python-holidays-ru/badge.svg?branch=main
        :target: https://coveralls.io/github/xvlady/python-holidays-ru?branch=main

:Meta:
    .. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :alt: Code style

    .. image:: http://img.shields.io/pypi/l/holidays.svg
        :target: LICENSE
        :alt: License

Install
-------

The latest stable version can always be installed or updated via pip:

.. code-block:: bash

    $ pip install --upgrade holidays-ru


Documentation
-------------

View Quick Start. You can use original library from other country and other functional https://python-holidays.readthedocs.io/


Quick Start
-----------

.. code-block:: python

    from datetime import date
    from holidays_ru import check_holidays, is_holidays

    check_holiday(date(2023, 1, 1))  # True
    check_holiday(date(2023, 1, 12)) # False
    check_holiday(date(2022, 12, 31)) # True
    check_holiday(date(2022, 12, 31), with_weekends=False) # False, it's Sunday
    is_holiday(date(2023, 1, 1))     # "New Year's Day"
    is_holiday(date(2023, 1, 12))    # ""
    is_holiday(date(2023, 1, 15))    # "Weekend"
    is_holiday(date(2023, 1, 15))    # "Moved weekend"
    is_holiday(date(2023, 1, 12))    # "", it's work Sunday


Contributions
-------------

.. _Issues: https://github.com/xvlady5/python-holidays-ru/issues
.. _pull requests: https://github.com/xvlady5/python-holidays-ru/pulls
.. _here: CONTRIBUTING.rst

Issues_ and `pull requests`_ are always welcome.  Please see
`here`_ for more information.

License
-------

.. __: LICENSE

Code and documentation are available according to the MIT License
(see LICENSE__).
