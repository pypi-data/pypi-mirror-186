============
Contributing
============

.. _prs: https://github.com/xvlady5/python-holidays-ru/pulls
.. |contributors| image:: https://img.shields.io/github/contributors/xvlady5/python-holidays-ru
    :target: https://www.github.com/dr-prodigy/python-holidays
    :alt: contributors

|contributors|


Basics
------

Contributed PRs_ are required to include valid test coverage **(95% minimum,
100% whenever possible)** in order to be merged.

Thanks a lot for your support.


Running tests
-------------

First step is installing all the required dependencies with:

.. code-block:: bash

    $ pip install -r requirements_dev.txt

The project provides automated tests and coverage checks with tox; just run:

.. code-block:: bash

    $ tox

Alternatively, you can run pytest to run tests and coverage:

.. code-block:: bash

    $ python -m pytest .
    # if you want to retrieve uncovered lines too:
    $ python -m pytest --cov-report term-missing .

In addition to pytest, you need to ensure that all staged files are up to
standard.

.. _pre-commit: https://github.com/xvlady5/python-holidays-ru/issues

Install `pre-commit`_ and its git hook script so that the quality assurance
tests will run on all staged files before they are committed:

.. code-block:: bash

    $ pip install pre-commit
    $ pre-commit install

To manually run the quality assurance tests on all tracked files:

.. code-block:: bash

    $ pre-commit run -a
