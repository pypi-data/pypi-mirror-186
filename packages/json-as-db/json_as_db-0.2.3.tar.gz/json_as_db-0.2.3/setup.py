# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['json_as_db']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=22.1.0', 'shortuuid>=1.0.11']

setup_kwargs = {
    'name': 'json-as-db',
    'version': '0.2.3',
    'description': 'Using JSON as very lightweight database',
    'long_description': '# JSON-as-DB\n\n![Python Version Badge] [![RTD](https://readthedocs.org/projects/json-as-db/badge/?version=latest)](https://json-as-db.readthedocs.io/) [![PyTest Badge]](https://github.com/joonas-yoon/json-as-db/actions/workflows/pytest.yml) ![PyPI Version Badge] ![PyPI Download Badge] [![Hits Badge]](#)\n\nUsing JSON as very lightweight database\n\n```python\n>>> db = Database()\n>>> db.load(\'output.json\')   # Load database from file\n>>> db.add([{                # Add items what you want to add\n...   "id": "1002",\n...   "type": "Chocolate"\n... })\n[\'FqkmbYFSCRCAHQWydhM69v\', \'RUJGcVBFANvNRReXa8U3En\']\n>>> db.save(\'output.json\', json_kwds={\'indent\': 4})   # Just save it into file.\n```\n\n```js\n// output.json\n{\n    "created_at": "2022-12-25T16:50:02.459068",\n    "creator": "json_as_db",\n    "data": {\n        "FqkmbYFSCRCAHQWydhM69v": {\n            "id": "1001",\n            "type": "Regular"\n        },\n        "RUJGcVBFANvNRReXa8U3En": {\n            "id": "1002",\n            "type": "Chocolate"\n        }\n    },\n    "updated_at": "2022-12-28T16:51:36.276790",\n    "version": "1.0.0"\n}\n```\n\n## Documentation\n\n- Read the Docs - https://json-as-db.readthedocs.io/\n\n## Installation\n\nInstalling via pip:\n\n```bash\npip install json-as-db\n```\n\nInstalling via GitHub repository,\n\n```bash\ngit clone https://github.com/joonas-yoon/json-as-db.git\npip install -e json-as-db\n```\n\n## Contributing\n\nContributing guidelines can be found [CONTRIBUTING.md](CONTRIBUTING).\n\nWelcome all contributions to the community and feel free to contribute.\n\n## License\n\nUnder the MIT license. See the [LICENSE] file for more info.\n\n\n[Python Version Badge]: https://img.shields.io/pypi/pyversions/json-as-db?style=flat-square\n[PyTest Badge]: https://github.com/joonas-yoon/json-as-db/actions/workflows/pytest.yml/badge.svg\n[PyPI Version Badge]: https://img.shields.io/pypi/v/json-as-db?style=flat-square\n[PyPI Download Badge]: https://img.shields.io/pypi/dm/json-as-db?style=flat-square\n[Hits Badge]: https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fjoonas-yoon%2Fjson-as-db\n[CONTRIBUTING]: CONTRIBUTING.md\n[LICENSE]: LICENSE\n',
    'author': 'Joonas',
    'author_email': 'joonas.yoon@gmail.com',
    'maintainer': 'Joonas',
    'maintainer_email': 'joonas.yoon@gmail.com',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
