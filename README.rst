========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |github-actions|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/beonetapi/badge/?style=flat
    :target: https://beonetapi.readthedocs.io/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/tanumkroken/beonetapi/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/tanumkroken/beonetapi/actions

.. |codecov| image:: https://codecov.io/gh/tanumkroken/beonetapi/branch/main/graphs/badge.svg?branch=main
    :alt: Coverage Status
    :target: https://codecov.io/github/tanumkroken/beonetapi

.. |version| image:: https://img.shields.io/pypi/v/beonetapi.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/beonetapi

.. |wheel| image:: https://img.shields.io/pypi/wheel/beonetapi.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/beonetapi

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/beonetapi.svg
    :alt: Supported versions
    :target: https://pypi.org/project/beonetapi

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/beonetapi.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/beonetapi

.. |commits-since| image:: https://img.shields.io/github/commits-since/tanumkroken/beonetapi/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/tanumkroken/beonetapi/compare/v0.0.0...main



.. end-badges

Bang Olufsen beo-net-remote api

* Free software: MIT license

Installation
============

::

    pip install beonetapi

You can also install the in-development version with::

    pip install https://github.com/tanumkroken/beonetapi/archive/main.zip


Documentation
=============


https://beonetapi.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
