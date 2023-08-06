# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['driveconnect']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'driveconnect',
    'version': '0.1.15',
    'description': 'Test whether a Windows drive is connected, and connect it.',
    'long_description': '# Installation\n\n```\npip install driveconnect\n```\nOr:\n```\npip install git+https:\\\\github.com\\gwangjinkim\\driveconnect.git\n```\nOr:\n```\npipenv install git+https:\\\\github.com\\gwangjinkim\\driveconnect.git#egg=driveconnect\n```\nOr:\n```\npoetry add driveconnect  # version number: driveconnect==0.1.8\n```\nOr (from github repo):\n```\npoetry add git+ssh://git@github.com/gwangjinkim/driveconnect.git#main\n```\n\n# Usage\n\n```\nimport driveconnect as dcn\nimport pycryptaes as pca\nimport logging as log\n\nprint(dcn.__version__)\n\n# set better pretty print for log message on stdout:\ndcn.set_pprint_width(width=81)\n\n# instanciate encryptor\nca = pca.AES()\n# for saving some typing on REPL:\nhome = "C:/Users/myusername"\np = lambda x: f"{home}/{x}"\nargs = (p(".key"), p(".user"), p(".pass"))\n\n# set logger\nlog.basicConfig(filename=f"{home}/mylog.log", filemode=\'a\', level=log.DEBUG)\n\n\n# if first time using credentials, you have to enter username and password after typing:\nca.generate_key_user_pass(*args)\n\n# otherwise comment out the previous line and collect/read the previously saved credentials:\nco = ca.read_key_user_pass(*args)           # `co` = `Credential Object`\n\n# now you can test, wether a drive e.g. \'G:\' is connected:\ndcn.is_drive_connected(drive_letter=\'G\') # it works also with "G:"\n## False\n\n# connect to the server\n# leading \'\\\\\' can be left out in server address and the \'M:\' as well as \'M\' both work\ndcn.connect_drive(\'G:\', \'\\\\serveraddress\\folder\', co=co, log=log, level="info")\n# or for connections where no credentials are needed:\ndcn.connect_drive(\'G:\', \'\\\\serveraddress\\folder\', log=log, level="info", _print=True)\n# `log=`, `level=` and `_print=` are optional.\n\n# disconnect from the server\ndcn.disconnect_drive(\'G:\', log=log, level="info", _print=True)\n# or without logger:\ndcn.disconnect_drive(\'G:\', _print=True)\n```\n',
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
