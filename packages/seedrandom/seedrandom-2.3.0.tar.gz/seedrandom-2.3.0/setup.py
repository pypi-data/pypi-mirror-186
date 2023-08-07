# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['seedrandom']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'seedrandom',
    'version': '2.3.0',
    'description': 'Proof-of-concept seeded RNG lib',
    'long_description': '# seedrandom\nDeterministic seeded RNG\n\n[![Python Version](https://img.shields.io/pypi/pyversions/seedrandom.svg?color=yellow&style=flat-square)](https://www.python.org/downloads/)\n[![GitHub Licence](https://img.shields.io/github/license/BananaLoaf/seedrandom.svg?color=blue&style=flat-square)](https://github.com/BananaLoaf/seedrandom/blob/master/LICENSE)\n[![Package Version](https://img.shields.io/pypi/v/seedrandom.svg?color=green&style=flat-square)](https://pypi.org/project/seedrandom/)\n\n\n### Installation / Updating\n```\npip install seedrandom\npip install --upgrade seedrandom\n```\nOr\n```\npip install git+https://github.com/BananaLoaf/seedrandom.git\npip install --upgrade git+https://github.com/BananaLoaf/seedrandom.git\n```\n\n### Usage\n\n```python\nfrom seedrandom import SeededRNG\nrng = SeededRNG(b"Test", b"values", hash_func=hashlib.sha512)  # any hash func from hashlib\n```\n\nGenerating random values:\n```python\nrng.randint(a=0, b=1000)  # 893\nrng.randfloat(a=0, b=100, step=0.1)  # 89.3\nrng.randbool()  # False\nrng.randbyte()  # b\'\\xbf\'\n```\n\n```SeededRNG``` can be converted to and from ```int``` or ```bytes```:\n```python\nbytes(rng)\nint(rng)\n\nrng1 = SeededRNG.from_bytes(b\'\\xbb\\x9a\\xf3\\xe3\\x1d\\xfcA\\xcc\\xc5\\x93S\\x9a\\xec:\\x9a\\x08z\\x88\\x85\\x99\\xf7\\xea\\x91\\xb6x\\x00\\xfb\\x82"\\xc2$K\', hash_func=hashlib.blake2s)\nrng2 = SeededRNG.from_int(13391421701272821393603640485300504071883816826531413055648909144818643814535822212998295950921452703111178763035507290455800978052021014498426299707601814, hash_func=hashlib.sha512)\n```\n\n```ordered``` parameter can be used:\n```python\nrng1 = SeededRNG(b"Hello", b"world")\nrng2 = SeededRNG(b"world", b"Hello")\nrng1 == rng2  # True\n\nrng1 = SeededRNG(ordered=(b"Hello", b"world"))\nrng2 = SeededRNG(ordered=(b"world", b"Hello"))\nrng1 == rng2  # False\n\nrng1 = SeededRNG(b"Hello", b"world", ordered=(b"spanish", b"inquisition"))\nrng2 = SeededRNG(b"world", b"Hello", ordered=(b"spanish", b"inquisition"))\nrng1 == rng2  # True\n\nrng1 = SeededRNG(b"Hello", b"world", ordered=(b"spanish", b"inquisition"))\nrng2 = SeededRNG(b"Hello", b"world", ordered=(b"inquisition", b"spanish"))\nrng1 == rng2  # False\n```\n',
    'author': 'BananaLoaf',
    'author_email': 'bananaloaf@protonmail.com',
    'maintainer': 'BananaLoaf',
    'maintainer_email': 'bananaloaf@protonmail.com',
    'url': 'https://github.com/BananaLoaf/seedrandom',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
