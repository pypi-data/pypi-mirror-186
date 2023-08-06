# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_json_config']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py-json-config',
    'version': '0.1.3',
    'description': 'JSONConfig was created to use .json files as configs',
    'long_description': '# JSONConfig\n\n### JSONConfig was created to use .json files as configs\n\n### You can create own functions to get values from the config and update values\n\n## How can i use it?\n\n*Use this command to install the module*\n```console\n$ > pip3 install py_json_config\n```\n\n## Simple tutorial\n\n*We are going to create some `Config` to add and get admins*\n\n#### Create `config.json` file in the root directory with content like this\n```json\n{\n    "admins": []\n}\n```\n\n#### Import the module into your main .py file\n```python\nimport py_json_config\n```\n\n#### Then you need to create some class with extend by the module\n```python \nclass Config(py_json_config.JSONConfig):\n    def get_admins(self):\n        return self.get_value(\'admins\') \n\n    def add_admin(self, admin):\n        admins = self.get_admins()\n        admins.append(admin)\n        self.set_value(\'admins\', admins)\n```\n\n#### That\\`s it! Now let`s test it\n\n```python\nconfig = Config(\'.config.json\')\n\nconfig.get_admins() # []\n\nconfig.add_admin(123)\n\nconfig.get_admins() # [123]\n```\n\n#### Now you can create own functions but you don`t know a main feature\n\n##### To get or update values you need to point the `path`, but if u have a complex structure you can use the "dot" operator like this:\n\n```python\n\n# the structure \n# \n# {\n#     "main": {\n#         "sub_main": {\n#             "admins": []\n#         }\n#     }\n# }\n\nclass Config(py_json_config.JSONConfig):\n    def get_admins(self):\n        return self.get_value(\'main.sub_main.admins\') \n\n    def add_admin(self, admin):\n        admins = self.get_admins()\n        admins.append(admin)\n        self.set_value(\'main.sub_main.admins\', admins)\n```\n\n## Ther are also others functions here:\n\n### `self._get_scheme`\nget data as dict of .json config\n\n### `self._save_scheme`\nsave data into .json config\n\n### `self.set_value`\nupdate value of .json config\n\n### `self.get_value`\nget value of .json config',
    'author': 'Enveloss',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>3.5',
}


setup(**setup_kwargs)
