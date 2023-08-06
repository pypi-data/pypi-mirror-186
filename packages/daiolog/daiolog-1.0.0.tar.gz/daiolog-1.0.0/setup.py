# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['daiolog']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'daiolog',
    'version': '1.0.0',
    'description': 'JSON logging in a separate thread for asyncio projects',
    'long_description': '# Do asyncio logging\n\nJSON logging in a separate thread for asyncio projects\n\n## Basic Usage\n\n```python\nimport os\nimport logging\nimport logging.config\nfrom daiolog import QueueListener\n\nLOGGING_CONFIG = { \n    \'version\': 1,\n    \'disable_existing_loggers\': True,\n    \'handlers\': { \n        \'default\': { \n            \'level\': \'INFO\',\n            \'class\': \'daiolog.QueueHandler\',\n        },\n    },\n    \'loggers\': { \n        \'\': {  # root logger\n            \'handlers\': [\'default\'],\n            \'level\': \'WARNING\',\n            \'propagate\': False\n        },\n        \'my.packg\': { \n            \'handlers\': [\'default\'],\n            \'level\': \'INFO\',\n            \'propagate\': False\n        },\n    } \n}\n\nlogging.config.dictConfig(LOGGING_CONFIG)\n\n\ndef main():\n    logger = logging.getLogger(\'my.packg\')\n    logger.info(\'Start main\', extra={\'pid\': os.getpid()})\n    ...\n    logger.info(\'Finish main\', extra={\'pid\': os.getpid()})\n\nif __name__ == \'__main__\':\n    QueueListener().start()\n    main()\n    QueueListener().stop()\n\n\n# {"logger_name": "my.packg", "level": "INFO", "timestamp": "2023-01-16T09:21:43.511+00:00", "message": "Start main", "pathname": "__main__.py", "module": "__main__", "function": "main", "line": 35, "traceback": null, "extra": {"pid": 60720}}\n# {"logger_name": "my.packg", "level": "INFO", "timestamp": "2023-01-16T09:21:43.512+00:00", "message": "Finish main", "pathname": "__main__.py", "module": "__main__", "function": "main", "line": 37, "traceback": null, "extra": {"pid": 60720}}\n```\n',
    'author': 'Vladislav Vorobyov',
    'author_email': 'vladislav.vorobyov@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/anysoft-kz/daiolog',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
