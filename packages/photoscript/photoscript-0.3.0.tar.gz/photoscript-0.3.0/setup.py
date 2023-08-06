# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['photoscript']

package_data = \
{'': ['*']}

install_requires = \
['py-applescript>=1.0.3,<2.0.0',
 'pyobjc-core>=9.0,<10.0',
 'pyobjc-framework-AppleScriptKit>=9.0,<10.0',
 'pyobjc-framework-AppleScriptObjC>=9.0,<10.0',
 'pyobjc-framework-Cocoa>=9.0,<10.0']

setup_kwargs = {
    'name': 'photoscript',
    'version': '0.3.0',
    'description': 'Python wrapper around Apple Photos applescript interface',
    'long_description': '# PhotoScript\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)\n[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)\n<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->\n[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat)](#contributors-)\n<!-- ALL-CONTRIBUTORS-BADGE:END -->\n\n\n## What is PhotoScript\n\nPhotoScript provides a python wrapper around Apple Photos applescript interface.  With PhotoScript you can interact with Photos using python.  Runs only on MacOS.  Tested on MacOS Catalina.\n\nPhotosScript is limited by Photos\' very limited AppleScript dictionary. \n\n## Compatibility\nDesigned for MacOS Catalina/Photos 5.  Preliminary testing on Big Sur/Photos 6 beta shows this should work on Big Sur as well.  Photos\' AppleScript interface has changed very little since Photos 2 (the earliest version I have access to).  This package should work with most versions of Photos but some methods may not function correctly on versions earlier than Photos 5.  If you find compatibility issues, open an issue or send a PR.\n\n## Installation\n\nPhotoScript uses [poetry](https://python-poetry.org/) for dependency management.  To install, clone the repo and run `poetry install`. If you don\'t have poetry already installed, follow the [installation instructions](https://python-poetry.org/docs/#installation). To enter the virtual environment, run `poetry shell`.\n\nOr you can install via pip:\n\n`python3 -m pip install photoscript`\n\n## Example\n\n```python\n""" Simple example showing use of photoscript """\n\nimport photoscript\n\nphotoslib = photoscript.PhotosLibrary()\n\nphotoslib.activate()\nprint(f"Running Photos version: {photoslib.version}")\n\nalbum = photoslib.album("Album1")\nphotos = album.photos()\n\nfor photo in photos:\n    photo.keywords = ["travel", "vacation"]\n    print(f"{photo.title}, {photo.description}, {photo.keywords}")\n\nnew_album = photoslib.create_album("New Album")\nphotoslib.import_photos(["/Users/rhet/Downloads/test.jpeg"], album=new_album)\n\nphotoslib.quit()\n```\n## Documentation\nFull documentation [here](https://rhettbull.github.io/PhotoScript/).\n\nAdditional documentation about Photos and AppleScript available on the [wiki](https://github.com/RhetTbull/PhotoScript/wiki/Welcome-to-the-PhotoScript-Wiki).\n\n## Testing\nTested on MacOS Catalina, Photos 5 with 100% coverage. \n\n## Limitations\nPhotos\' AppleScript interface is very limited.  For example, it cannot access information on faces in photos nor can it delete a photo.  PhotoScript is thus limited.  PhotoScript works by executing AppleScript through an Objective-C bridge from python.  Every method call has to do a python->Objective C->AppleScript round trip; this makes the interface much slower than native python code.  This is particularly noticeable when dealing with Folders which requires significant work arounds.\n\nWhere possible, PhotoScript attempts to provide work-arounds to Photos\' limitations. For example, Photos does not provide a way to remove a photo from an album.  PhotoScript does provide a `Album.remove()` method but in order to do this, it creates a new album with the same name as the original, copies all but the removed photos to the new album then deletes the original album.  This simulates removing photos and produces the desired effect but is not the same thing as removing a photo from an album.\n\n## Related Projects\n- [osxphotos](https://github.com/RhetTbull/osxphotos): Python package that provides read-only access to the Photos library including all associated metadata. \n\n## Dependencies\n- [py-applescript](https://github.com/rdhyee/py-applescript)\n- [PyObjC](https://github.com/ronaldoussoren/pyobjc)\n\n## Contributors ✨\n\nThanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):\n\n<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->\n<!-- prettier-ignore-start -->\n<!-- markdownlint-disable -->\n<table>\n  <tr>\n    <td align="center"><a href="http://davidhaberthür.ch"><img src="https://avatars.githubusercontent.com/u/1651235?v=4?s=100" width="100px;" alt=""/><br /><sub><b>David Haberthür</b></sub></a><br /><a href="https://github.com/RhetTbull/PhotoScript/commits?author=habi" title="Documentation">📖</a></td>\n  </tr>\n</table>\n\n<!-- markdownlint-restore -->\n<!-- prettier-ignore-end -->\n\n<!-- ALL-CONTRIBUTORS-LIST:END -->\n\nThis project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!',
    'author': 'Rhet Turnbull',
    'author_email': 'rturnbull+git@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/RhetTbull/photoscript',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
