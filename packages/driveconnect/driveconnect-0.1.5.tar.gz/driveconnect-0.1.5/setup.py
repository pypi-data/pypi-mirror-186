# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['driveconnect']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'driveconnect',
    'version': '0.1.5',
    'description': 'Test whether a Windows drive is connected, and connect it.',
    'long_description': '# Installation\n\n```\npip install driveconnect\n```\nOr:\n```\npip install git+https:\\\\github.com\\gwangjinkim\\driveconnect.git\n```\n\n# Usage\n\n```\nimport driveconnect as dcn\n\n# test, wether a drive e.g. \'M:\' is connected:\ndcn.is_drive_connected(drive_letter=\'M\') # it works also with "M:"\n## False\n\n# set the credentials for the server in local folders\ndcn.pss.set_credentials(\'.\\.user\', \'.\\.pass\')\n\n# connect to the server\n# leading \'\\\\\' can be left out in server address and the \'M:\' as well as \'M\' both work\ndcn.connect_drive(\'M:\', \'\\\\serveraddress\\folder\', \'.\\.user\', \'.\\.pass\')\n\n# disconnect from the server\ndcn.disconnect_drive(\'M:\')\n```\n',
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
