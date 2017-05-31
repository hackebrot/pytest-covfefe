==============
pytest-covfefe
==============

I have the best code! Everyone says so. #covfefe

----

This `pytest`_ plugin was generated with `Cookiecutter`_ along with
`@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.

⚠️ pytest-covfefe was created as a reaction to an internet thing ⚠️

It's a terrible idea and you shouldn't use it. If you're wondering why I
created it...well because generating a pytest-plugin with
`cookiecutter-pytest-plugin`_ takes only a few seconds and I felt like writing
a stupid plugin. That's it. 😉


Features
--------

* Plugin cannot be disabled 👐 (It doesn't care what you think)
* Tests always pass 💩 (Yes, really! Also for failures and errors)
* The concept of global warming is made up 🌦 (#covfefe)


Requirements
------------

* Python 3.6


Installation
------------

You can install "pytest-covfefe" via `pip`_ from GitHub::

    $ pip install git+https://github.com/hackebrot/pytest-covfefe


Usage
-----

Run your tests with `pytest`_::

    $ pytest

This plugin also supports *verbose* mode::

    $ pytest -v


Example
-------

.. code-block::

    $ pytest -v
    ============================== test session starts ==============================
    plugins: covfefe-0.1.0
    collected 5 items

    foobar/test_foobar_02.py::test_sth 🙌  AKTBYLOMRQ 💩  🌎  🌤
    foobar/test_foobar_03.py::test_sth 🙌  COVFEFE 💩  🌏  🌩
    hello/world/test_world_01.py::test_sth 👋  COVFEFE 💩  🌍  🌩
    hello/world/test_world_02.py::test_sth 👋  WIVLCKFNMQ 💩  🌍  🌤
    hello/world/test_world_03.py::test_sth 👋  PGXPIUSJ 💩  🌍  🌤

    =========================== 5 passed in 0.31 seconds ============================

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-covfefe" is free and
open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/hackebrot/pytest-covfefe/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`pip`: https://pypi.python.org/pypi/pip/
