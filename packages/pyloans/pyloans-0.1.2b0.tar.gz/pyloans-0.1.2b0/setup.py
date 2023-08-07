# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pyloans']

package_data = \
{'': ['*']}

install_requires = \
['numpy-financial>=1.0.0,<2.0.0', 'pandas>=1.5.2,<2.0.0']

setup_kwargs = {
    'name': 'pyloans',
    'version': '0.1.2b0',
    'description': 'A package to generate, analyze and work with simple installment loans.',
    'long_description': "![tests](https://github.com/sandeepkavadi/pyloans/actions/workflows/test.yml/badge.svg)\n![docs build](https://github.com/sandeepkavadi/pyloans/actions/workflows/docs.yml/badge.svg)\n\n# `pyloans`: A simulator for installment based financial obligations\n\n## Introduction\n\n`pyloans` is a python based package to simplify, analyze and work with\ninstallment based loan obligations. The installments are generally a fixed\namount that the borrower pays to the lender at equally spaced intervals\nover the life of the loan.\n\nThe pyloans package is written with both the borrowers (end-consumer) and\nlenders (financial institutions) in mind.\n\nFrom a borrower's perspective the package offers the following functionality:\n1. Original schedule of Cashflows\n2. Modified schedule of Cashflows, in case of additional payments or full\n   pre-payment\n3. Updated date of maturity based on additional payments made\n4. Annual Percentage Rate (APR)\n\n[comment]: <> (5. Compare offers and consolidate multiple financial\n   obligations)\n\nFrom a lenders perspective the package offers the following functionality:\n1. Weighted average life of a loan (WAL)\n\n[comment]: <> (2. Consolidate multiple loan objects into a portfolio)\n[comment]: <> (3. Simulate various loan structure to quantify impact to\nlender's profitability)\n[comment]: <> (4. Simulate an unsecured lending portfolio by creating multiple\n   instances of loan objects with random initial parameters based on\n   historical distributions for each parameter.)\n[comment]: <> (5. Systematic way to understand portfolio profitability based on\n   historical distributions of prepayments, charge-offs and loan structures.)\n\nPlease see [Quickstart guide](https://sandeepkavadi.github.io/pyloans/quickstart/) for basic functionality of the\npackage.\n",
    'author': 'Sandeep',
    'author_email': 'sandeep.kavadi.uc@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
