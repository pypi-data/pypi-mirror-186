# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['alns',
 'alns.accept',
 'alns.accept.tests',
 'alns.select',
 'alns.select.tests',
 'alns.stop',
 'alns.stop.tests',
 'alns.tests']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=2.2.0', 'numpy>=1.15.2']

setup_kwargs = {
    'name': 'alns',
    'version': '5.0.4',
    'description': 'A flexible implementation of the adaptive large neighbourhood search (ALNS) algorithm.',
    'long_description': '[![PyPI version](https://badge.fury.io/py/alns.svg)](https://badge.fury.io/py/alns)\n[![ALNS](https://github.com/N-Wouda/ALNS/actions/workflows/alns.yaml/badge.svg)](https://github.com/N-Wouda/ALNS/actions/workflows/alns.yaml)\n[![Documentation Status](https://readthedocs.org/projects/alns/badge/?version=latest)](https://alns.readthedocs.io/en/latest/?badge=latest)\n[![codecov](https://codecov.io/gh/N-Wouda/ALNS/branch/master/graph/badge.svg)](https://codecov.io/gh/N-Wouda/ALNS)\n\n``alns`` is a general, well-documented and tested implementation of the adaptive\nlarge neighbourhood search (ALNS) metaheuristic in Python. ALNS is an algorithm\nthat can be used to solve difficult combinatorial optimisation problems. The\nalgorithm begins with an initial solution. Then the algorithm iterates until a\nstopping criterion is met. In each iteration, a destroy and repair operator are\nselected, which transform the current solution into a candidate solution. This\ncandidate solution is then evaluated by an acceptance criterion, and the\noperator selection scheme is updated based on the evaluation outcome.\n\n`alns` depends only on `numpy` and `matplotlib`. It may be installed in the\nusual way as\n\n```\npip install alns\n```\n\nThe documentation is available [here][1].\n\n### Getting started\n\nIf you are new to metaheuristics or ALNS, you might benefit from reading\nthe [introduction to ALNS][11] page.\n\nThe `alns` library provides the ALNS algorithm and various acceptance criteria,\noperator selection schemes, and stopping criteria. To solve your own problem,\nyou should provide the following:\n\n- A solution state for your problem that implements an `objective()` function.\n- An initial solution.\n- One or more destroy and repair operators tailored to your problem.\n\nA "quickstart" code template is available [here][10].\n\n### Examples\n\nWe provide several example notebooks showing how the ALNS library may be used.\nThese include:\n\n- The travelling salesman problem (TSP), [here][2]. We solve an instance of 131\n  cities using very simple destroy and repair heuristics.\n- The capacitated vehicle routing problem (CVRP), [here][8]. We solve an\n  instance with 241 customers using a combination of a greedy repair operator,\n  and a _slack-induced substring removal_ destroy operator.\n- The cutting-stock problem (CSP), [here][4]. We solve an instance with 180\n  beams over 165 distinct sizes in only a very limited number of iterations.\n- The resource-constrained project scheduling problem (RCPSP), [here][6]. We\n  solve an instance with 90 jobs and 4 resources using a number of different\n  operators and enhancement techniques from the literature.\n- The permutation flow shop problem (PFSP), [here][9]. We solve an instance with\n  50 jobs and 20 machines. Moreover, we demonstrate multiple advanced features\n  of ALNS, including auto-fitting the acceptance criterion and adding local\n  search to repair operators. We also demonstrate how one could tune ALNS\n  parameters.\n\nFinally, the features notebook gives an overview of various options available in\nthe `alns` package. In the notebook we use these different options to solve a\ntoy 0/1-knapsack problem. The notebook is a good starting point for when you\nwant to use different schemes, acceptance or stopping criteria yourself. It is\navailable [here][5].\n\n### Contributing\n\nWe are very grateful for any contributions you are willing to make. Please have\na look [here][3] to get started. If you aim to make a large change, it is\nhelpful to discuss the change first in a new GitHub issue. Feel free to open\none!\n\n### Getting help\n\nIf you are looking for help, please follow the instructions [here][7].\n\n[1]: https://alns.readthedocs.io/en/latest/\n\n[2]: https://alns.readthedocs.io/en/latest/examples/travelling_salesman_problem.html\n\n[3]: https://alns.readthedocs.io/en/latest/setup/contributing.html\n\n[4]: https://alns.readthedocs.io/en/latest/examples/cutting_stock_problem.html\n\n[5]: https://alns.readthedocs.io/en/latest/examples/alns_features.html\n\n[6]: https://alns.readthedocs.io/en/latest/examples/resource_constrained_project_scheduling_problem.html\n\n[7]: https://alns.readthedocs.io/en/latest/setup/getting_help.html\n\n[8]: https://alns.readthedocs.io/en/latest/examples/capacitated_vehicle_routing_problem.html\n\n[9]: https://alns.readthedocs.io/en/latest/examples/permutation_flow_shop_problem.html\n\n[10]: https://alns.readthedocs.io/en/latest/setup/template.html\n\n[11]: https://alns.readthedocs.io/en/latest/setup/introduction_to_alns.html\n',
    'author': 'Niels Wouda',
    'author_email': 'nielswouda@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/N-Wouda/ALNS',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
