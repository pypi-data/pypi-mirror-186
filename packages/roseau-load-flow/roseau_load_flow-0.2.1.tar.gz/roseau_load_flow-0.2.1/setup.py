# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['load_flow',
 'load_flow.io',
 'load_flow.models',
 'load_flow.models.lines',
 'load_flow.models.loads',
 'load_flow.models.transformers',
 'load_flow.network',
 'load_flow.utils']

package_data = \
{'': ['*']}

install_requires = \
['Shapely>=1.8.0,<2.0.0',
 'geopandas>=0.10.2',
 'numpy>=1.21.5,<2.0.0',
 'pandas>=1.4.0,<2.0.0',
 'pint>=0.19.2',
 'pygeos>=0.12.0',
 'regex>=2022.1.18',
 'requests>=2.28.1,<3.0.0',
 'rich>=11.0.0']

setup_kwargs = {
    'name': 'roseau-load-flow',
    'version': '0.2.1',
    'description': 'Three-phase load flow solver',
    'long_description': '![CI](https://github.com/RoseauTechnologies/Roseau_Load_Flow/workflows/CI/badge.svg)\n\n# Roseau Load Flow #\n\n## Installation ##\n\nThe simplest way is to download the docker container attached to this repository and to start it. I will start a\nJupyterlab session with the package installed.\n\n## Usage ##\n\nThere are 2 main ways to execute a load flow with thunders:\n\n### From files ###\n\nBy giving path to the needed files:\n\n```python\nfrom roseau.load_flow import ElectricalNetwork\n\nen = ElectricalNetwork.from_dgs(path=path)  # DGS\n\nen = ElectricalNetwork.from_json(path=path)  # Json\n\nen.solve_load_flow(auth=("username", "password"))\n```\n\n### From code ###\n\nBy describing the network and its components, here is a simple example:\n\n```python\nfrom roseau.load_flow import Ground, VoltageSource, Bus, PowerLoad, PotentialRef, SimplifiedLine, ElectricalNetwork, LineCharacteristics\nimport numpy as np\n\nground = Ground()\nvn = 400 / np.sqrt(3)\nvoltages = [vn, vn * np.exp(-2 / 3 * np.pi * 1j), vn * np.exp(2 / 3 * np.pi * 1j)]\nvs = VoltageSource(\n    id="source",\n    n=4,\n    ground=ground,\n    source_voltages=voltages,\n)\nload_bus = Bus(id="load bus", n=4)\nload = PowerLoad(id="power load", n=4, bus=load_bus, s=[100 + 0j, 100 + 0j, 100 + 0j])\nline_characteristics = LineCharacteristics(type_name="test", z_line=np.eye(4, dtype=complex))\nline = SimplifiedLine(\n    id="line",\n    n=4,\n    bus1=vs,\n    bus2=load_bus,\n    line_characteristics=line_characteristics,\n    length=10  # km\n)\np_ref = PotentialRef(element=ground)\n\nen = ElectricalNetwork(buses=[vs, load_bus], branches=[line], loads=[load], special_elements=[p_ref, ground])\n# or\n# en = ElectricalNetwork.from_element(vs)\n\nen.solve_load_flow(auth=("username", "password"))\n```\n\n<!-- Local Variables: -->\n<!-- mode: gfm -->\n<!-- coding: utf-8-unix -->\n<!-- ispell-local-dictionary: "british" -->\n<!-- End: -->\n',
    'author': 'Sébastien Vallet',
    'author_email': 'sebastien.vallet@roseautechnologies.com',
    'maintainer': 'Sébastien Vallet',
    'maintainer_email': 'sebastien.vallet@roseautechnologies.com',
    'url': 'https://github.com/RoseauTechnologies/Roseau_Load_Flow/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
