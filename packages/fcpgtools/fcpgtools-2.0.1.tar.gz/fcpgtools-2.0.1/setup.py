# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['fcpgtools', 'fcpgtools.terrainengine']

package_data = \
{'': ['*']}

install_requires = \
['descartes>=1.1.0,<2.0.0',
 'geopandas>=0.12.2,<0.13.0',
 'pysheds>=0.3.3,<0.4.0',
 'rasterio>=1.3.4,<2.0.0',
 'rioxarray>=0.13.3,<0.14.0',
 'xarray>=2023.1.0,<2024.0.0']

setup_kwargs = {
    'name': 'fcpgtools',
    'version': '2.0.1',
    'description': 'Tools to create Flow-Conditioned Parameter Grids (FCPGs) from Flow Direction Rasters (FDRs) and arbitrary rasterized parameter data.',
    'long_description': 'Flow-Conditioned Parameter Grid (FCPG) Tools Documentation\n===============================================================\n\n\n**For detailed documentation please reference our [ReadTheDocs site](https://usgs.github.io/water-fcpg-tools/)!** \n\nPlease log any issues or feature requests using [this form](https://code.usgs.gov/StreamStats/data-preparation/cpg/FCPGtools/-/issues/new?issuable_template=bug).\n\n# Getting Started\n## Installation\n`FCPGtools` can be installed from [`PyPI`](https://pypi.org/project/fcpgtools/) into a virtual environment containing [`GDAL`](https://anaconda.org/conda-forge/gdal), and for full functionality, [`TauDEM`](https://anaconda.org/conda-forge/taudem) as well.\n\n**We strongly encourage the following installation workflow:**\n\n1. Install the Anaconda Python Distribution or Miniconda\n    * [Anaconda Individual Edition](https://www.anaconda.com/products/distribution) - includes `conda`, a complete Python (and R) data science stack, and the helpful Anaconda Navigator GUI.\n    * A lighter-weight alternative is to [install Miniconda](https://docs.conda.io/en/latest/miniconda.html).\n2. Use the `conda` command line to clone our lightweight `fcpgtools_base` virtual environment that contains non-Python dependencies from the [`environment.yml`](https://code.usgs.gov/StreamStats/data-preparation/cpg/FCPGtools/-/blob/master/environment.yml) file available in our repo. Either clone the repo, or just download the .yml file locally, and run the following commands:\n\n    ```\n    conda env create -f {PATH}/environment.yml\n    ```\n    * **Note:** We also provide a more robust [`environment_dev.yml`](https://code.usgs.gov/StreamStats/data-preparation/cpg/FCPGtools/-/blob/master/environment_dev.yml) virtual environment for developers containing all libraries relevant to making contributions as well as running our [example notebooks](https://code.usgs.gov/StreamStats/data-preparation/cpg/FCPGtools/-/blob/master/examples).\n3. Activate the `fcpgtools_base` environment, and pip install `fcpgtools`.\n    ```\n    pip install fcpgtools\n    ```\n\n\n\n## Using FCPGtools\nVersion 2.0 of `FCPGtools` has a "flat" architecture, meaning all functions can be accessed by importing the main `fcpgtools` module as shown in a simple example below:\n\n```python\n# creating an flow accumulation raster from a Flow Direction Raster (FDR)\nimport fcpgtools\n\npath_to_fdr = r\'YOUR/PATH/HERE/fdr.tif\'\n\nflow_accumulation_grid = fcpgtools.accumulate_flow(\n    d8_fdr=path_to_fdr,\n) -> xarray.DataArray\n```\n\nPlease refer to our documentation\'s [Cookbook](https://usgs.github.io/water-fcpg-tools/cookbook.html) page for more intricate examples of usage.\n\n# Citation\n* **Version 2.0** was released in January, 2023.\n    * Barnhart, T.B., Nogueira, X.R., Siefken, S.A., Schultz, A.R., Aufenkampe, A., Tomasula, P., 2023, Flow-Conditioned Parameter Grid Tools Version 2.0.\n* **Version 1.1** was released in September, 2022.\n* **Version 1.0** (IP-112996) was approved on September 3, 2020.\n    * Barnhart, T.B., Sando, R., Siefken, S.A., McCarthy, P.M., and Rea, A.H., 2020, Flow-Conditioned Parameter Grid Tools: U.S. Geological Survey Software Release, DOI: https://doi.org/10.5066/P9W8UZ47.\n\n# Migrating from Version 1.0\nVersion 2.0 of `FCPGtools` is a ground-up refactor and rebuild of Version 1.0. Backwards compatibility is broken, and many work-flows have been significantly streamlined. We strongly suggest that any users accustomed to Version 1.0 reference our [updated documentation site](https://usgs.github.io/water-fcpg-tools/index.html).\n\n**A non-exhaustive list of key updates is below:**\n* All functions output an in-memory [`xarray.DataArray`](https://docs.xarray.dev/en/stable/generated/xarray.DataArray.html#xarray.DataArray) object, allowing for functions to be strung together into performance oriented pipelines.\n    * [`xarray.DataArray`](https://docs.xarray.dev/en/stable/generated/xarray.DataArray.html#xarray.DataArray) objects have a variety of powerful features and optimizations. For more information please reference the library\'s [documentation](https://docs.xarray.dev/en/stable/getting-started-guide/why-xarray.html).\n    * Rasters can still be saved to a local GeoTIFF file by providing a valid `.tif` path to `param:out_path`.\n* All functions can now accept either local string paths, local [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html) objects, or in-memory [`xarray.DataArray`](https://docs.xarray.dev/en/stable/generated/xarray.DataArray.html#xarray.DataArray) objects.\n* Multi-band parameter grids are now supported!\n    * Example: Passing a 12-month precipitation raster (where each month is a raster band) into [`fcpgtools.accumulate_parameter()`](https://usgs.github.io/water-fcpg-tools/functions.html#fcpgtools.tools.accumulate_parameter) will output a 12-band [`xarray.DataArray`](https://docs.xarray.dev/en/stable/generated/xarray.DataArray.html#xarray.DataArray) object.\n* Flow Direction Raster format conversion (i.e. ESRI -> TauDEM) is now automated behind-the-scenes.\n* Support for multiple "terrain engines" gives users optionality and increases dependency deprecation resiliancy. \n    * Where necessary users can set `param:engine` to [`taudem`](https://hydrology.usu.edu/taudem/taudem5/) (default) or [`pysheds`](https://github.com/mdbartos/pysheds).\n    * Note that the `pysheds` terrain engine is signifcantly more performant, however it currently only supports [`accumulate_flow()`](https://usgs.github.io/water-fcpg-tools/functions.html#fcpgtools.tools.accumulate_flow) and [`accumulate_parameter()`](https://usgs.github.io/water-fcpg-tools/functions.html#fcpgtools.tools.accumulate_parameter).\n\n**Please reference our markdown [`refactored_names`](examples/refactored_names.md) document for a complete mapping of Version 1.1 to Version 2.0 function names.**\n\n\n## Disclaimers\nAny use of trade, firm, or product names is for descriptive purposes only and does not imply endorsement by the U.S. Government.\n\nPlease see [DISCLAIMER.md](DISCLAIMER.md) in the project repository.\n\n## License\nPlease see [LICENSE.md](LICENSE.md) in the project repository.\n',
    'author': 'Theodore Barnhart',
    'author_email': 'tbarnhart@usgs.gov',
    'maintainer': 'Xavier R Nogueira',
    'maintainer_email': 'xrnogueira@limno.com',
    'url': 'https://usgs.github.io/water-fcpg-tools/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
