# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fractal_tasks_core', 'fractal_tasks_core.tools']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.1.1,<10.0.0',
 'PyQt5',
 'anndata>=0.8.0,<0.9.0',
 'cellpose>=2.2,<2.3',
 'dask>=2023.1.0,<2023.2.0',
 'defusedxml>=0.7.1,<0.8.0',
 'imageio-ffmpeg>=0.4.7,<0.5.0',
 'llvmlite>=0.39.1,<0.40.0',
 'lxml>=4.9.1,<5.0.0',
 'napari-segment-blobs-and-things-with-membranes>=0.3.3,<0.4.0',
 'napari-skimage-regionprops>=0.5.3,<0.6.0',
 'napari-workflows>=0.2.8,<0.3.0',
 'napari==0.4.16',
 'numpy>=1.23.5,<1.24.0',
 'pandas>=1.2.0,<2.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'scikit-image>=0.19.3,<0.20.0',
 'torch==1.12.1',
 'zarr>=2.13.6,<2.14.0']

extras_require = \
{'tools': ['matplotlib']}

setup_kwargs = {
    'name': 'fractal-tasks-core',
    'version': '0.7.0',
    'description': '',
    'long_description': '# Fractal Core Tasks\n\n[![PyPI version](https://img.shields.io/pypi/v/fractal-tasks-core?color=gree)](https://pypi.org/project/fractal-tasks-core/)\n[![CI Status](https://github.com/fractal-analytics-platform/fractal-tasks-core/actions/workflows/ci.yml/badge.svg)](https://github.com/fractal-analytics-platform/fractal-tasks-core/actions/workflows/ci.yml)\n[![Documentation Status](https://github.com/fractal-analytics-platform/fractal-tasks-core/actions/workflows/documentation.yaml/badge.svg)](https://fractal-analytics-platform.github.io/fractal-tasks-core)\n[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)\n\nFractal is a framework to process high-content imaging data at scale and prepare it for interactive visualization.\n\n![Fractal_Overview](https://fractal-analytics-platform.github.io/assets/fractal_overview.jpg)\n\nFractal provides distributed workflows that convert TBs of image data into OME-Zarr files. The platform then processes the 3D image data by applying tasks like illumination correction, maximum intensity projection, 3D segmentation using [cellpose](https://cellpose.readthedocs.io/en/latest/) and measurements using [napari workflows](https://github.com/haesleinhuepf/napari-workflows). The pyramidal OME-Zarr files enable interactive visualization in the napari viewer.\n\nThis is the **core-tasks repository**, containing the python tasks that parse Yokogawa CV7000 images into OME-Zarr and process OME-Zarr files. Find more information about Fractal in general and the other repositories at the [Fractal home page](https://fractal-analytics-platform.github.io).\n\n## Documentation\n\nSee https://fractal-analytics-platform.github.io/fractal-tasks-core\n\n\n## Available tasks\n\nCurrently, the following tasks are available:\n- Create Zarr Structure: Task to generate the zarr structure based on Yokogawa metadata files\n- Yokogawa to Zarr: Parses the Yokogawa CV7000 image data and saves it to the Zarr file\n- Illumination Correction: Applies an illumination correction based on a flatfield image & subtracts a background from the image.\n- Image Labeling (& Image Labeling Whole Well): Applies a cellpose network to the image of a single ROI or the whole well. cellpose parameters can be tuned for optimal performance.\n- Maximum Intensity Projection: Creates a maximum intensity projection of the whole plate.\n- Measurement: Make some standard measurements (intensity & morphology) using napari workflows, saving results to AnnData tables.\n\nSome additional tasks are currently being worked on and some older tasks are still present in the fractal_tasks_core folder.\n\n# Contributors and license\n\nUnless otherwise stated in each individual module, all Fractal components are released according to a BSD 3-Clause License, and Copyright is with Friedrich Miescher Institute for Biomedical Research and University of Zurich.\n\nFractal was conceived in the Liberali Lab at the Friedrich Miescher Institute for Biomedical Research and in the Pelkmans Lab at the University of Zurich (both in Switzerland). The project lead is with [@gusqgm](https://github.com/gusqgm) & [@jluethi](https://github.com/jluethi). The core development is done under contract by [@mfranzon](https://github.com/mfranzon), [@tcompa](https://github.com/tcompa) & [@jacopo-exact](https://github.com/jacopo-exact) from [eXact lab S.r.l.](exact-lab.it).\n',
    'author': 'Jacopo Nespolo',
    'author_email': 'jacopo.nespolo@exact-lab.it',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/fractal-analytics-platform/fractal-tasks-core',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
