# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['criminal_dance',
 'criminal_dance.game',
 'criminal_dance.game.dog',
 'criminal_dance.game.hard',
 'criminal_dance.room']

package_data = \
{'': ['*']}

install_requires = \
['ayaka>=0.0.1.2,<0.0.2.0']

setup_kwargs = {
    'name': 'criminal-dance',
    'version': '0.0.1b2',
    'description': '犯人在跳舞',
    'long_description': '# 犯人在跳舞 - 先行测试版 0.0.1b2\n\n- 第一发现人 √\n- 共犯 √\n- 普通人 √\n- 不在场证明 √\n- 目击者 √\n- 犯人 √\n- 侦探 √\n- 警部 √\n- 神犬 √\n- 谣言 √\n\n## 代码重构中\n\n- 交易 \n- 情报交换 ',
    'author': 'Su',
    'author_email': 'wxlxy316@163.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/bridgeL/criminal_dance',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
