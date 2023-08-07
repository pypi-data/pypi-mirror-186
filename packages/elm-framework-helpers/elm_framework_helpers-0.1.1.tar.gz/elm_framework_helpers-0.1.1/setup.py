# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['elm_framework_helpers', 'elm_framework_helpers.output']

package_data = \
{'': ['*']}

install_requires = \
['reactivex>=4.0.4,<5.0.0']

setup_kwargs = {
    'name': 'elm-framework-helpers',
    'version': '0.1.1',
    'description': '',
    'long_description': "# Helpers for the ELM framework scripts\n\n## Logging\n\nHere's a sample logging for production:\n\n```\n[loggers]\nkeys=root,Rx,rawsocket\n\n[handlers]\nkeys=consoleHandler,fileHandler,socketFileHandler\n\n[formatters]\nkeys=fileFormatter,consoleFormatter,socketFileFormatter\n\n[logger_root]\nlevel=DEBUG\nhandlers=consoleHandler,fileHandler\n\n[logger_Rx]\nlevel=INFO\nhandlers=consoleHandler\nqualname=Rx\n\n[logger_rawsocket]\nqualname=bittrade_kraken_websocket.connection.generic.raw\nhandlers=socketFileHandler\n\n[handler_consoleHandler]\nclass=StreamHandler\nlevel=INFO\nformatter=consoleFormatter\nargs=(sys.stdout,)\n\n[handler_fileHandler]\nclass=FileHandler\nlevel=DEBUG\nformatter=fileFormatter\nargs=('logfile.log',)\n\n[handler_socketFileHandler]\nclass=FileHandler\nlevel=DEBUG\nformatter=socketFileFormatter\nargs=('raw_socket.log',)\n\n[formatter_fileFormatter]\nformat=%(asctime)s   - %(name)s - %(levelname)s - %(message)s\ndatefmt=%H:%M:%S\n\n[formatter_socketFileFormatter]\nformat=%(asctime)s - %(message)s\ndatefmt=%H:%M:%S\n\n[formatter_consoleFormatter]\nformat=%(asctime)s   - %(levelname)s - %(message)s\ndatefmt=%H:%M:%S\n```",
    'author': 'Mat',
    'author_email': 'mathieu@redapesolutions.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/TechSpaceAsia/elm-framework-helpers',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
