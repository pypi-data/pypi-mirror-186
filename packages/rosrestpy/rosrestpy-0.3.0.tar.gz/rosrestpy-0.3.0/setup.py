# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ros',
 'ros.inteface',
 'ros.inteface.bridge',
 'ros.inteface.ethernet',
 'ros.inteface.list',
 'ros.ip',
 'ros.ip.dhcp_server',
 'ros.ip.dns',
 'ros.ppp',
 'ros.queue',
 'ros.routing',
 'ros.system',
 'ros.system.package',
 'ros.tool']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.0.0,<=23.0.0', 'cattrs>=21.0.0,<=23.0.0', 'requests>=2.28.1,<3.0.0']

extras_require = \
{'ujson': ['ujson>=5.5.0,<6.0.0']}

setup_kwargs = {
    'name': 'rosrestpy',
    'version': '0.3.0',
    'description': 'RouterOS v7 REST API python module',
    'long_description': '# RosRestPy\n\n[![PyPi Package Version](https://img.shields.io/pypi/v/rosrestpy)](https://pypi.org/project/rosrestpy/)\n[![Supported Python versions](https://img.shields.io/pypi/pyversions/rosrestpy)](https://pypi.org/project/rosrestpy/)\n[![LICENSE](https://img.shields.io/github/license/hexatester/rosrestpy)](https://github.com/hexatester/rosrestpy/blob/main/LICENSE)\n\nRouterOS v7 REST API python module\n\n## RouterOS v7 REST API Support\n\nNot all types and methods of the RouterOS v7 REST API are supported, yet.\n\n## Installing\n\nYou can install or upgrade rosrestpy with:\n\n```bash\npip install rosrestpy --upgrade\n```\n\n## Example\n\n```python\nfrom ros import Ros\n\nros = Ros("https://192.168.88.1/", "admin", "")\nif ros.system.resource.cpu_load > 90:\n    print(f"{ros.system.identity}\'s CPU > 90%")\n\nfor interface in ros.interface():\n    print(interface.name)\n\nqueues = ros.queue.simple(name="Hotspot")\nif len(queues) == 1:\n    queue = queues[0]\n    print(f"Usage {queue.bytes}")\n\nbw_tests = ros.tool.bandwith_test("172.16.0.1", "3s", "admin", direction="both")\nresult_bw_test = bw_tests[-1]\nprint(f"Download {result_bw_test.rx_total_average}")\nprint(f"Upload {result_bw_test.tx_total_average}")\n```\n\n## Resources\n\nThe [RouterOS REST API](https://help.mikrotik.com/docs/display/ROS/REST+API) is the technical reference for `rosrestpy`.\n\n## Contributing\n\nContributions of all sizes are welcome. Please review our [contribution guidelines](https://github.com/hexatester/rosrestpy/blob/main/CONTRIBUTING.md "How To Contribute") to get started. You can also help by [reporting bugs or feature requests](https://github.com/hexatester/rosrestpy/issues/new/choose).\n',
    'author': 'hexatester',
    'author_email': 'hexatester@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/hexatester/rosrestpy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
