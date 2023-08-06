# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['geoapps',
 'geoapps.base',
 'geoapps.block_model_creation',
 'geoapps.calculator',
 'geoapps.clustering',
 'geoapps.contours',
 'geoapps.coordinate_transformation',
 'geoapps.driver_base',
 'geoapps.edge_detection',
 'geoapps.export',
 'geoapps.interpolation',
 'geoapps.inversion',
 'geoapps.inversion.airborne_electromagnetics',
 'geoapps.inversion.components',
 'geoapps.inversion.components.factories',
 'geoapps.inversion.electricals',
 'geoapps.inversion.electricals.direct_current',
 'geoapps.inversion.electricals.direct_current.three_dimensions',
 'geoapps.inversion.electricals.direct_current.two_dimensions',
 'geoapps.inversion.electricals.induced_polarization',
 'geoapps.inversion.electricals.induced_polarization.three_dimensions',
 'geoapps.inversion.electricals.induced_polarization.two_dimensions',
 'geoapps.inversion.natural_sources',
 'geoapps.inversion.natural_sources.magnetotellurics',
 'geoapps.inversion.natural_sources.tipper',
 'geoapps.inversion.potential_fields',
 'geoapps.inversion.potential_fields.gravity',
 'geoapps.inversion.potential_fields.magnetic_scalar',
 'geoapps.inversion.potential_fields.magnetic_vector',
 'geoapps.iso_surfaces',
 'geoapps.octree_creation',
 'geoapps.peak_finder',
 'geoapps.scatter_plot',
 'geoapps.shared_utils',
 'geoapps.triangulated_surfaces',
 'geoapps.utils']

package_data = \
{'': ['*'], 'geoapps': ['images/*']}

install_requires = \
['dask[distributed]==2022.10.0',
 'discretize>=0.7.4,<0.8.0',
 'distributed==2022.10.0',
 'empymod>=2.1.3,<3.0.0',
 'fsspec>=2022.0.0,<2023.0.0',
 'geoana>=0.0.6,<0.1.0',
 'geoh5py==0.5.0',
 'h5py>=3.2.1,<4.0.0',
 'matplotlib>=3.5.1,<4.0.0',
 'mira-simpeg==0.15.1dev7',
 'mkl>=2022.0.0,<2023.0.0',
 'numpy>=1.21.5,<2.0.0',
 'pandas>=1.3.5,<2.0.0',
 'param-sweeps==0.1.3',
 'properties>=0.6.1,<0.7.0',
 'pydiso>=0.0.3,<0.1.0',
 'pymatsolver>=0.2.0,<0.3.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'scipy>=1.7.3,<2.0.0',
 'simpeg_archive==0.9.1.dev5',
 'tqdm>=4.64.0,<5.0.0',
 'utm>=0.7.0,<0.8.0',
 'zarr>=2.8.1,<3.0.0']

extras_require = \
{'full': ['fiona>=1.8.21,<2.0.0',
          'gdal>=3.5.1,<4.0.0',
          'ipyfilechooser>=0.6.0,<0.7.0',
          'ipywidgets>=7.6.5,<8.0.0',
          'plotly>=5.8.0,<6.0.0',
          'scikit-image>=0.19.2,<0.20.0',
          'jupyter-dash>=0.4.2,<0.5.0',
          'dash-daq>=0.5.0,<0.6.0']}

setup_kwargs = {
    'name': 'geoapps',
    'version': '0.9.2',
    'description': 'Open-sourced Applications in Geoscience',
    'long_description': 'Welcome to **geoapps** - Open-source applications in geosciences\n================================================================\n\n<img align="right" width="50%" src="https://github.com/MiraGeoscience/geoapps/raw/develop/docs/images/index_page.png">\n\nIn short\n--------\n\nThe **geoapps** project has been created by [Mira Geoscience](https://mirageoscience.com/) for the development and sharing of open-source\napplications in geoscience. Users will be able to directly leverage\nthe powerful visualization capabilities of [Geoscience ANALYST](https://mirageoscience.com/mining-industry-software/geoscience-analyst/)\nalong with open-source code from the Python ecosystem.\n\nLinks\n-----\n\n- [Download the latest](https://github.com/MiraGeoscience/geoapps/archive/main.zip)\n- [Getting started](https://geoapps.readthedocs.io/en/latest/content/installation.html#installation)\n- [Documentation](https://geoapps.readthedocs.io/en/latest/index.html)\n- [Available on PyPI](https://pypi.org/project/geoapps/)\n\n  ```pip install geoapps```\n\n\nCurrent sponsors:\n-----------------\n\n- [Anglo American](http://www.angloamerican.ca/)\n- [Barrick](https://www.barrick.com/English/home/default.aspx)\n- [BHP](https://www.bhp.com/)\n- [Cameco](https://www.cameco.com/)\n- [Glencore](https://www.glencore.com/)\n- [Mira Geoscience](https://mirageoscience.com/)\n- [Rio Tinto](https://www.riotinto.com/en)\n- [Teck](https://www.teck.com/)\n- [Vale](http://www.vale.com/canada/EN/Pages/default.aspx)\n\nLicense\n-------\n\n**geoapps** is distributed under the terms and conditions of the [MIT License](LICENSE).\n\n\n*Copyright (c) 2023 Mira Geoscience Ltd.*\n',
    'author': 'Mira Geoscience',
    'author_email': 'dominiquef@mirageoscience.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://mirageoscience.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
