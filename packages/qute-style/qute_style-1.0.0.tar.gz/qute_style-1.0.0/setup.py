# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qute_style',
 'qute_style.dev',
 'qute_style.gen',
 'qute_style.widgets',
 'qute_style_examples']

package_data = \
{'': ['*'],
 'qute_style': ['resources/png_icons/*',
                'resources/svg_icons/*',
                'resources/svg_images/*',
                'ui/*'],
 'qute_style_examples': ['example_images/*',
                         'test_changelog/1.01/*',
                         'test_changelog/1.10/*',
                         'test_changelog/1.100/*']}

install_requires = \
['PySide6==6.4.2']

entry_points = \
{'console_scripts': ['qute-style-example = '
                     'qute_style_examples.main:main_method']}

setup_kwargs = {
    'name': 'qute-style',
    'version': '1.0.0',
    'description': 'QuteStyle is an expandable application framework for PySide6',
    'long_description': '<p align="center">\n  <a href="https://github.com/TUV-SUD-Product-Service-GmbH/QuteStyle">\n    <img src="https://github.com/TUV-SUD-Product-Service-GmbH/QuteStyle/raw/master/qute_style/resources/svg_images/banner_qute_style.svg" alt="QuteStyle logo" width="500" height="200">\n  </a>\n</p>\n\n# QuteStyle\n\nQuteStyle is an expandable application framework for PySide6 and heavily inspired by [PyDracula](https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6).\nThe main goal of this project is to provide a simple and easy to use application frame that can be used to create a new application.\nIt is mainly suited for applications that rely on a center widget for user interaction. Functionality is extendable by having different widgets that can be loaded into that center widget area.\n\n**Project status**\n\n[![Python Versions](https://img.shields.io/badge/Python-3.10%20|%203.11-blue.svg?&logo=Python&logoWidth=18&logoColor=white)](https://www.python.org/downloads/)\n[![Qt Versions](https://img.shields.io/badge/Qt-6-blue.svg?&logo=Qt&logoWidth=18&logoColor=white)](https://www.qt.io/qt-for-python)\n[![License](https://img.shields.io/github/license/TUV-SUD-Product-Service-GmbH/QuteStyle.svg)](https://github.com/TUV-SUD-Product-Service-GmbH/QuteStyle/blob/master/LICENSE)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/python/black)\n\n\n**Tests**\n\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/TUV-SUD-Product-Service-GmbH/QuteStyle/master.svg)](https://results.pre-commit.ci/latest/github/TUV-SUD-Product-Service-GmbH/QuteStyle/master)\n[![CodeQL](https://github.com/TUV-SUD-Product-Service-GmbH/QuteStyle/workflows/CodeQL/badge.svg)](https://github.com/TUV-SUD-Product-Service-GmbH/QuteStyle/actions?query=workflow%3ACodeQL)\n[![Build Status](https://github.com/TUV-SUD-Product-Service-GmbH/QuteStyle/workflows/Tests/badge.svg?branch=master&event=push)](https://github.com/TUV-SUD-Product-Service-GmbH/QuteStyle/actions?query=workflow%3ATests)\n[![Code Coverage](https://codecov.io/github/TUV-SUD-Product-Service-GmbH/QuteStyle/coverage.svg?branch=master&token=)](https://codecov.io/gh/TUV-SUD-Product-Service-GmbH/QuteStyle)\n\n\n**Package**\n\n[![PyPI](https://img.shields.io/pypi/v/qute_style)](https://pypi.org/project/qute-style/)\n[![PyPI - Wheel](https://img.shields.io/pypi/wheel/qute_style)](https://pypi.org/project/qute-style/#files)\n\n\n## Features\n\n- Easy integration of already existing widgets\n- Preset themes that easily can be modified\n- Custom widgets\n- Splash screen\n- Build-in release history\n- Used and developed in a productive environment\n\n## Themes and Styled Widgets\n\nQuteStyle provides five themes, defining the color composition of the app.\nAdditionally, the user can define new themes ([check this out](https://github.com/TUV-SUD-Product-Service-GmbH/QuteStyle/blob/master/docs/style.md)). We provide five themes, for example a dark and light mode ```Darcula``` and ```Highbridge Grey```.\nWe defined [custom widgets](https://github.com/TUV-SUD-Product-Service-GmbH/QuteStyle/blob/master/docs/widgets.md), such that they fit to the overall style and implemented new behaviour. A selection can be found in the Test-App:\n\n<img src="https://raw.githubusercontent.com/TUV-SUD-Product-Service-GmbH/QuteStyle/master/qute_style_examples/example_images/highbridge_grey.PNG" alt="Highbridge Grey" width="400" height="300"><img src="https://raw.githubusercontent.com/TUV-SUD-Product-Service-GmbH/QuteStyle/master/qute_style_examples/example_images/darcula.PNG" alt="Darcula" width="400" height="300">\n\n\n## Requirements\n\n- [Python 3.10+](https://www.python.org/downloads/)\n- [PySide6](https://wiki.qt.io/Qt_for_Python)\n\n## Installation Method\n\n   ```plaintext\n   pip install qute-style\n   ```\n\n## Usage\n\n```Python\nimport sys\n\nfrom qute_style_examples.sample_main_window import StyledMainWindow\nfrom qute_style.qs_application import QuteStyleApplication\nfrom qute_style.update_window import AppData\n\nclass MyApplication(QuteStyleApplication):\n    # take a look at qute_style_examples.sample_main_window and qute_style_examples.sample_widgets\n    # to find out more about setting up a main window and the widgets that it\n    # should display\n    MAIN_WINDOW_CLASS = StyledMainWindow\n    # add basic information about your application\n    APP_DATA = AppData(\n        "Test-App",\n        "2.3.4",\n        ":/svg_images/logo_qute_style.svg",\n        ":/svg_images/logo_qute_style.svg",\n        "",\n        "Test Version",\n    )\n\nif __name__ == "__main__":\n\n    APP_NAME = "Test-App"\n\n    app = MyApplication(sys.argv)\n    sys.exit(app.exec())\n```\n\nFor further information, see our [documentation](https://github.com/TUV-SUD-Product-Service-GmbH/QuteStyle/tree/master/docs).\n\n## Example\n\nCheck out our example app by running:\n\n```plaintext\npython -m qute_style_examples\n```\n\n## License\n\nThe original design idea is from [Wanderson-Magalhaes](https://github.com/Wanderson-Magalhaes) and his project [PyDracula](https://github.com/Wanderson-Magalhaes/Modern_GUI_PyDracula_PySide6_or_PyQt6) (MIT License).\nThe svg files are derived from [Material design icons](https://fonts.google.com/icons) (Apache License Version 2.0). Other files are covered by QuteStyle\'s MIT license.\n\n## Contributing\n\nAll contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.\n',
    'author': 'Marina Baumgartner, Dairen Gonschior, Tilman Krummeck, Dennis Spitzhorn, Gerhard Trapp, Patrick Zwerschke',
    'author_email': 'PS-TF-Entwicklung@tuev-sued.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/TUV-SUD-Product-Service-GmbH/QuteStyle',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
