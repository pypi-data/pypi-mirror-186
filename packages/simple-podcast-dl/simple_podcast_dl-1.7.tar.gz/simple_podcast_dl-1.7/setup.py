# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['podcast_dl']

package_data = \
{'': ['*']}

install_requires = \
['aiodns>=1.1,<2.0',
 'attrs>=18.2,<19.0',
 'click>=7.0,<8.0',
 'httpx>=0.18.2,<0.19.0',
 'lxml>=4.2,<5.0',
 'python-slugify>=1.2,<2.0']

entry_points = \
{'console_scripts': ['podcast-dl = podcast_dl.cli:main']}

setup_kwargs = {
    'name': 'simple-podcast-dl',
    'version': '1.7',
    'description': 'Simple podcast downloader (podcatcher)',
    'long_description': '# Simple podcast downloader (podcatcher)\n\nThe simplest podcast downloader with no configuration, no tagging, no nothing.  \nIt simply downloads missing episodes from supported podcasts to a directory.  \n_That\'s it._\n\nYou don\'t even have to know the URL of the RSS, you can give it a website URL,  \na domain name, or simply the podcast name, it will find out which podcast you want to download.\n\nIt doesn\'t have a complicated UI or fancy features, it\'s just a command line application.  \nThe download folder and the number of threads can be customized.\n\nI use it in a Jenkins job to synchronize all the episodes to [Nextcloud](https://nextcloud.com/),  \nso it will be synced to my phone and I can listen the episodes without internet connection.\n\n## Supported podcasts\n\n- Talk Python To Me (https://talkpython.fm/)\n- Python Bytes (https://pythonbytes.fm/)\n- The Changelog (https://changelog.com/podcast)\n- Podcast.\\_\\_init\\_\\_ (https://www.podcastinit.com/)\n- Indie Hackers (https://www.indiehackers.com/podcast)\n- Real Python (https://realpython.com/podcasts/rpp/)\n- Kubernetes Podcast (https://kubernetespodcast.com/)\n\n## Installation\n\nYou need at least Python 3.6, then you can simply run:\n\n```\n$ pip3 install simple-podcast-dl\n```\n\n## Getting started\n\nIt is as simple as running the command:\n\n```\n$ podcast-dl talkpython.fm\n```\n\nAnd the podcast will be downloaded to the "talkpython.fm" directory.  \nYou can change the download directory by specifying the `--directory`\n(or `-d`) option:\n\n```\n$ podcast-dl talkpython.fm -d talkpython-podcast\n```\n\nYou can list the supported podcast sites with the `--list-podcasts`\n(or `-l`) option:\n\n```\n$ podcast-dl --list-podcasts\n```\n\nYou can specify which episodes to download with the `--episodes`\n(or `-e`) option:\n\n```\n$ podcast-dl --episodes 1,2,3 talkpython\n```\n\nYou can use the "last" or "last:n" keyword to select the last or last n number\nof episodes to download:\n\n```\n$ podcast-dl --episodes last:3 talkpython\n```\n\nYou can list the podcast episodes sorted by episode number with\n`--show-episodes` or (`-s`):\n\n```\n$ podcast-dl --show-episodes talkpython\n```\n\nOr you can even combine it with selecting episodes:\n\n```\n$ podcast-dl --show-episodes -e 1-5 talkpython\n```\n\nIt can show a progress bar with the `--progress` or (`-p`) option:\n\n```\n$ podcast-dl -p talkpython\nFound a total of 182 missing episodes.\n  [##########--------------------------]   28%  00:03:16\n```\n\n## Usage\n\n```plain\nUsage: podcast-dl [OPTIONS] PODCAST\n\n  Download podcast episodes to the given directory\n\n  URL or domain or short name for the PODCAST argument can be specified,\n  e.g. pythonbytes.fm or talkpython or https://talkpython.fm\n\nOptions:\n  -d, --download-dir PATH         Where to save downloaded episodes. Can be\n                                  specified by the DOWNLOAD_DIR environment\n                                  variable.  [default: name of PODCAST]\n  -e, --episodes EPISODELIST      Episodes to download.\n  -s, --show-episodes             Show the list of episodes for PODCAST.\n  -l, --list-podcasts             List of supported podcasts, ordered by name.\n  -p, --progress                  Show progress bar instead of detailed\n                                  messages during download.\n  -t, --max-threads INTEGER RANGE\n                                  The maximum number of simultaneous\n                                  downloads. Can be specified with the\n                                  MAX_THREADS environment variable.  [default:\n                                  10]\n  -v, --verbose                   Show detailed informations during download.\n  -V, --version                   Show the version and exit.\n  -h, --help                      Show this message and exit.\n```\n\n## Development\n\nThe project has a `pyproject.toml`, so you can simply install everything needed for development with a single command:\n\n```\n$ pip install pipenv\n$ poetry install\n```\n\nYou should format your code with black (it\'s included in the development requirements):\n\n```\n$ poetry run black .\n```\n\nYou can run the tests with:\n\n```\n$ poetry run pytest\n```\n',
    'author': 'Kiss György',
    'author_email': 'kissgyorgy@me.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kissgyorgy/simple-podcast-dl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
