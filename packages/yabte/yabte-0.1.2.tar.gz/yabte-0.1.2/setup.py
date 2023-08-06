# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yabte']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.2,<2.0.0']

setup_kwargs = {
    'name': 'yabte',
    'version': '0.1.2',
    'description': 'Yet another backtesting engine',
    'long_description': '# yabte - Yet Another BackTesting Engine\n\nPython module for backtesting trading strategies.\n\nSupport event driven backtesting, ie `on_open`, `on_close`, etc. Also supports multiple assets.\n\nVery basic statistics like book cash, mtm and total value. Currently, everything else needs to be deferred to a 3rd party module like `empyrical`.\n\nThere are some basic tests but use at your own peril. It\'s not production level code.\n\n## Core dependencies\n\nThe core module uses pandas.\n\n## Installation\n\n```bash\npip install yatbe\n```\n\n## Usage\n\nBelow is an example usage (the performance of the example strategy won\'t be good).\n\n```python\nfrom pathlib import Path\nimport pandas as pd\n\nimport yabte\nfrom yabte import Strategy, StrategyRunner, Order\nfrom yabte.utils import crossover\n\ndata_dir = Path(yabte.__file__).parents[1] / "tests/data"\n\n\nclass SmokeStrat1(Strategy):\n    def init(self):\n        # enhance data with simple moving averages\n        csma10 = (\n            self.data.loc[:, (slice(None), "Close")]\n            .rolling(10)\n            .mean()\n            .rename({"Close": "CloseSMA10"}, axis=1, level=1)\n        )\n        csma20 = (\n            self.data.loc[:, (slice(None), "Close")]\n            .rolling(20)\n            .mean()\n            .rename({"Close": "CloseSMA20"}, axis=1, level=1)\n        )\n        self.data = pd.concat([self.data, csma10, csma20], axis=1).sort_index(axis=1)\n\n    def on_close(self):\n        # create some orders\n        data_2d = self.data.iloc[-2:]\n        for sym in ["GOOG", "MSFT"]:\n            data = data_2d[sym].loc[:, ("CloseSMA10", "CloseSMA20")].dropna()\n            if len(data) == 2:\n                if crossover(data.CloseSMA10, data.CloseSMA20):\n                    self.orders.append(Order(asset_name=sym, size=100))\n                elif crossover(data.CloseSMA20, data.CloseSMA10):\n                    self.orders.append(Order(asset_name=sym, size=-100))\n\n\n# load some data\nasset_meta = {"GOOG": {"denom": "USD"}, "MSFT": {"denom": "USD"}}\n\ndf_goog = pd.read_csv(data_dir / "GOOG.csv", index_col=0, parse_dates=[0])\ndf_goog.columns = pd.MultiIndex.from_tuples([("GOOG", f) for f in df_goog.columns])\n\ndf_msft = pd.read_csv(data_dir / "MSFT.csv", index_col=0, parse_dates=[0])\ndf_msft.columns = pd.MultiIndex.from_tuples([("MSFT", f) for f in df_msft.columns])\n\n# run our strategy\nsr = StrategyRunner(\n    data=pd.concat([df_goog, df_msft], axis=1),\n    asset_meta=asset_meta,\n    strats=[SmokeStrat1],\n)\nsr.run()\n\n# see the trades or book history\nth = sr.trade_history\nbch = sr.book_history.loc[:, (slice(None), "cash")]\n```',
    'author': 'Blair Azzopardi',
    'author_email': 'blairuk@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bsdz/yabte',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
