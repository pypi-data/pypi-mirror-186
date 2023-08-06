# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['newspy', 'newspy.newsapi', 'newspy.rss', 'newspy.shared']

package_data = \
{'': ['*']}

install_requires = \
['feedparser==6.0.10',
 'python-slugify==6.1.2',
 'requests==2.28.1',
 'urllib3==1.26.12']

setup_kwargs = {
    'name': 'newspy',
    'version': '1.1.1',
    'description': 'The news client written in Python that fetches and curates the world news across the web.',
    'long_description': "# Newspy\n\nThe news client written in Python that fetches and curates the world news across the web.\n\n## Requirements\n\n* Python 3.10\n* Poetry 1.3.1+ (for dependency management)\n* yarn (for the semantic-release versioning)\n* API Key from the New API Organisation: https://newsapi.org/\n\n## News Sources\n\n- [X] News API. Requires API Key from: https://newsapi.org/\n- [ ] RSS feeds\n\n## Getting started\n\n1. Install and confirm the Python version\n\n```bash\npython --version\n```\n\n2. Create the virtual environment\n\n```bash\npython -m venv .venv\n\n# Activate virtual environment\n.venv/bin/activate # Linux or MacOS\n.venv/Script/activate # Windows\n```\n\n3. Install the requirements\n\n```bash\npoetry install\n```\n\n4. Install the git hook scripts\n\n```bash\npre-commit install\n```\n\n5. Yarn install semantic-release dependencies\n\n```bash\nyarn install\n```\n\n6. Set up husky pre-commit hook\n\n```bash\nyarn husky add .husky/commit-msg 'yarn commitlint --edit $1'\n```\n\n## Chores\n\n- [X] Add GitHub Action for Continuous Integration (CI)\n- [X] Add GitHub Action for Continuous Deployment (CD)\n",
    'author': 'Sechaba Mofokeng',
    'author_email': 'sechaba@onemoola.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/msotho/newspy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
