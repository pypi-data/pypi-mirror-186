# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['drpt']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'dask>=2023.1.0,<2024.0.0',
 'jsonschema>=4.17.3,<5.0.0',
 'pandas>=1.5.2,<2.0.0',
 'pyarrow>=10.0.1,<11.0.0']

entry_points = \
{'console_scripts': ['drpt = drpt.__main__:main']}

setup_kwargs = {
    'name': 'drpt',
    'version': '0.8.2',
    'description': 'Tool for preparing a dataset for publishing by dropping, renaming, scaling, and obfuscating columns defined in a recipe.',
    'long_description': '# Data Release Preparation Tool\n\n- [Data Release Preparation Tool](#data-release-preparation-tool)\n  - [Description](#description)\n  - [Installation](#installation)\n  - [Usage](#usage)\n    - [CLI](#cli)\n    - [Recipe Definition](#recipe-definition)\n  - [Example](#example)\n  - [Thanks](#thanks)\n\n> :warning: This is currently at beta development stage and likely has a lot of bugs. Please use the [issue tracker](https://github.com/ConX/drpt/issues) to report an bugs or feature requests.\n\n## Description\n\nCommand-line tool for preparing a dataset for publishing by dropping, renaming, scaling, and obfuscating columns defined in a recipe.\n\nAfter performing the operations defined in the recipe the tool generates the transformed dataset version and a CSV report listing the performed actions.\n\n## Installation\n\nThe tool can be installed using pip:\n\n```shell\npip install drpt\n```\n\n## Usage\n\n### CLI\n\n```txt\nUsage: drpt [OPTIONS] RECIPE_FILE INPUT_FILE\n\nOptions:\n  -d, --dry-run           Generate only the report without the release dataset\n  -v, --verbose           Verbose [Not implemented]\n  -n, --nrows TEXT        Number of rows to read from a CSV file. Doesn\'t work\n                          with parquet files.\n  -l, --limits-file PATH  Limits file\n  -o, --output-dir PATH   Output directory. The default output directory is\n                          the same as the location of the recipe_file.\n  --version               Show the version and exit.\n  --help                  Show this message and exit.\n```\n\n### Recipe Definition\n\n#### Overview\nThe recipe is a JSON formatted file that includes what operations should be performed on the dataset. For versioning purposes, the recipe also contains a `version` key which is appended in the generated filenames and the report.\n\n**Default recipe:**\n```json\n{\n  "version": "",\n  "actions": {\n    "drop": [],\n    "drop-constant-columns": false,\n    "obfuscate": [],\n    "disable-scaling": false,\n    "skip-scaling": [],\n    "sort-by": [],\n    "rename": []\n  }\n}\n```\n\nThe currently supported actions, performed in this order, are as follows:\n  - `drop`: Column deletion\n  - `drop-constant-columns`: Drops all columns that containt only one unique value\n  - `obfuscate`: Column obfuscation, where the listed columns are treated as categorical variables and then integer coded.\n  - Scaling: By default all columns are Min/Max scaled\n    - `disable-scaling`: Can be used to disable scaling for all columns\n    - `skip-scaling`: By default all columns are Min/Max scaled, except those excluded (`skip-scaling`)\n  - `sort-by`: Sort rows by the listed columns\n  - `rename`: Column renaming\n\nAll column definitions above support [regular expressions](https://docs.python.org/3/library/re.html#regular-expression-syntax).\n\n#### Actions\n\n##### _drop_\nThe `drop` action is defined as a list of column names to be dropped.\n\n##### _drop-constant-columns_\nThis is a boolean action, which when set to `true` will drop all the columns that have only a single unique value.\n\n##### _obfuscate_\nThe `obfuscate` action is defined as a list of column names to be obfuscated.\n\n##### _disable-scaling_, _skip-scaling_\nBy default, the tool Min/Max scales all numerical columns. This behavior can be disabled for all columns by setting the `disable-scaling` action to `true`. If scaling must be disabled for only a set of columns these columns can be defined using the `skip-scaling` action, as a list of column names.\n\n##### _sort-by_\nThis is a list of column names by which to sort the rows. The order in the list denotes the sorting priority.\n\n##### _rename_\nThe `rename` action is defined as a list of objects whose key is the original name (or regular expression), and their value is the target name. When the target uses matched groups from the regular expression those can be provided with their group number prepended with an escaped backslash (`\\\\1`) [see [example](#example) below].\n\n```json\n{\n  //...\n  "rename": [{"original_name": "target_name"}]\n  //...\n}\n```\n## Example\n\n**Input CSV file:**\n```csv\ntest1,test2,test3,test4,test5,test6,test7,test8,test9,foo.bar.test,foo.bar.test2,const\n1.1,1,one,2,0.234,0.3,-1,a,e,1,1,1\n2.2,2,two,2,0.555,0.4,0,b,f,2,2,1\n3.3,3,three,4,0.1,5,1,c,g,3,3,1\n2.22,2,two,4,1,0,2.5,d,h,4,4,1\n```\n\n**Recipe:**\n```json\n{\n  "version": "1.0",\n  "actions": {\n    "drop": ["test2", "test[8-9]"],\n    "drop-constant-columns": true,\n    "obfuscate": ["test3"],\n    "skip-scaling": ["test4"],\n    "sort-by": ["test4", "test3"],\n    "rename": [\n      { "test1": "test1_renamed" },\n      { "test([3-4])": "test\\\\1_regex_renamed" },\n      { "foo[.]bar[.].*": "foo" }\n    ]\n  }\n}\n```\n\n**Generated CSV file:**\n```csv\ntest3_regex_renamed,test4_regex_renamed,test1_renamed,test5,test6,test7,foo_1,foo_2\n0,2,0.0,0.1488888888888889,0.06,0.0,0.0,0.0\n2,2,0.5000000000000001,0.5055555555555556,0.08,0.2857142857142857,0.3333333333333333,0.3333333333333333\n1,4,1.0,0.0,1.0,0.5714285714285714,0.6666666666666666,0.6666666666666666\n2,4,0.5090909090909091,1.0,0.0,1.0,1.0,1.0\n```\n\n**Report:**\n```csv\n,action,column,details\n0,recipe_version,,1.0\n1,drpt_version,,0.6.3\n2,DROP,test2,\n3,DROP,test8,\n4,DROP,test9,\n5,DROP_CONSTANT,const,\n6,OBFUSCATE,test3,"{""one"": 0, ""three"": 1, ""two"": 2}"\n7,SCALE_DEFAULT,test1,"[1.1,3.3]"\n8,SCALE_DEFAULT,test5,"[0.1,1.0]"\n9,SCALE_DEFAULT,test6,"[0.0,5.0]"\n10,SCALE_DEFAULT,test7,"[-1.0,2.5]"\n11,SCALE_DEFAULT,foo.bar.test,"[1,4]"\n12,SCALE_DEFAULT,foo.bar.test2,"[1,4]"\n13,SORT,"[\'test4\', \'test3\']",\n14,RENAME,test1,test1_renamed\n15,RENAME,test3,test3_regex_renamed\n16,RENAME,test4,test4_regex_renamed\n17,RENAME,foo.bar.test,foo_1\n18,RENAME,foo.bar.test2,foo_2\n```\n\n## Thanks\n\nThis tool was made possible with [Pandas](https://pandas.pydata.org/), [PyArrow](https://arrow.apache.org/docs/python/index.html), [jsonschema](https://pypi.org/project/jsonschema/), and of course [Python](https://www.python.org/).\n\n\n  ',
    'author': 'Constantinos Xanthopoulos',
    'author_email': 'conx@xanthopoulos.info',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ConX/drpt',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
