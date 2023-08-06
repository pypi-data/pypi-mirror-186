# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fraud_eagle']

package_data = \
{'': ['*']}

install_requires = \
['networkx>=3.0,<4.0', 'numpy>=1.24.1,<2.0.0']

setup_kwargs = {
    'name': 'rgmining-fraud-eagle',
    'version': '0.10.0',
    'description': 'An implementation of Fraud Eagle algorithm',
    'long_description': 'Fraud Eagle Algorithm\n=====================\n\n|GPLv3| |Build Status| |Maintainability| |Test Coverage| |Release|\n|Japanese|\n\n|Logo|\n\nThis package provides an implementation of Fraud Eagle algorithm. This\nalgorithm has been introduced by Leman Akoglu, *et al.* in `ICWSM\n2013 <https://www.aaai.org/ocs/index.php/ICWSM/ICWSM13/paper/viewFile/5981/6338>`__\n\nSee `the documents <https://rgmining.github.io/fraud-eagle/>`__ for more\ninformation.\n\nInstallation\n------------\n\nUse ``pip`` to install this package.\n\n::\n\n    pip install --upgrade rgmining-fraud-eagle\n\nLicense\n-------\n\nThis software is released under The GNU General Public License Version\n3, see\n`COPYING <https://github.com/rgmining/fraud-eagle/blob/master/COPYING>`__\nfor more detail.\n\n.. |GPLv3| image:: https://img.shields.io/badge/license-GPLv3-blue.svg\n   :target: https://www.gnu.org/copyleft/gpl.html\n.. |Build Status| image:: https://github.com/rgmining/fraud-eagle/actions/workflows/python-lib.yaml/badge.svg\n   :target: https://github.com/rgmining/fraud-eagle/actions/workflows/python-lib.yaml\n.. |Maintainability| image:: https://api.codeclimate.com/v1/badges/cf5f0ee2f7f5aa6bd846/maintainability\n   :target: https://codeclimate.com/github/rgmining/fraud-eagle/maintainability\n.. |Test Coverage| image:: https://api.codeclimate.com/v1/badges/cf5f0ee2f7f5aa6bd846/test_coverage\n   :target: https://codeclimate.com/github/rgmining/fraud-eagle/test_coverage\n.. |Release| image:: https://img.shields.io/badge/release-0.10.0-brightgreen.svg\n   :target: https://pypi.org/project/rgmining-fraud-eagle/\n.. |Japanese| image:: https://img.shields.io/badge/qiita-%E6%97%A5%E6%9C%AC%E8%AA%9E-brightgreen.svg\n   :target: http://qiita.com/jkawamoto/items/d2284316cc37cd810bfd\n.. |Logo| image:: https://rgmining.github.io/fraud-eagle/_static/image.png\n   :target: https://rgmining.github.io/fraud-eagle/\n',
    'author': 'Junpei Kawamoto',
    'author_email': 'kawamoto.junpei@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://rgmining.github.io/frad-eagle/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
