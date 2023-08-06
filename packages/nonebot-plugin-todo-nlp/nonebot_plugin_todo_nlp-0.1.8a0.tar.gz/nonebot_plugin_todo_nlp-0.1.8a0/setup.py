# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_todo_nlp']

package_data = \
{'': ['*'], 'nonebot_plugin_todo_nlp': ['templates/*', 'templates/css/*']}

install_requires = \
['jionlp>=1.4.17,<2.0.0',
 'nonebot-adapter-onebot>=2.1.3,<3.0.0',
 'nonebot-plugin-apscheduler>=0.1.4,<0.2.0',
 'nonebot-plugin-htmlrender>=0.1.1,<0.2.0',
 'nonebot2>=2.0.0-beta.5,<3.0.0',
 'pandas>=1.4.3,<2.0.0',
 'pathlib>=1.0.1,<2.0.0']

setup_kwargs = {
    'name': 'nonebot-plugin-todo-nlp',
    'version': '0.1.8a0',
    'description': '一款自动识别提醒内容，可生成todo图片并定时推送的nonebot2插件',
    'long_description': 'None',
    'author': 'CofinCup',
    'author_email': '864341840@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
