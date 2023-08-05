# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['statute_patterns', 'statute_patterns.components', 'statute_patterns.recipes']

package_data = \
{'': ['*']}

install_requires = \
['email-validator>=1.3.0,<2.0.0',
 'pydantic>=1.10.4,<2.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'python-dotenv>=0.21,<0.22',
 'python-slugify>=6.1.2,<7.0.0']

setup_kwargs = {
    'name': 'statute-patterns',
    'version': '0.0.25',
    'description': 'Philippine statutory law pattern matching library.',
    'long_description': '# Statute Patterns\n\n## Title and path matching of rules\n\nDetect titles of Philippine statutory text from given text input.\n\nUpon detection, generate a possible path from which to extract the content of a detected rule.\n\nThis presumes existence of a local path to separate library from which the contents of the rule can be extracted from.\n\n```python\n# use sample text for demo\n>>> text = """The Civil Code of the Philippines, the old Spanish Civil Code; Rep Act No. 386"""\n\n# get first matching rule with helper to extract path\nfrom statute_patterns import extract_rule\n>>> rule_obj = extract_rule(text)\n>>> rule_obj\nRule(cat=\'ra\', id=\'386\')\n\n\n# get all rules\n>>> from statute_patterns import extract_rules\n>>> extract_rules(text)\n[\n    Rule(cat=\'ra\', id=\'386\'),\n    Rule(cat=\'ra\', id=\'386\'),\n    Rule(cat=\'spain\', id=\'civil\')\n]\n\n\n# get unique rules with counts\n>>> from statute_patterns import count_rules\n>>> count_rules(text):\n[\n    {\'cat\': \'ra\', \'id\': \'386\', \'mentions\': 2},\n    {\'cat\': \'spain\', \'id\': \'civil\', \'mentions\': 1}\n]\n```\n\n## Loading files from rules\n\nEach rule corresponds to a possible set of folders in a local directory `/statutes`.\n\nEach rule belongs to a *StatuteSerialCategory*. The present *StatuteSerialCategory* is an Enum with the following members. The value of each member is the path to such category.\n\n```python\n>>>StatuteSerialCategory\n<enum \'StatuteSerialCategory\'>\n>>>StatuteSerialCategory._member_map_\n{\n    \'RepublicAct\': <StatuteSerialCategory.RepublicAct: \'ra\'>,\n    \'CommonwealthAct\': <StatuteSerialCategory.CommonwealthAct: \'ca\'>,\n    \'Act\': <StatuteSerialCategory.Act: \'act\'>,\n    \'Constitution\': <StatuteSerialCategory.Constitution: \'const\'>,\n    \'Spain\': <StatuteSerialCategory.Spain: \'spain\'>,\n    \'BatasPambansa\': <StatuteSerialCategory.BatasPambansa: \'bp\'>,\n    \'PresidentialDecree\': <StatuteSerialCategory.PresidentialDecree: \'pd\'>,\n    \'ExecutiveOrder\': <StatuteSerialCategory.ExecutiveOrder: \'eo\'>,\n    \'LetterOfInstruction\': <StatuteSerialCategory.LetterOfInstruction: \'loi\'>,\n    \'VetoMessage\': <StatuteSerialCategory.VetoMessage: \'veto\'>,\n    \'RulesOfCourt\': <StatuteSerialCategory.RulesOfCourt: \'roc\'>,\n    \'BarMatter\': <StatuteSerialCategory.BarMatter: \'rule_bm\'>,\n    \'AdministrativeMatter\': <StatuteSerialCategory.AdministrativeMatter: \'rule_am\'>,\n    \'ResolutionEnBanc\': <StatuteSerialCategory.ResolutionEnBanc: \'rule_reso\'>,\n    \'CircularOCA\': <StatuteSerialCategory.CircularOCA: \'oca_cir\'>,\n    \'CircularSC\': <StatuteSerialCategory.CircularSC: \'sc_cir\'>\n}\n```\n\nSo to point to the Civil Code of the Philippines, this would be represented by the following path `statutes/ra/386` where *ra* is the StatuteSerialCategory and *386* is the serial id.\n\nKnowing the path to a rule, we can extract the rules contents.\n\n```python\n>>> rule_obj # example from above\nRule(cat=\'ra\', id=\'386\')\n>>> list(rule_obj.extract_folders(<path/to/statutes>))\n[PosixPath(\'.../statutes/ra/386\')]\n```\n\nThere can be more than one path since in exceptional cases, the combination of *category* + *serial id* does not yield a unique rule.\n\nWe can extract the details of the rule with the `StatuteDetails.from_rule()` also accessible via `Rule.get_details()`:\n\n```python\n>>>from statute_patterns import StatuteDetails\n>>>StatuteDetails.from_rule(rule_obj, <path/to/statutes>) # or rule_obj.get_details(<path/to/details>)\nStatuteDetails(\n    created=1665225124.0644598,\n    modified=1665225124.0644598,\n    rule=Rule(cat=\'ra\', id=\'386\'),\n    title=\'Republic Act No. 386\',\n    description=\'An Act to Ordain and Institute the Civil Code of the Philippines\',\n    id=\'ra-386-june-18-1949\',\n    emails=[\'maria@abcxyz.law\', \'fernando@abcxyz.law\'],\n    date=datetime.date(1949, 6, 18),\n    variant=1,\n    units=[\n        {\n            \'item\': \'Container 1\',\n            \'caption\': \'Preliminary Title\',\n            \'units\': [\n                {\n                    \'item\': \'Chapter 1\',\n                    \'caption\': \'Effect and Application of Laws\',\n                    \'units\': [\n                        {\n                            \'item\': \'Article 1\',\n                            \'content\': \'This Act shall be known as the "Civil Code of the Philippines." (n)\\n\'\n                        },\n                        {\n                            \'item\': \'Article 2\',\n                            \'content\': \'Laws shall take effect after fifteen days following the completion of their publication either in the Official Gazette or in a newspaper of general circulation in the Philippines, unless it is otherwise provided. (1a)\\n\'\n                        },\n                        ...\n                    ]\n                },\n                ...\n            ]\n        },\n        ...\n    ],\n    titles=[\n        StatuteTitle(\n            statute_id=\'ra-386-june-18-1949\',\n            category=\'alias\',\n            text=\'New Civil Code\'\n        ),\n        StatuteTitle(\n            statute_id=\'ra-386-june-18-1949\',\n            category=\'alias\',\n            text=\'Civil Code of 1950\'\n        ),\n        StatuteTitle(\n            statute_id=\'ra-386-june-18-1949\',\n            category=\'official\',\n            text=\'An Act to Ordain and Institute the Civil Code of the Philippines\'\n        ),\n        StatuteTitle(\n            statute_id=\'ra-386-june-18-1949\',\n            category=\'serial\',\n            text=\'Republic Act No. 386\'\n        )\n    ]\n)\n```\n',
    'author': 'Marcelino G. Veloso III',
    'author_email': 'mars@veloso.one',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
