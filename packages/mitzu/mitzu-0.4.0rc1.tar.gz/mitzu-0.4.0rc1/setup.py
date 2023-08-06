# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mitzu',
 'mitzu.adapters',
 'mitzu.adapters.sqlalchemy',
 'mitzu.adapters.sqlalchemy.athena',
 'mitzu.adapters.sqlalchemy.athena.sqlalchemy',
 'mitzu.adapters.sqlalchemy.databricks',
 'mitzu.adapters.sqlalchemy.databricks.sqlalchemy',
 'mitzu.notebook',
 'mitzu.samples',
 'mitzu.visualization',
 'mitzu.webapp',
 'mitzu.webapp.auth',
 'mitzu.webapp.pages',
 'mitzu.webapp.pages.connections',
 'mitzu.webapp.pages.dashboards',
 'mitzu.webapp.pages.explore',
 'mitzu.webapp.pages.home',
 'mitzu.webapp.pages.projects']

package_data = \
{'': ['*'], 'mitzu.webapp': ['assets/*', 'assets/warehouse/*']}

install_requires = \
['fastparquet>=0.8.0,<0.9.0',
 'pandas>=1.3.5,<1.4.0',
 'plotly>=5.5.0,<5.6.0',
 'pyarrow>=8.0.0,<8.1.0',
 'sqlalchemy[asyncio]>=1.4.31,<1.5.0',
 'sqlparse>=0.4.2,<0.5.0',
 'tqdm>=4.64.1,<5.0.0']

extras_require = \
{'athena': ['PyAthena>=2.13.0,<3.0.0'],
 'databricks': ['databricks-sql-connector>=2.0.2,<3.0.0'],
 'mysql': ['mysql-connector-python>=8.0.28,<8.1.0'],
 'postgres': ['psycopg2>=2.9.3,<2.10.0'],
 'snowflake': ['snowflake-sqlalchemy>=1.4.3,<2.0.0'],
 'trinodwh': ['trino[sqlalchemy]>=0.313.0,<0.314.0'],
 'webapp': ['dash[celery,compress,diskcache]>=2.6.0,<3.0.0',
            'dash-bootstrap-components>=1.2.0,<2.0.0',
            'dash-mantine-components>=0.11.1,<0.12.0',
            'orjson>=3.7.11,<4.0.0',
            'PyJWT[crypto]>=2.4.0,<3.0.0',
            'gunicorn>=20.1.0,<21.0.0',
            'redis>=4.4.0,<5.0.0',
            'kaleido==0.2.1',
            'dash-iconify>=0.1.2,<0.2.0',
            'dash-draggable>=0.1.2,<0.2.0',
            'requests>=2.28.2,<3.0.0']}

