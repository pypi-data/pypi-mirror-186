# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['todoist_tree']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'todoist-tree',
    'version': '0.1.0',
    'description': 'Create a tree from Todoist projects > sections > tasks',
    'long_description': '# todoist_tree\n\nThese are the core functions of [todoist_bot](https://github.com/ShayHill/todoist_bot).\n\nThe reading and writing functions are just (sometimes typeguarded) aliases of Todoist api calls. The differentiating functionality is building a tree with\n\n``` python\nimport time\nfrom todoist_tree import headers\nfrom todoist_tree import read_changes\nfrom todoist_tree import tree\n\nheaders = new_headers(api_token)\ntodoist = None\nsync_token: str = "*"\n\ncomplete = False\n\nwhile not complete:\n\n    todoist = read_changes.read_changes(headers)\n    if todoist is None:\n        # no changes or failure\n        time.sleep(2)\n        continue\n\n    sync_token = todoist.sync_token\n\n    projects = todoist.projects\n    sections = todoist.sections\n    tasks = todoist.tasks\n\n    id2node = tree.map_id_to_branch(\n        todoist.projects,\n        todoist.sections,\n        todoist.tasks\n    )\n\n    # do something here\n\n    time.sleep(5)\n```\n\nThe tree isn\'t doesn\'t have one root. `map_id_to_branch` maps the id[1] of each project, section, and task to a node. Top-level projects will not have parents, so they are effectively roots of their own trees.\n\nSee [todoist_bot](https://github.com/ShayHill/todoist_bot) for a full example.\n\n[1] where `id` is the value returned in the json dictionary from the Todoist api, *not* the Python object id.\n',
    'author': 'Shay Hill',
    'author_email': 'shay_public@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
