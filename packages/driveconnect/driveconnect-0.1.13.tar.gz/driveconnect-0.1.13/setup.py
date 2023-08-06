# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['driveconnect']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'driveconnect',
    'version': '0.1.13',
    'description': 'Test whether a Windows drive is connected, and connect it.',
    'long_description': '# Installation\n\n```\npip install driveconnect\n```\nOr:\n```\npip install git+https:\\\\github.com\\gwangjinkim\\driveconnect.git\n```\nOr:\n```\npipenv install git+https:\\\\github.com\\gwangjinkim\\driveconnect.git#egg=driveconnect\n```\nOr:\n```\npoetry add driveconnect  # version number: driveconnect==0.1.8\n```\nOr (from github repo):\n```\npoetry add git+ssh://git@github.com/gwangjinkim/driveconnect.git#main\n```\n\n# Usage\n\n```\nimport driveconnect as dcn\nimport pycryptaes as pca\nimport logging\n\n# instanciate encryptor\nca = pca.AES()\n\n# set logger\nlogging.basicConfig(filename=\'mylog.log\', filemode=\'a\', level=logging.DEBUG)\n\n# test, wether a drive e.g. \'G:\' is connected:\ndcn.is_drive_connected(drive_letter=\'G\') # it works also with "G:"\n## False\n\n# in the terminal/console/REPL to save some typing:\nhome = "C:/Users/myusername"\np = lambda x: f"{home}/{x}"   # helper function\nargs = (p(".key"), p(".user"), p(".pass"))\n\n# set the credentials for the server in local folders\nca.generate_key_user_pass(*args)\n\n# connect to the server\n# leading \'\\\\\' can be left out in server address and the \'M:\' as well as \'M\' both work\ndcn.connect_drive(\'G:\', \'\\\\serveraddress\\folder\', co=co)\n# or for connections where no credentials are needed:\ndcn.connect_drive(\'G:\', \'\\\\serveraddress\\folder\', _print=True)\n# or with logger\ndcn.connect_drive(\'G:\', \'\\\\serveraddress\\folder\', log=logging, level="info", _print=True)\n\n\n\n# disconnect from the server\ndcn.disconnect_drive(\'G:\', _print=True)\n# or with logger:\ndcn.disconnect_drive(\'G:\', log=logging, level="info")\n```\n',
    'author': 'Gwang-Jin Kim',
    'author_email': 'gwang.jin.kim.phd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
