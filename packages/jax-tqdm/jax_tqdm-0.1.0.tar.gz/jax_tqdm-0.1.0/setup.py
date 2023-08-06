# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['jax_tqdm']

package_data = \
{'': ['*']}

install_requires = \
['jax>=0.3.5', 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'jax-tqdm',
    'version': '0.1.0',
    'description': 'Tqdm progress bar for JAX scans and loops',
    'long_description': '# JAX-tqdm\n\nAdd a tqdm progress bar to your JAX scans and loops.\n\nThe code is explained in this [blog post](https://www.jeremiecoullon.com/2021/01/29/jax_progress_bar/).\n\n## Example usage\n\n### in `jax.lax.scan`\n\n```python\nfrom jax_tqdm import scan_tqdm\nfrom jax import lax\nimport jax.numpy as jnp\n\nn = 10_000\n\n@scan_tqdm(n)\ndef step(carry, x):\n    return carry + 1, carry + 1\n\nlast_number, all_numbers = lax.scan(step, 0, jnp.arange(n))\n```\n\n\n### in `jax.lax.fori_loop`\n\n```python\nfrom jax_tqdm import loop_tqdm\nfrom jax import lax\n\nn = 10_000\n\n@loop_tqdm(n)\ndef step(i, val):\n    return val + 1\n\nlast_number = lax.fori_loop(0, n, step, 0)\n```\n',
    'author': 'Jeremie Coullon',
    'author_email': 'jeremie.coullon@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/jeremiecoullon/jax-tqdm',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