setup_kwargs = {
    'name': 'mitzu',
    'version': '0.4.0rc1',
    'description': 'Product analytics over your data warehouse',
    'long_description': '[![PyPI version](https://badge.fury.io/py/mitzu.svg)](https://badge.fury.io/py/mitzu)\n![Mit - License](https://img.shields.io/pypi/l/mitzu)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mitzu.svg)](https://pypi.org/project/mitzu/)\n\n<h2 align="center">\n<b>Mitzu<b> is an open source <b>product analytics </b> tool that queries your <b>data lake</b> or <b>data warehouse</b>.\n</h2>\n</br>\n\n![webapp example](https://raw.githubusercontent.com/mitzu-io/mitzu/main/resources/mitzu_webapp_hero.gif)\n\n</br>\n\n# Features\n\n- Visualization for:\n  - Funnels\n  - Segmentation\n  - Retention\n  - User Journey (coming soon)\n  - Revenue calculations (coming soon)\n- User Lookup (coming soon)\n- Cohorts Analysis\n- Standalone web app for non-tech people\n- Notebook visual app\n- Notebook low-code analytics in python\n- Batch ETL jobs support\n\n# Supported Integrations\n\nMitzu integrates with most modern data lake and warehouse solutions:\n\n- [AWS Athena](https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)\n- [Databricks Spark (SQL)](https://www.databricks.com/product/databricks-sql)\n- Files - [SQLite](https://www.sqlite.org/index.html) (csv, parquet, json, etc.)\n- [MySQL](https://www.mysql.com/)\n- [PostgreSQL](https://www.postgresql.org/)\n- [Snowflake](https://www.snowflake.com/en/)\n- [Trino / Starburst](https://trino.io/)\n\n## Coming Soon\n\n- [Clickhouse](https://clickhouse.com/)\n- [BigQuery](https://cloud.google.com/bigquery/)\n- [Redshift](https://aws.amazon.com/redshift/)\n\n# Quick Start\n\nIn this section, we will describe how to start with `Mitzu` on your local machine. Skip this section if you rather see `Mitzu` in a prepared notebook or webapp. Otherwise get ready and fire up your own data-science [notebook](https://jupyter.org/).\n![Notebook example](https://raw.githubusercontent.com/mitzu-io/mitzu/main/resources/mitzu_notebook_hero.gif)\n\n---\n\nInstall the Mitzu python library\n\n```\npip install mitzu\n```\n\n## Reading The Sample Dataset\n\nThe simplest way to get started with `Mitzu` is in a data-science notebook. In your notebook read the sample user behavior dataset.\nMitzu can [discover](https://mitzu.io/documentation/discovery) your tables in a data warehouse or data lake. For the sake of simplicity we provide you an in-memory [sqlite](https://www.sqlite.org/index.html) based table that contains\n\n```python\nimport mitzu.samples as smp\n\ndp = smp.get_sample_discovered_project()\nm = dp.create_notebook_class_model()\n```\n\n## Segmentation\n\nThe following command visualizes the `count of unique users` over time who did `page visit` action in the last `30 days`.\n\n```python\nm.page_visit\n```\n\n![segmentation metric](https://raw.githubusercontent.com/mitzu-io/mitzu/main/resources/segmentation.png)\n\nIn the example above `m.page_visit` refers to a `user event segment` for which the notebook representation is a `segmentation chart`.\nIf this sounds unfamiliar, don\'t worry! Later we will explain you everything.\n\n## Funnels\n\nYou can create a `funnel chart` by placing the `>>` operator between two `user event segments`.\n\n```python\nm.page_visit >> m.checkout\n```\n\nThis will visualize the `conversion rate` of users that first did `page_visit` action and then did `checkout` within a day in the last 30 days.\n\n## Filtering\n\nYou can apply filters to `user event segment` the following way:\n\n```python\nm.page_visit.user_country_code.is_us >> m.checkout\n\n# You can achieve the same filter with:\n# (m.page_visit.user_country_code == \'us\')\n#\n# you can also apply >, >=, <, <=, !=, operators.\n```\n\nWith this syntax we have narrowed down our `page visit` `user event segment` to page visits from the `US`.\nStacking filters is possible with the `&` (and) and `|` (or) operators.\n\n```python\nm.page_visit.user_country_code.is_us & m.page_visit.acquisition_campaign.is_organic\n\n# if using the comparison operators, make sure you put the user event segments in parenthesis.\n# (m.page_visit.user_country_code == \'us\') & (m.page_visit.acquisition_campaign == \'organic\')\n```\n\nApply multi value filtering with the `any_of` or `none_of` functions:\n\n```python\nm.page_visit.user_country_code.any_of(\'us\', \'cn\', \'de\')\n\n# m.page_visit.user_country_code.none_of(\'us\', \'cn\', \'de\')\n```\n\nOf course you can apply filters on every `user event segment` in a funnel.\n\n```python\nm.add_to_cart >> (m.checkout.cost_usd <= 1000)\n```\n\n## Metrics Configuration\n\nTo any funnel or segmentation you can apply the config method. Where you can define the parameters of the metric.\n\n```python\nm.page_visit.config(\n   start_dt="2021-08-01",\n   end_dt="2021-09-01",\n   group_by=m.page_visit.domain,\n   time_group=\'total\',\n)\n```\n\n- `start_dt` should be an iso datetime string, or python datetime, where the metric should start.\n- `end_dt` should be an iso datetime string, or python datetime, where the metric should end.\n- `group_by` is a property that you can refer to from the notebook class model.\n- `time_group` is the time granularity of the query for which the possible values are: `hour`, `day`, `week`, `month`, `year`, `total`\n\nFunnels have an extra configuration parameter `conv_window`, this has the following format: `<VAL> <TIME WINDOW>`, where `VAL` is a positive integer.\n\n```python\n(m.page_visit >> m.checkout).config(\n   start_dt="2021-08-01",\n   end_dt="2021-09-01",\n   group_by=m.page_visit.domain,\n   time_group=\'total\',\n   conv_window=\'1 day\',\n)\n```\n\n## SQL Generator\n\nFor any metric you can print out the SQL code that `Mitzu` generates.\nThis you can do by calling the `.print_sql()` method.\n\n```python\n(m.page_visit >> m.checkout).config(\n   start_dt="2021-08-01",\n   end_dt="2021-09-01",\n   group_by=m.page_visit.domain,\n   time_group=\'total\',\n   conv_window=\'1 day\',\n).print_sql()\n```\n\n![webapp example](https://raw.githubusercontent.com/mitzu-io/mitzu/main/resources/print_sql.png)\n\n## Pandas DataFrames\n\nSimilarly you can access the results in the form of a [Pandas](https://pandas.pydata.org/) DataFrame with the method `.get_df()`\n\n```python\n(m.page_visit >> m.checkout).config(\n   start_dt="2021-08-01",\n   end_dt="2021-09-01",\n   group_by=m.page_visit.domain,\n   time_group=\'total\',\n   conv_window=\'1 day\',\n).get_df()\n```\n\n## Notebook Dashboards\n\nYou can also visualize the webapp in a Jupyter Notebook:\n\n```python\nimport mitzu.samples as smp\n\ndp = smp.get_sample_discovered_project()\ndp.notebook_dashboard()\n```\n\n![dash](https://raw.githubusercontent.com/mitzu-io/mitzu/main/resources/dash_notebook.png)\n\n## Usage In Notebooks\n\n- [Example notebook](https://deepnote.com/@istvan-meszaros/Mitzu-Introduction-af037f5a-2184-494d-9362-6f4c69b5eedc)\n- [Documentation](https://mitzu.io/documentation/notebook)\n\n## Webapp\n\nMitzu can run as a standalone webapp or embedded inside a notebook.\n\nTrying out locally:\n\n```bash\ndocker run -p 8082:8082 imeszaros/mitzu-webapp\n```\n\n- [Example webapp](https://app.mitzu.io)\n- [Webapp documentation](https://mitzu.io/documentation/webapp)\n\n## Connect Your Own Data\n\nMitzu is be able to connect to your data warehouse or data lake.\nTo get started with your own data integration please read our handy\n[docs](/DOCS.md)\n\n## Contribution Guide\n\nPlease read our [Contribution Guide](/CONTRIBUTION.md)\n',
    'author': 'Istvan Meszaros',
    'author_email': 'istvan.meszaros.88@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://mitzu.io',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
