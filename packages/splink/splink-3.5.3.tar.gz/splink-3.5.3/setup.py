# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['splink',
 'splink.athena',
 'splink.databricks',
 'splink.duckdb',
 'splink.spark',
 'splink.sqlite']

package_data = \
{'': ['*'],
 'splink': ['files/*',
            'files/chart_defs/*',
            'files/chart_defs/del/*',
            'files/external_js/*',
            'files/spark_jars/*',
            'files/splink_cluster_studio/*',
            'files/splink_comparison_viewer/*',
            'files/splink_vis_utils/*',
            'files/templates/*']}

install_requires = \
['Jinja2>=3.0.3,<4.0.0',
 'duckdb>=0.6.0,<0.7.0',
 'jsonschema>=3.2,<5.0',
 'pandas>=1.0.0,<2.0.0',
 'sqlglot==5.1.0']

extras_require = \
{':python_version == "3.6"': ['altair==4.1.0'],
 ':python_version >= "3.7"': ['altair>=4.2.0,<5.0.0']}

setup_kwargs = {
    'name': 'splink',
    'version': '3.5.3',
    'description': 'Fast probabilistic data linkage at scale',
    'long_description': '![image](https://user-images.githubusercontent.com/7570107/85285114-3969ac00-b488-11ea-88ff-5fca1b34af1f.png)\n[![pypi](https://img.shields.io/github/v/release/moj-analytical-services/splink?include_prereleases)](https://pypi.org/project/splink/#history)\n[![Downloads](https://pepy.tech/badge/splink/month)](https://pepy.tech/project/splink)\n[![Documentation](https://img.shields.io/badge/API-documentation-blue)](https://moj-analytical-services.github.io/splink/)\n\n# Fast, accurate and scalable probabilistic data linkage using your choice of SQL backend.\n\n`splink` is a Python package for probabilistic record linkage (entity resolution).\n\nIts key features are:\n\n- It is extremely fast. It is capable of linking a million records on a laptop in around a minute.\n\n- It is highly accurate, with support for term frequency adjustments, and sophisticated fuzzy matching logic.\n\n- Linking jobs can be executed in Python (using the `DuckDB` package), or using big-data backends like `AWS Athena` and `Spark` to link 100+ million records.\n\n- Training data is not required because models can be trained using an unsupervised approach.\n\n- It produces a wide variety of interactive outputs, helping users to understand their model and diagnose linkage problems.\n\nThe core linkage algorithm is an implementation of Fellegi-Sunter\'s model of record linkage, with various customisations to improve accuracy.\n\n## What does Splink do?\n\nSplink deduplicates and/or links records from datasets that lack a unique identifier.\n\nIt assumes that prior to using Splink your datasets have been standardised so they all have the same column names, and consistent formatting (e.g. lowercased, punctuation cleaned up).\n\nFor example, a few of your records may look like this:\n\n| row_id | first_name | surname | dob        | city       |\n| ------ | ---------- | ------- | ---------- | ---------- |\n| 1      | lucas      | smith   | 1984-01-02 | London     |\n| 2      | lucas      | smyth   | 1984-07-02 | Manchester |\n| 3      | lucas      | smyth   | 1984-07-02 |            |\n| 4      | david      | jones   |            | Leeds      |\n| 5      | david      | jones   | 1990-03-21 | Leeds      |\n\nSplink produces pairwise predictions of the links:\n\n| row_id_l | row_id_r | match_probability |\n| -------- | -------- | ----------------- |\n| 1        | 2        | 0.9               |\n| 1        | 3        | 0.85              |\n| 2        | 3        | 0.92              |\n| 4        | 5        | 0.7               |\n\nAnd clusters the predictions to produce an estimated unique id:\n\n| cluster_id | row_id |\n| ---------- | ------ |\n| a          | 1      |\n| a          | 2      |\n| a          | 3      |\n| b          | 4      |\n| b          | 5      |\n\n## What data does Splink work best with?\n\nSplink works best when the input data has multiple columns, and the data in the columns is not highly correlated. For example, if the entity type is persons, you may have their full name, date of birth and city. If the entity type is companies, you may have their name, turnover, sector and telephone number.\n\nSplink will work less well if _all_ of your input columns are highly correlated - for instance, city, county and postal code. You would need to have additional, less correlated columns such as full name or date or birth, for the linkage to work effectively.\n\nSplink is also not designed for linking a single column containing a \'bag of words\'. For example, a table with a single \'company name\' column, and no other details.\n\n## Documentation\n\nThe homepage for the Splink documentation can be found [here](https://moj-analytical-services.github.io/splink/). Interactive demos can be found [here](https://github.com/moj-analytical-services/splink_demos/tree/splink3_demos), or by clicking the following Binder link:\n\n[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/moj-analytical-services/splink_demos/master?urlpath=lab)\n\nThe specification of the Fellegi Sunter statistical model behind `splink` is similar as that used in the R [fastLink package](https://github.com/kosukeimai/fastLink). Accompanying the fastLink package is an [academic paper](http://imai.fas.harvard.edu/research/files/linkage.pdf) that describes this model. A [series of interactive articles](https://www.robinlinacre.com/probabilistic_linkage/) also explores the theory behind Splink.\n\nThe Office for National Statistics have written a [case study about using Splink](https://github.com/Data-Linkage/Splink-census-linkage/blob/main/SplinkCaseStudy.pdf) to link 2021 Census data to itself. \n\n## Installation\n\nSplink supports python 3.7+. To obtain the latest released version of splink:\n\n```sh\npip install splink\n```\n\n## Quickstart\n\nThe following code demonstrates how to estimate the parameters of a deduplication model, use it to identify duplicate records, and then use clustering to generate an estimated unique person ID.\n\nFor more detailed tutorials, please see [here](https://moj-analytical-services.github.io/splink/demos/00_Tutorial_Introduction.html).\n\n```py\nfrom splink.duckdb.duckdb_linker import DuckDBLinker\nfrom splink.duckdb.duckdb_comparison_library import (\n    exact_match,\n    levenshtein_at_thresholds,\n)\n\nimport pandas as pd\n\ndf = pd.read_csv("./tests/datasets/fake_1000_from_splink_demos.csv")\n\nsettings = {\n    "link_type": "dedupe_only",\n    "blocking_rules_to_generate_predictions": [\n        "l.first_name = r.first_name",\n        "l.surname = r.surname",\n    ],\n    "comparisons": [\n        levenshtein_at_thresholds("first_name", 2),\n        exact_match("surname"),\n        exact_match("dob"),\n        exact_match("city", term_frequency_adjustments=True),\n        exact_match("email"),\n    ],\n}\n\nlinker = DuckDBLinker(df, settings)\nlinker.estimate_u_using_random_sampling(target_rows=1e6)\n\nblocking_rule_for_training = "l.first_name = r.first_name and l.surname = r.surname"\nlinker.estimate_parameters_using_expectation_maximisation(blocking_rule_for_training)\n\nblocking_rule_for_training = "l.dob = r.dob"\nlinker.estimate_parameters_using_expectation_maximisation(blocking_rule_for_training)\n\npairwise_predictions = linker.predict()\n\nclusters = linker.cluster_pairwise_predictions_at_threshold(pairwise_predictions, 0.95)\nclusters.as_pandas_dataframe(limit=5)\n```\n\n## Videos\n\n- [A introductory presentation on Splink](https://www.youtube.com/watch?v=msz3T741KQI)\n- [An introduction to the Splink Comparison Viewer dashboard](https://www.youtube.com/watch?v=DNvCMqjipis)\n\n## Acknowledgements\n\nWe are very grateful to [ADR UK](https://www.adruk.org/) (Administrative Data Research UK) for providing the initial funding for this work as part of the [Data First](https://www.adruk.org/our-work/browse-all-projects/data-first-harnessing-the-potential-of-linked-administrative-data-for-the-justice-system-169/) project.\n\nWe are extremely grateful to professors Katie Harron, James Doidge and Peter Christen for their expert advice and guidance in the development of Splink. We are also very grateful to colleagues at the UK\'s Office for National Statistics for their expert advice and peer review of this work. Any errors remain our own.\n',
    'author': 'Robin Linacre',
    'author_email': 'robinlinacre@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/moj-analytical-services/splink',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
