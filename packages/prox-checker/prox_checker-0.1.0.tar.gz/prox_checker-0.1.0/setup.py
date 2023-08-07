# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['prox_checker']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp-socks>=0.7.1,<0.8.0',
 'aiohttp>=3.8.3,<4.0.0',
 'beautifulsoup4>=4.11.1,<5.0.0',
 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'prox-checker',
    'version': '0.1.0',
    'description': 'Async python proxy checker',
    'long_description': "# prox-checker\n**Async python proxy checker**\n\n\n### Features\n- **Works in 2023**\n- **No pycurl needed**, OS independent\n- **HTTP, Socks4, Socks5**\n- **Async**\n- **Fast** (<= 1.5kb per check)\n- Checks **availability** and **anonymity**\n- **Secure**, no data collecting\n- **Typed**\n\n\n## Installation\n`pip install prox-checker`\n\n## Usage\n```python\n...\n\nfrom prox_checker import ProxyChecker, ProxyProtocol, ProxyCheckerResult\n\n\nasync def check_my_proxies():\n    proxies = [\n        '144.24.207.98:8080',\n        '103.169.130.51:5678',\n        '198.58.126.147:51576',\n        '45.79.155.9:3128',\n        '206.220.175.2:4145',\n    ]\n\n    working_proxies: List[ProxyCheckerResult] = await ProxyChecker().check_proxies(\n        proxies=proxies,\n        proxy_async_limit=1_000,\n        protocol_async_limit=3,\n        response_timeout=5,\n    )\n\n    print(working_proxies)\n    '''\n    Output: \n    [\n        <ProxyCheckerResult url=http://144.24.207.98:8080 proxy=144.24.207.98:8080 protocol=ProxyProtocol.http>, \n        <ProxyCheckerResult url=socks4://198.58.126.147:51576 proxy=198.58.126.147:51576 protocol=ProxyProtocol.socks4>, \n        <ProxyCheckerResult url=socks5://198.58.126.147:51576 proxy=198.58.126.147:51576 protocol=ProxyProtocol.socks5>,\n        <ProxyCheckerResult url=socks4://206.220.175.2:4145 proxy=206.220.175.2:4145 protocol=ProxyProtocol.socks4>, \n        <ProxyCheckerResult url=socks5://206.220.175.2:4145 proxy=206.220.175.2:4145 protocol=ProxyProtocol.socks5>\n    ]\n    \n    Leaves only anon working proxies, separated by protocols\n    '''\n    socks5_urls = [\n        result.url\n        for result in working_proxies\n        if result.protocol == ProxyProtocol.socks5\n    ]\n    print(socks5_urls)  # ['socks5://198.58.126.147:51576', 'socks5://206.220.175.2:4145']\n\n    max_bandwidth_bytes_s = ProxyChecker.estimate_max_bandwidth_bytes_s(\n        proxy_async_limit=1_000,\n        protocol_async_limit=3,\n    )\n    max_bandwidth_mb_s = max_bandwidth_bytes_s / 1024 / 1024\n    print(max_bandwidth_mb_s)  # 4.39453125\n\n    custom_judges = [\n        'http://proxyjudge.us',\n        'http://azenv.net/',\n    ]\n    custom_judges_working_proxies = await ProxyChecker(judges=custom_judges).check_proxies(\n        proxies=proxies,\n        proxy_async_limit=1_000,\n        protocol_async_limit=3,\n        response_timeout=5,\n    )\n    print(custom_judges_working_proxies)  # same as first\n\n...\n\n```",
    'author': 'Anton Nechaev',
    'author_email': 'antonnechaev990@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/gh0st-work/prox-checker',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
