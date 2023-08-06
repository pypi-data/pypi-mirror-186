# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cipher',
 'cipher.factories',
 'cipher.models',
 'cipher.plotters',
 'cipher.proxies',
 'cipher.services',
 'cipher.sources',
 'cipher.use_cases',
 'cipher.utils',
 'cipher.values']

package_data = \
{'': ['*'], 'cipher': ['templates/*', 'templates/strategies/*']}

install_requires = \
['dependency-injector>=4.41.0,<5.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'mplfinance>=0.12.9b7,<0.13.0',
 'pandas-ta>=0.3.14b0,<0.4.0',
 'pydantic[dotenv]>=1.10.4,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'tabulate>=0.9.0,<0.10.0',
 'typer>=0.7.0,<0.8.0',
 'ujson>=5.6.0,<6.0.0']

extras_require = \
{'finplot': ['finplot>=1.9.0,<2.0.0'],
 'jupyter': ['jupyterlab>=3.5.2,<4.0.0'],
 'yfinance': ['yfinance>=0.2.3,<0.3.0']}

entry_points = \
{'console_scripts': ['cipher = cipher.cli:app']}

setup_kwargs = {
    'name': 'cipher-bt',
    'version': '0.1.4',
    'description': 'Cipher, a backtesting framework.',
    'long_description': '# Cipher - trading strategy backtesting framework\n\n![Tests](https://github.com/nanvel/cipher-bt/actions/workflows/tests.yaml/badge.svg)\n\n- [Usage](#usage)  \n- [Development](#development)\n- [Disclaimer](#disclaimer)\n\nDocumentation: https://cipher.nanvel.com\n\nFeatures:\n\n- well-structured, simple to use, extensible\n- multiple trading sessions at the same time\n- complex exit strategies can be implemented (trailing take profit, etc.)\n- multiple data sources support (multiple exchanges, symbols, timeframes, etc.)\n- signal generation and signal handlers are splitted\n- simple to run, just `python my_strategy.py`\n- works in [Google Colab](https://colab.research.google.com/)\n- [finplot](https://github.com/highfestiva/finplot) and [mplfinance](https://github.com/matplotlib/mplfinance) plotters\n- TA: [pandas-ta](https://github.com/twopirllc/pandas-ta) is included, you can still use your libraries of choice\n\n## Usage\n\nInitialize a new strategies folder and create a strategy:\n```shell\npip install cipher-bt\nmkdir my_strategies\ncd my_strategies\n\ncipher init\ncipher new my_strategy\npython my_strategy.py\n```\n\nEMA crossover strategy example:\n```python\nimport numpy as np\n\nfrom cipher import Cipher, Session, Strategy\n\n\nclass EmaCrossoverStrategy(Strategy):\n    def __init__(self, fast_ema_length=9, slow_ema_length=21, trend_ema_length=200):\n        self.fast_ema_length = fast_ema_length\n        self.slow_ema_length = slow_ema_length\n        self.trend_ema_length = trend_ema_length\n\n    def compose(self):\n        df = self.datas.df\n        df["fast_ema"] = df.ta.ema(length=self.fast_ema_length)\n        df["slow_ema"] = df.ta.ema(length=self.slow_ema_length)\n        df["trend_ema"] = df.ta.ema(length=self.trend_ema_length)\n\n        df["difference"] = df["fast_ema"] - df["slow_ema"]\n\n        # this column is required, it triggers on_entry, has to be bool\n        df["entry"] = np.sign(df["difference"].shift(1)) != np.sign(df["difference"])\n\n        df["max_6"] = df["high"].rolling(window=6).max()\n        df["min_6"] = df["low"].rolling(window=6).min()\n\n        return df[df["trend_ema"].notnull()]\n\n    def on_entry(self, row: dict, session: Session):\n        if row["difference"] > 0 and row["close"] > row["trend_ema"]:\n            # start a new long session\n            session.position += "0.01"\n            session.stop_loss = row["min_6"]\n            session.take_profit = row["close"] + 1.5 * (row["close"] - row["min_6"])\n\n        elif row["difference"] < 0 and row["close"] < row["trend_ema"]:\n            # start a new short session\n            session.position -= "0.01"\n            session.stop_loss = row["max_6"]\n            session.take_profit = row["close"] - 1.5 * (row["max_6"] - row["close"])\n\n    # def on_<signal>(self, row: dict, session: Session) -> None:\n    #     """Custom signal handler, called for each open session.\n    #     We can adjust or close position or adjust brackets here."""\n    #     # session.position = 1\n    #     # session.position = base(1)  # same as the one above\n    #     # session.position = \'1\'  # int, str, float are being converted to Decimal\n    #     # session.position = quote(100)  # sets position worth 100 quote asset\n    #     # session.position += 1  # adds to the position\n    #     # session.position -= Decimal(\'1.25\')  # reduces position by 1.25\n    #     # session.position += percent(50)  # adds 50% more position\n    #     # session.position *= 1.5  # has the same effect as the one above\n    #     pass\n    #\n    # def on_take_profit(self, row: dict, session: Session) -> None:\n    #     """Called once take profit hit, default action - close position.\n    #     We can adjust the position and brackets here and let the session continue."""\n    #     session.position = 0\n    #\n    # def on_stop_loss(self, row: dict, session: Session) -> None:\n    #     """Called once stop loss hit, default action - close position.\n    #     We can adjust the position and brackets here and let the session continue."""\n    #     session.position = 0\n    #\n    # def on_stop(self, row: dict, session: Session) -> None:\n    #     """Called for each open session when the dataframe end reached.\n    #     We have an opportunity to close open sessions, otherwise - they will be ignored."""\n    #     session.position = 0\n\n\ndef main():\n    cipher = Cipher()\n    cipher.add_source("binance_spot_ohlc", symbol="BTCUSDT", interval="1h")\n    cipher.set_strategy(EmaCrossoverStrategy())\n    cipher.run(start_ts="2020-01-01", stop_ts="2020-04-01")\n    cipher.set_commission("0.0025")\n    print(cipher.sessions)\n    print(cipher.stats)\n    cipher.plot()\n\n\nif __name__ == "__main__":\n    main()\n```\n\n## Development\n\n```shell\nbrew install poetry\npoetry install\npoetry shell\n\npytest tests\n\ncipher --help\n```\n\n## Disclaimer\n\nThis software is for educational purposes only. Do not risk money which you are afraid to lose.\nUSE THE SOFTWARE AT YOUR OWN RISK. THE AUTHORS AND ALL AFFILIATES ASSUME NO RESPONSIBILITY FOR YOUR TRADING RESULTS.\n',
    'author': 'Oleksandr Polieno',
    'author_email': 'oleksandr@nanvel.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
