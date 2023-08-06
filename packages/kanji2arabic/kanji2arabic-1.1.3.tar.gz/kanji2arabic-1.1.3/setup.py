# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kanji2arabic']

package_data = \
{'': ['*']}

install_requires = \
['kanjize==1.3.0']

setup_kwargs = {
    'name': 'kanji2arabic',
    'version': '1.1.3',
    'description': 'Convert Kanji numerals to Arabic numerals.',
    'long_description': '# kanji2arabic_number\n\nConvert Kanji numerals to Arabic numerals.\n\npowerd by [Interman co., ltd](https://interman.jp/)\n\n[GitHub](https://github.com/interman-corp/kanji2arabic)\n\n## Demo\n\n```python\nfrom kanji2arabic import Kanji2Arabic\n\nprint(Kanji2Arabic.kanji2arabic("一二三"))\n  # "123"\n\nprint(Kanji2Arabic.kanji2arabic("百二十三"))\n  # "123"\n\nprint(Kanji2Arabic.kanji2arabic("二〇二〇"))\n  # "2020"\n\nprint(Kanji2Arabic.arabic2kanji("1230456"))\n  # "一二三〇四五六"\n\n```\n\n## Requirements\n\nkanjize 1.3.0\n',
    'author': 'hgs-interman',
    'author_email': 'system@interman.co.jp',
    'maintainer': 'hgs-interman',
    'maintainer_email': 'system@interman.co.jp',
    'url': 'https://github.com/interman-corp/kanji2arabic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
