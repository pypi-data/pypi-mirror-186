# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ykman',
 'ykman._cli',
 'ykman.hid',
 'ykman.pcsc',
 'ykman.scancodes',
 'yubikit',
 'yubikit.core']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0,<9.0',
 'cryptography>=3.0,<42',
 'fido2>=1.0,<2.0',
 'keyring>=23.4,<24.0',
 'pyscard>=2.0,<3.0']

extras_require = \
{':sys_platform == "win32"': ['pywin32>=223']}

entry_points = \
{'console_scripts': ['ykman = ykman._cli.__main__:main']}

setup_kwargs = {
    'name': 'yubikey-manager',
    'version': '5.0.1',
    'description': 'Tool for managing your YubiKey configuration.',
    'long_description': 'None',
    'author': 'Dain Nilsson',
    'author_email': 'dain@yubico.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Yubico/yubikey-manager',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
