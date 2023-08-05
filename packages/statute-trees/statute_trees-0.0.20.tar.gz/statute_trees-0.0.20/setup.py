# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['statute_trees', 'statute_trees.utils']

package_data = \
{'': ['*']}

install_requires = \
['citation-utils>=0.0.17,<0.0.18',
 'email-validator>=1.3.0,<2.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'markdown>=3.4.1,<4.0.0',
 'statute-patterns>=0.0.25,<0.0.26']

setup_kwargs = {
    'name': 'statute-trees',
    'version': '0.0.20',
    'description': 'Law mostly consists of tree-like nodes. This package supports a common tree format for Philippine Codifications, Statutes, and Documents, using a uniform node structure (i.e., leaves of a tree) identified by a given material path.',
    'long_description': '# Statute Trees\n\n## Prerequisite\n\nTo add a new statute-pattern that will get recognized, update the `statute-patterns` library. This enables the `Rule` mechanism, a pre-requisite to utilizing the `StatuteBase` pydantic model. Trees are a crucial cog in the `corpus-x` library.\n\n## Rules\n\nRules are tree-based. This library facilitates the creation of codifications, statutes, and documents in the form of trees.\n\n```python shell\ntrees=CodeUnit(\n        item=\'Modern Child and Youth Welfare Code\',\n        caption=None,\n        content=None,\n        id=\'1.\',\n        history=None,\n        units=[\n            CodeUnit(\n                item=\'Title I\',\n                caption=\'General Principles\',\n                content=None,\n                id=\'1.1.\',\n                history=None,\n                units=[\n                    CodeUnit(\n                        item=\'Article 1\',\n                        caption=\'Declaration of Policy.\',\n                        content=None,\n                        id=\'1.1.1.\',\n                        history=None,\n                        units=[\n                            CodeUnit(\n                                item=\'Paragraph 1\',\n                                caption=None,\n                                content=\'The Child is one of the most important assets of the nation. Every effort should be exerted to promote his welfare and enhance his opportunities for a useful and happy life.\',\n                                id=\'1.1.1.1.\',\n                                history=None,\n                                units=[]\n                            ),\n                            CodeUnit(\n                                item=\'Paragraph 2\',\n                                caption=None,\n                                content=\'The child is not a mere creature of the State. Hence, his individual traits and aptitudes should be cultivated to the utmost insofar as they do not conflict with the general welfare.\',\n                                id=\'1.1.1.2.\',\n                                history=None,\n                                units=[]\n                            ),\n                        ]\n                    )\n                ]\n            )\n        ]\n    ... # sample excludes the rest of the tree\n)\n```\n\n## Categories\n\nWe\'ll concern ourselves with 3 distinct categorizations of trees as they apply to Philippine law:\n\n1. Codification Trees\n2. Statute Trees\n3. Document Trees\n\nEach of these trees rely on a similar `Node` structure consisting of the following fields:\n\n```python\nclass Node:\n    item: str\n    caption: str\n    content: str\n```\n\nIf we imagine this to be the root of the tree, it can branch out using a `units` key like so:\n\n```python shell\n>>> data = [\n        {\n            "item": "Preliminary Title",\n            "units": [\n                {\n                    "item": "Chapter 1",\n                    "caption": "Effect and Application of Laws",\n                    "units": [\n                        {\n                            "item": "Article 1",\n                            "content": \'This Act shall be known as the "Civil Code of the Philippines." (n)\\n\',\n                        },\n                        {\n                            "item": "Article 2",\n                            "content": "Laws shall take effect after fifteen days following the completion of their publication either in the Official Gazette or in a newspaper of general circulation in the Philippines, unless it is otherwise provided. (1a)\\n",\n                        },\n                    ],\n                }\n            ],\n        }\n    ]\n```\n\nSince each branch needs to be validated, i.e. have the correct type of information per field. We utilize Pydantic for each of the main categories.\n',
    'author': 'Marcelino G. Veloso III',
    'author_email': 'mars@veloso.one',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '==3.11.0',
}


setup(**setup_kwargs)
