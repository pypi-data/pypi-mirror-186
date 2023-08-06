# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coinglass_api']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.2,<2.0.0', 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'coinglass-api',
    'version': '0.1.0',
    'description': 'Unofficial Python client for Coinglass API',
    'long_description': '# Coinglass API\n\n## Unofficial Python client for Coinglass API\n\nWrapper around the [Coinglass API](https://coinglass.com/pricing) to fetch data about the crypto markets.\nAll data is output in pandas DataFrames (single or multi index).\n\n**Note**: This is work in progress. The API is not stable yet.\n\n![Example Plot](examples/example_plot.jpg)\n\n## Installation\n\n```bash\npip install coinglass-api\n```\n\n## Usage\n\nCurrently only supports the `indicator` API endpoint.\n\n```python\nfrom coinglass_api import CoinglassAPI\n\ncg = CoinglassAPI(api_key="abcd1234")\n\n# Get average funding for Bitcoin\nfr_avg = cg.average_funding(symbol="BTC", interval="h4")\n\n# Get aggregated OI OHLC data for Bitcoin\noi_agg = cg.open_interest_aggregated_ohlc(symbol="BTC", interval="h4")\n\n# Get liquidation data for Bitcoin\nliq = cg.liquidation_symbol(symbol="BTC", interval="h4")\n\n# Get long/short ratio data for Bitcoin\nlsr = cg.long_short_symbol(symbol="BTC", interval="h4")\n```\n\n\n## Disclaimer\n\nThis project is for educational purposes only. You should not construe any such information or other material as legal,\ntax, investment, financial, or other advice. Nothing contained here constitutes a solicitation, recommendation,\nendorsement, or offer by me or any third party service provider to buy or sell any securities or other financial\ninstruments in this or in any other jurisdiction in which such solicitation or offer would be unlawful under the\nsecurities laws of such jurisdiction.\n\nUnder no circumstances will I be held responsible or liable in any way for any claims, damages, losses, expenses, costs,\nor liabilities whatsoever, including, without limitation, any direct or indirect damages for loss of profits.',
    'author': 'dineshpinto',
    'author_email': 'dkpinto95@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dineshpinto/coinglass-api',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
