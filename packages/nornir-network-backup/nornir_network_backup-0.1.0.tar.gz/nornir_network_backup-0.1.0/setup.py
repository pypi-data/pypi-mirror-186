# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nornir_network_backup',
 'nornir_network_backup.nornir',
 'nornir_network_backup.nornir.plugins',
 'nornir_network_backup.nornir.plugins.inventory',
 'nornir_network_backup.nornir.plugins.processors']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'nornir-netmiko>=0.2.0,<0.3.0',
 'nornir-utils>=0.2.0,<0.3.0',
 'nornir>=3.3.0,<4.0.0']

entry_points = \
{'console_scripts': ['nnb = nornir_network_backup.cli:base'],
 'nornir.plugins.inventory': ['NMAPInventory = '
                              'nornir_network_backup.plugins.inventory.nmap_discovery:NMAPDiscoveryInventory'],
 'nornir.plugins.processors': ['BackupReporter = '
                               'nornir_network_backup.plugins.processors.backup_reporter:BackupReporter']}

setup_kwargs = {
    'name': 'nornir-network-backup',
    'version': '0.1.0',
    'description': '',
    'long_description': '# nornir-network-backup\n\nA nornir playbook to store network equipment config backups and relevant "show" command facts.\n\nYou can define the main configuration backup command or fact commands per device type.\n\nThis backup tool uses Netmiko for connecting to devices and Textfsm to parse facts.\n\nRequirements:\n\n- nornir\n- nornir-utils\n- nornir-netmiko\n\n> This is a beta version. Extra options and documentation will follow soon !\n\n## Function\n\n- take the running config of 1 or more hosts and save it to a file\n  - the file will be overwritten every day\n  - optional take a diff of the previous file and save it as well\n- run "show" commands and save each output to a separate file in a facts folder\n  - files will be overwritten every time\n  - all files in a single facts folder\n  - save a file with meta data: info about the last backup time, commands executed, failed + successful commands\n  - the commands may change depending on vendor or hw type or software\n  - commands which can be parsed with textfsm will be saved as YAML, if they cannot be parsed then it will be .config text files\n- it should be possible to run the backup file for a single host\n- or run agains a complete file\n- generate an overall report with:\n  - last run time\n  - hosts succeeded\n  - hosts failed\n  - hosts skipped\n\n## Output folder structure\n\n```text\n|- backup folder\n|  |-- facts folder\n|  |-- reports folder  \n```\n\n## Commands\n\n```shell\nnnb backup\nnnb backup-single-host\n```\n\n## Usage\n\n```shell\npoetry run nnb backup-single-host\n```\n\n## Environment Variables\n\nUsed by nornir_utils.plugins.inventory.load_credentials transform function, in case username + password are not defined by CLI\n\nNORNIR_USERNAME\n\nNORNIR_PASSWORD\n',
    'author': 'mwallraf',
    'author_email': 'maarten.wallraf@orange.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
