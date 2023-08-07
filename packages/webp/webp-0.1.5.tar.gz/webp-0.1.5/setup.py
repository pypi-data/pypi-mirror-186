# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['webp', 'webp_build']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=4.0.0', 'cffi>=1.0.0', 'numpy>=1.0.0']

setup_kwargs = {
    'name': 'webp',
    'version': '0.1.5',
    'description': 'Python bindings for WebP',
    'long_description': '# WebP Python bindings\n\n[![Build status](https://img.shields.io/endpoint.svg?url=https%3A%2F%2Factions-badge.atrox.dev%2Fanibali%2Fpywebp%2Fbadge&label=build&logo=none)](https://actions-badge.atrox.dev/anibali/pywebp/goto)\n[![License](https://img.shields.io/github/license/anibali/pywebp.svg)](https://github.com/anibali/pywebp/blob/master/LICENSE)\n[![PyPI](https://img.shields.io/pypi/v/webp)](https://pypi.org/project/webp/)\n[![GitHub](https://img.shields.io/github/stars/anibali/pywebp?style=social)](https://github.com/anibali/pywebp)\n\n## Installation\n\n```sh\npip install webp\n```\n\nOn Windows you may encounter the following error during installation:\n\n```\nconans.errors.ConanException: \'settings.compiler\' value not defined\n```\n\nThis means that you need to install a C compiler and configure Conan so that it knows which\ncompiler to use. See https://github.com/anibali/pywebp/issues/20 for more details.\n\n### Requirements\n\n* Python 3.7+\n\n## Usage\n\n```python\nimport webp\n```\n\n### Simple API\n\n```python\n# Save an image\nwebp.save_image(img, \'image.webp\', quality=80)\n\n# Load an image\nimg = webp.load_image(\'image.webp\', \'RGBA\')\n\n# Save an animation\nwebp.save_images(imgs, \'anim.webp\', fps=10, lossless=True)\n\n# Load an animation\nimgs = webp.load_images(\'anim.webp\', \'RGB\', fps=10)\n```\n\nIf you prefer working with numpy arrays, use the functions `imwrite`, `imread`, `mimwrite`,\nand `mimread` instead.\n\n### Advanced API\n\n```python\n# Encode a PIL image to WebP in memory, with encoder hints\npic = webp.WebPPicture.from_pil(img)\nconfig = WebPConfig.new(preset=webp.WebPPreset.PHOTO, quality=70)\nbuf = pic.encode(config).buffer()\n\n# Read a WebP file and decode to a BGR numpy array\nwith open(\'image.webp\', \'rb\') as f:\n  webp_data = webp.WebPData.from_buffer(f.read())\n  arr = webp_data.decode(color_mode=WebPColorMode.BGR)\n\n# Save an animation\nenc = webp.WebPAnimEncoder.new(width, height)\ntimestamp_ms = 0\nfor img in imgs:\n  pic = webp.WebPPicture.from_pil(img)\n  enc.encode_frame(pic, timestamp_ms)\n  timestamp_ms += 250\nanim_data = enc.assemble(timestamp_ms)\nwith open(\'anim.webp\', \'wb\') as f:\n  f.write(anim_data.buffer())\n\n# Load an animation\nwith open(\'anim.webp\', \'rb\') as f:\n  webp_data = webp.WebPData.from_buffer(f.read())\n  dec = webp.WebPAnimDecoder.new(webp_data)\n  for arr, timestamp_ms in dec.frames():\n    # `arr` contains decoded pixels for the frame\n    # `timestamp_ms` contains the _end_ time of the frame\n    pass\n```\n\n## Features\n\n* Picture encoding/decoding\n* Animation encoding/decoding\n* Automatic memory management\n* Simple API for working with `PIL.Image` objects\n\n### Not implemented\n\n* Encoding/decoding still images in YUV color mode\n* Advanced muxing/demuxing (color profiles, etc.)\n* Expose all useful fields\n\n## Developer notes\n\n### Setting up\n\n1. Install `mamba` and `conda-lock`. The easiest way to do this is by installing\n   [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge) and then\n   running `mamba install conda-lock`. \n2. Create and activate the Conda environment:\n   ```console\n   $ conda-lock install -n webp\n   $ mamba activate webp\n   ```\n3. Install PyPI dependencies:\n   ```console\n   $ poetry install\n   ```\n\n### Running tests\n\n```console\n$ pytest tests/\n```\n\n### Cutting a new release\n\n1. Ensure that tests are passing and everything is ready for release.\n2. Create and push a Git tag:\n   ```console\n   $ git tag -a v0.1.5\n   $ git push --tags\n   ```\n3. Download the artifacts from GitHub Actions, which will include the source distribution tarball and binary wheels.\n4. Create a new release on GitHub from the tagged commit and upload the packages as attachments to the release.\n5. Also upload the packages to PyPI using Twine:\n   ```console\n   $ twine upload webp-*.tar.gz webp-*.whl\n   ```\n6. Bump the version number in `pyproject.toml` and create a commit, signalling the start of development on the next version.\n\nThese files should also be added to a GitHub release.\n\n## Known issues\n\n* An animation where all frames are identical will "collapse" in on itself,\n  resulting in a single frame. Unfortunately, WebP seems to discard timestamp\n  information in this case, which breaks `webp.load_images` when the FPS\n  is specified.\n* There are currently no 32-bit binaries of libwebp uploaded to Conan Center. If you are running\n  32-bit Python, libwebp will be built from source.\n',
    'author': 'Aiden Nibali',
    'author_email': 'dismaldenizen@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/anibali/pywebp',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
