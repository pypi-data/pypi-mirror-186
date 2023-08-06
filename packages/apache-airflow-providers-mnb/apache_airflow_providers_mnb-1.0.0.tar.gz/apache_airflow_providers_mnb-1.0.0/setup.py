# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['airflow',
 'airflow.providers.mnb',
 'airflow.providers.mnb.hooks',
 'airflow.providers.mnb.operators',
 'airflow.providers.mnb.sensors']

package_data = \
{'': ['*']}

install_requires = \
['apache-airflow>=2.0,<3.0', 'mnb>=1.0.0,<2.0.0', 'zeep>=4.2,<5.0']

entry_points = \
{'apache_airflow_provider': ['provider_info = '
                             'airflow.providers.mnb.__init__:get_provider_info']}

setup_kwargs = {
    'name': 'apache-airflow-providers-mnb',
    'version': '1.0.0',
    'description': 'Provider for Apache Airflow. Implements apache-airflow-providers-mnb package',
    'long_description': '# MNB Provider for Apache Airflow\n\nThis package contains all the necessary operators, hooks and sensors necessary to access the daily exchange rates published by MNB (Central Bank of Hungary) in Apache Airflow.\n\n## Installation\n\nYou can install it with any package manager compatible with PyPI:\n\n```\npip install apache-airflow-provider-mnb\n```\n\n## Components\n\n| Component | Notes |\n| - | - |\n| `MnbHook` | Implements low-level functions to interact with MNB\'s API |\n| `MnbExchangeRateOperator` | Provides access to the exchange rates published on a specific day |\n| `MnbExchangeRateSensor` | Senses whether the rates were already published for a specific day\n\n## Example\nThis following example demonstrates a typical use case:\n\n1. Start running at 8:00AM every day\n1. Check if the exchange rates were already published (repeat every 10 minutes)\n1. Permanently fail after 3 hours if the rates were never published (there are no rates available on the weekends and public holidays)\n1. Generate the SQL commands\n1. Run them against a PostgreSQL database\n\n```python\nfrom datetime import date\nimport json\nimport pendulum\nfrom airflow.decorators import dag, task\nfrom airflow.providers.postgres.operators.postgres import PostgresOperator\nfrom airflow.providers.mnb.sensors.mnb import MnbExchangeRateSensor\nfrom airflow.providers.mnb.operators.mnb import MnbExchangeRateOperator\n\n@dag(\n    dag_id="refresh_currency_rates",\n    description="Refresh currency exchange rates",\n    schedule="0 8 * * *",\n    start_date=pendulum.datetime(2023, 1, 16, tz="Europe/Budapest"),\n    catchup=False\n)\ndef mnb():\n    is_exchange_rate_available = MnbExchangeRateSensor(\n        task_id="is_exchange_rate_available",\n        timeout=10800,\n        poke_interval=600,\n        date=date.today()\n    )\n    \n    exchange_rates = MnbExchangeRateOperator(\n        task_id="get_exchange_rates",\n        date=date.today()\n    )\n    \n    @task\n    def generate_queries(exchange_rates: str):\n        rates = json.loads(exchange_rates)\n        queries = ""\n        mnb_date = rates["date"]\n        for rate in rates["rates"]:\n            currency_id = rate["currency"]\n            mnb_rate = rate["rate"]\n            queries += f"UPDATE finance.currency SET mnb_rate = \'{mnb_rate}\', mnb_date = \'{mnb_date}\' WHERE currency_id = \'{currency_id}\';\\n"\n        return queries\n\n    is_exchange_rate_available >> exchange_rates\n\n    queries = generate_queries(exchange_rates.output)\n    PostgresOperator(\n        task_id="update_exchange_rates",\n        postgres_conn_id="postgres_default",\n        database="erp",\n        sql=queries)\n\nmnb()\n```',
    'author': 'Balázs Keresztury',
    'author_email': 'balazs@keresztury.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/belidzs/airflow-provider-mnb',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.1,<4.0.0',
}


setup(**setup_kwargs)
