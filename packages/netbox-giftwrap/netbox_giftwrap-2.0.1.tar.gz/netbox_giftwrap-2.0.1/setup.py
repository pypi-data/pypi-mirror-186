# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['netbox_giftwrap']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'aiofiles>=22.1.0,<23.0.0',
 'aiohttp>=3.8.3,<4.0.0',
 'rich-click>=1.3.0,<2.0.0']

entry_points = \
{'console_scripts': ['netbox_giftwrap = netbox_giftwrap.script:run']}

setup_kwargs = {
    'name': 'netbox-giftwrap',
    'version': '2.0.1',
    'description': 'Transform NetBox APIs into Business Ready Documents',
    'long_description': '![Logo](/images/netbox_giftwrap.png)\n# netbox_giftwrap\nTransform NetBox APIs into Business Ready formats\n\n## Installing netbox_giftwrap\nTo install netbox_giftwrap there are a few simple steps:\n#### Ubuntu Linux \n##### The following instructions are based on Windows WSL2 and Ubuntu however any flavour of Linux will work with possibly slightly different commands.\n\n##### Confirm Python 3 is installed\n\n#####\n```console\n\n$ python3 -V\nPython 3.9.10\n\n```\n\n##### Create and activate a virtual environment\n\n######\n```console\n\n$ sudo apt install python3-venv\n$ python3 -m venv netbox_giftwrap\n$ source netbox_giftwrap/bin/activate\n(netbox_giftwrap)$\n\n```\n##### Install the netbox_giftwrap\n```console\n\n(netbox_giftwrap)$pip install netbox_giftwrap\n\n```\n\n##### Create an output folder\n```console\n\n(netbox_giftwrap)$mkdir output\n\n```\n### Windows\n\n#### [Download Python](https://python.org)\n#### Create and activate a virtual environment\n#####\n```console\n\nC:\\>python3 -m venv netbox_giftwrap\nC:\\>netbox_giftwrap\\Scripts\\activate\n(netbox_giftwrap) C:\\>\n\n```\n#### Install netbox_giftwrap\n```console\n\n(message_room)$pip install netbox_giftwrap\n\n```\n\n##### Create an output folder\n```console\n\n(netbox_giftwrap)$mkdir output\n\n```\n## Using the bot\n### Run the bot as an interactive session\n```console\n\n(netbox_giftwrap)$ cd output\n(netbox_giftwrap)$~/output/netbox_giftwrap.py\n\n```\n\n### The form questions:\n\n##### Question 1 - NetBox URL:\n\nEnter the URL of your NetBox instance (e.g. https://demo.netbox.dev):\n\nThis can be set as an environment variable\n\n##### Question 2 - NetBox API Token: \n\nEnter your NetBox API Token - you can create / retrieve one from https://URL/user/api-tokens/\n\nThis can be set as an environment variable\n\n#### Current API Covera\n\naggregates\n\nasns\n\ncables\n\ncircuit-terminations\n\ncircuit-types\n\ncircuits\n\ncluster-groups\n\ncluster-types\n\nclusters\n\nconsole-port-templates\n\nconsole-ports\n\ncontact-assignments\n\ncontact-groups\n\ncontact-roles\n\ncontacts\n\ndevice-bay-templates\n\ndevice-bays\n\ndevice-roles\n\ndevice-types\n\ndevices\n\nfront-port-templates\n\nfront-ports\n\ngroups\n\ninterface-templates\n\ninterfaces\n\ninventory-items\n\nip-addresses\n\nip-ranges\n\nlocations\n\nmanufacturers\n\nmodule-bay-templates\n\nmodule-bays\n\nmodule-types\n\nmodules\n\nplatforms\n\npower-feeds\n\npower-outlet-templates\n\npower-outlets\n\npower-panels\n\npower-port-templates\n\npower-ports\n\nprefixes\n\nprovider-networks\n\nproviders\n\nrack-reservations\n\nrack-roles\n\nracks\n\nrear-port-templates\n\nrear-ports\n\nregions\n\nrirs\n\nroles\n\nroute-targets\n\nservice-templates\n\nservices\n\nsite-groups\n\nsites\n\nstatus\n\ntenant-groups\n\ntenants\n\ntokens\n\nusers\n\nvirtual-chassis\n\nvirtual-interfaces\n\nvirtual-machines\n\nvlan-groups\n\nvlans',
    'author': 'John Capobianco',
    'author_email': 'ptcapo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
