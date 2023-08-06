# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['lisatools']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.11.1,<5.0.0',
 'cachetools>=5.2.1,<6.0.0',
 'requests>=2.28.1,<3.0.0']

setup_kwargs = {
    'name': 'lisatools',
    'version': '0.5.0',
    'description': 'Tools for monitoring my Lifetime ISA portfolio.',
    'long_description': '# lisatools\n\nTools for monitoring my Lifetime ISA portfolio.\n\n## Installation\n\n```bash\n$ pip install lisatools\n```\n\n## Usage\n\n`lisatools` provides classes and functions that help me manage my Lifetime ISA\nfund portfolio. For example, I can calculate the trades required to obtain\nmy target portfolio as in the following snippet:\n\n```python\nimport lisatools\nimport datetime\n\nftse_global = lisatools.Fund(\n    "FTSE Global All Cap Index Fund",\n    172.14,\n    isin="GB00BD3RZ582",\n    date=datetime.date(2022, 11, 21)\n)\ngilts = lisatools.Fund(\n    "U.K. Gilt UCITS ETF (VGOV)",\n    18.58,\n    isin="IE00B42WWV65",\n    date=datetime.date(2022, 11, 21)\n)\nholding1 = lisatools.Holding(ftse_global, 1.0, 0.6)\nholding2 = lisatools.Holding(gilts, 5.0, 0.4)\npf = lisatools.Portfolio([holding1, holding2])\n\nbuy, sell = pf.trade_to_target()\nprint("Buy:\\n=====", buy, "\\nSell:\\n=====", sell, sep = "\\n")\n```\n\n[A more elaborate example](/docs/example.ipynb) is provided in the /docs/ folder.\n\n## License\n\n`lisatools` was created by Istvan Kleijn. It is licensed under the terms of the MIT license.\n\n## Credits\n\n`lisatools` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).\n',
    'author': 'Istvan Kleijn',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
