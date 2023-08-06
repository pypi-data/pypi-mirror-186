=================
Jara core package
=================

    Jara means bear in `Sesotho`_.

.. image:: https://img.shields.io/badge/python-3.11.x-blue.svg
    :alt: Python 3.11.x

.. image:: https://img.shields.io/badge/code_style-flake8-brightgreen.svg
    :alt: Flake8

.. image:: https://img.shields.io/badge/dependency_manager-poetry-blueviolet.svg
    :alt: Poetry

Why?
~~~~
Sometimes I start a new project and I need to implement again same methods and after create tests for each method. This package will provide common methods like ``str_2_bool`` or other methods check ``README.rst`` for all methods available.

How to contribute to the package?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Clone project locally and then:
    * Install all dependencies including the test and the dev oanes: ``poetry install -E test -D``;
    * Do changes in the project;
    * Create unittests (please make sure  you will keep coverage to 100%);
    * Run all sanity commands (pytest, flake8, mypy, bandit);
    * Check if there is any duplicated or dead fixtures by running ``pytest`` with ``--dead-fixtures`` and ``--dup-fixtures``;

Note: Run commands using poetry: ``poetry run <command>``;

What you will find in this package?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Basically will contain utils methods to avoid write them in all projects. Some examples:

* decorator to benchmark methods;
* methods to handle environment variables;
* some utils methods such as: ``snake_2_camel``, ``str_2_bool``.


.. _Sesotho: https://en.wikipedia.org/wiki/Sotho_language
