# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['studatio']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.4,<2.0.0',
 'click>=8.1.3,<9.0.0',
 'icalevents>=0.1.27,<0.2.0',
 'pyperclip>=1.8.2,<2.0.0',
 'tomlkit>=0.11.4,<0.12.0']

entry_points = \
{'console_scripts': ['studatio = studatio.main:main']}

setup_kwargs = {
    'name': 'studatio',
    'version': '1.3.2',
    'description': 'Personal tool for my violin teaching database',
    'long_description': "# studatio\n\n![PyPI](https://img.shields.io/pypi/v/studatio)\n\n`studatio` is a Python tool for private music teachers to manage their studio's data.\n\nI am primarily developing this for my own use as a violin teacher. However, I hope for the project to become useful to\nother teachers. Currently, studatio pulls and formats Apple iCal data about music lessons for use in lesson schedules or\nfacility reservations.\n\nI hope to add support for automated facility reservations, expanded business statistics, billing, and note-taking.\n\n## Installation\n\nFirst, [install Python](https://www.python.org/downloads/) if it is not already installed. Use the package\nmanager [pip](https://pip.pypa.io/en/stable/) to\ninstall studatio.\n\n```bash\npip install studatio\n```\n\nOn first use, studatio will prompt you for a URL containing iCal data of your studio's calendar.\n\n## Usage\n\n```\nUsage: studatio schedule [OPTIONS]\n\n  Prints and copies to clipboard a formatted list of\n  studio events.\n\nOptions:\n  -m, --month TEXT    Integer, or range of ints\n                      separated by a hyphen,\n                      representing a month/s of the\n                      year. Defaults to current\n                      month.\n  -y, --year INTEGER  Defaults to current year.\n```\n\n```\nUsage: studatio elapsed [OPTIONS]\n\n  Prints the time elapsed of events in the given\n  period\n\nOptions:\n  -m, --month TEXT    Integer, or range of ints\n                      separated by a hyphen,\n                      representing a month/s of the\n                      year. Defaults to current\n                      month.\n  -y, --year INTEGER  Defaults to current year.\n```\n\nExamples:\n\n```\n% studatio schedule --month 1 --year 2022\nJan 01 2022 Violin Lesson 10:45 AM to 11:45 AM\nJan 07 2022 Violin/Viola Lessons 04:30 PM to 06:15 PM\nJan 08 2022 Violin Lesson 12:30 PM to 01:30 PM\nJan 18 2022 Violin Lesson 06:05 PM to 06:35 PM\nJan 21 2022 Violin Lessons 03:30 PM to 05:30 PM\nJan 28 2022 Viola Lesson 05:30 PM to 06:15 PM\n```\n\n`studatio schedule -m 10-12`\n\n`% studatio elapsed --month 10 --year 2022\n22 Hours, 0 Minutes Elapsed`\n\n## Contributing\n\nTo build, you must install [poetry](https://python-poetry.org/) and [pre-commit](https://pre-commit.com/). Pull requests\nare welcome. Documentation and test changes are just as\nwelcome as changes to source code.\n\nI am an amateur programmer, but I always want to learn, so if there are things that work but are not best practices, I\nwould be eager to hear them.\n\n## License\n[MIT](https://choosealicense.com/licenses/mit/)\n",
    'author': 'Eliza Wilson',
    'author_email': 'elizaaverywilson@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/elizaaverywilson/studatio',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
