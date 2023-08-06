# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xjet']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.1']

setup_kwargs = {
    'name': 'xjet',
    'version': '0.1.0',
    'description': 'Python SDK for t.me/xJetSwapBot',
    'long_description': '# pyxJetAPI\n\n## Authors\n- [@xJetLabs](https://github.com/xJetLabs) (forked from)\n- [@nik-1x](https://www.github.com/nik-1x)\n \n## Usage/Examples  \n```python\napi = pyxJet(\n    api_key="API_KEY",\n    private_key="PRIVATE_KEY", \n    mainnet=xJetNet.TESTNET # or xJetNet.MAINNET\n)\n```\n\n```python\n# Account methods\nawait api.me() # get API Application information.\nawait api.balance() # get balance\nawait api.submit_deposit() # check for deposit\nawait api.withdraw(ton_address, currency, amount) # check for deposit\n```\n\n```python\n# Cheques methods\nawait api.cheque_create(currency, amount, expires, description, activates_count, groups_id, personal_id, password) # create cheque\nawait api.cheque_status(cheque_id) # get cheque status\nawait api.cheque_list() # get cheques on account\nawait api.cheque_cancel(cheque_id) # delete cheque\n```\n\n```python\n# Invoice methods\nawait api.invoice_create(currency, amount, description, max_payments) # create invoice\nawait api.invoice_status(invoice_status) # get invoice status\nawait api.invoice_list() # get invoices on account\n```\n\n## License\n[GNUv3](https://github.com/nik-1x/pyxJetAPI/blob/main/LICENSE)  \n',
    'author': 'delpydoc',
    'author_email': 'delpydoc@proton.me',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/xJetLabs/python-sdk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
