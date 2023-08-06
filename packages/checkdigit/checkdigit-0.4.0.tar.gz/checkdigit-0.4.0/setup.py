# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['checkdigit']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'checkdigit',
    'version': '0.4.0',
    'description': 'A check digit library for data validation',
    'long_description': ".. image:: https://raw.githubusercontent.com/harens/checkdigit/master/art/logo.png\n   :alt: checkdigit logo\n   :target: https://github.com/harens/checkdigit\n   :align: center\n\n|\n\n.. image:: https://img.shields.io/github/actions/workflow/status/harens/checkdigit/test.yml?logo=github&style=flat-square\n   :alt: GitHub Tests status\n   :target: https://github.com/harens/checkdigit/actions\n\n.. image:: https://img.shields.io/codecov/c/github/harens/checkdigit?logo=codecov&style=flat-square\n   :alt: Codecov\n   :target: https://app.codecov.io/gh/harens/checkdigit\n\n.. image:: https://img.shields.io/pypi/dm/checkdigit?logo=python&logoColor=white&style=flat-square\n   :alt: PyPi - Downloads\n   :target: https://pepy.tech/project/checkdigit\n\n.. image:: https://img.shields.io/codefactor/grade/github/harens/checkdigit?logo=codefactor&style=flat-square\n   :alt: CodeFactor Grade\n   :target: https://www.codefactor.io/repository/github/harens/checkdigit/\n\n=========\n\n.. image:: https://repology.org/badge/vertical-allrepos/python:checkdigit.svg\n   :alt: checkdigit repology\n   :target: https://repology.org/project/python:checkdigit/versions\n   :align: right\n\n**checkdigit** is a pure Python library built for identification numbers.\nYou want to validate a credit card number, or maybe even calculate a missing digit on an ISBN code?\nWe've got you covered 😎.\n\nWant to know more? Check out the `API Reference and documentation <https://checkdigit.readthedocs.io/en/latest/reference.html>`_!\n\nInstallation\n------------\n\n`MacPorts <https://ports.macports.org/port/py-checkdigit/summary>`_ 🍎\n*************************************************************************\n\n.. code-block::\n\n    sudo port install py-checkdigit\n\n`PyPi <https://pypi.org/project/checkdigit/>`_ 🐍\n**************************************************\n\n.. code-block::\n\n    pip install checkdigit\n\n✨ Features\n------------\n\n* 📦 Works out of the box with all `supported Python versions <https://endoflife.date/python>`_ (3.7-3.11).\n* ⌨️ `PEP 561 compatible <https://www.python.org/dev/peps/pep-0561>`_, with built in support for type checking.\n* 🏃 Zero runtime dependencies. What you see is what you get.\n* 🧮 Capable of calculating missing digits or validating a block of data.\n* 📝 Extensive in-code comments and docstrings to explain how it works behind the scenes.\n\n✅ Supported Formats\n---------------------\n\n* `Even/Odd binary parity <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.parity.html#module-checkdigit.parity>`_\n* `CRC <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.crc.html#module-checkdigit.crc>`_\n  (credit to `@sapieninja <https://github.com/sapieninja>`_)\n* `GS1 Standards <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.gs1.html#module-checkdigit.gs1>`_ (credit to `@OtherBarry <https://github.com/OtherBarry>`_)\n    * EAN-8/13\n    * GDTI\n    * GLN\n    * SSCC\n    * UPC-A/E\n    * etc. *(all fixed length numeric GS1 data structures with a check digit)*\n* `ISBN-10/13 <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.isbn.html#module-checkdigit.isbn>`_\n* `Luhn <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.luhn.html#module-checkdigit.luhn>`_\n* `Verhoeff <https://checkdigit.readthedocs.io/en/latest/_autosummary/checkdigit.verhoeff.html#module-checkdigit.verhoeff>`_\n\nFor each of these formats, we provide functions to validate them and calculate missing digits.\n\nDo you have any formats that you'd like to see supported? 🤔 Feel free to raise an issue,\nor even to send a pull request!\n\n🔨 Contributing\n---------------\n\n- Contributing Page: `<https://checkdigit.rtfd.io/en/latest/contributing.html>`_\n- Issue Tracker: `<https://github.com/harens/checkdigit/issues>`_\n- Source Code: `<https://github.com/harens/checkdigit>`_\n\nAny change, big or small, that you think can help improve this project is more than welcome 🎉.\n\nAs well as this, feel free to open an issue with any new suggestions or bug reports. Every contribution is appreciated.\n\nTo find out more, please read our `contributing page <https://checkdigit.readthedocs.io/en/latest/contributing.html>`_. Thank you!\n\n📙 License\n-----------\n\nThis project is licensed under `GPL-3.0-or-later <https://github.com/harens/checkdigit/blob/master/LICENSE>`_.\n",
    'author': 'harens',
    'author_email': 'harensdeveloper@gmail.com',
    'maintainer': 'harens',
    'maintainer_email': 'harensdeveloper@gmail.com',
    'url': 'https://checkdigit.rtfd.io',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
