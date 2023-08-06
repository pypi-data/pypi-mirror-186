# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kafka_connect']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'requests>=2.25,<3.0']

entry_points = \
{'console_scripts': ['kafka-connect = kafka_connect.cli:cli',
                     'kc = kafka_connect.cli:cli']}

setup_kwargs = {
    'name': 'kafka-connect-py',
    'version': '0.6.1',
    'description': 'A client for the Confluent Platform Kafka Connect REST API.',
    'long_description': '# Kafka Connect Python\n\nThe Kafka Connect REST API allows you to manage connectors that move data between Apache Kafka and other systems.\n\nThe Kafka Connect command line tool, also known as `kc` or `kafka-connect`, allows users to manage their Kafka Connect cluster and connectors. With this tool, users can retrieve information about the cluster and connectors, create new connectors, update existing connectors, delete connectors, and perform other actions.\n\nThis project aims to supported all features of the [Kafka Connect REST API](https://docs.confluent.io/platform/current/connect/references/restapi.html#kconnect-rest-interface).\n\n## Install\n\n```bash\npip install kafka-connect-py\n```\n\n## Command Line Usage\n\nGet the version and other details of the Kafka Connect cluster.\n\n```bash\nkc info\n```\n\n###### Get a list of all connectors\n\n```bash\nkc list [--expand=status|info] [--connector-pattern=regex]\n```\n\n###### Get the details of a single connector\n\n```bash\nkc get <connector>\n```\n\n###### Get the status of a connector\n\n```bash\nkc status <connector>\n```\n\n###### Get the config of a connector\n\n```bash\nkc config <connector>\n```\n\n###### Create a new connector with a JSON file\n\n```bash\nkc create --config-file <config-file>\n```\n\n###### Create a new connector with inline JSON data\n\n```bash\nkc create --config-data <config-data>\n```\n\n###### Update the configuration for an existing connector with a JSON file\n\n```bash\nkc update <connector> --config-file <config_file>\n```\n\n###### Update the configuration for an existing connector with inline JSON data\n\n```bash\nkc create <connector> --config-data <config-data>\n```\n\n###### Restart a connector\n\n```bash\nkc restart <connector> [--include-tasks] [--only-failed]\n```\n\n###### Restart all connectors\n\n```bash\nkc restart --all-connectors [--connector-pattern=regex]\n```\n\n###### Pause a connector\n\n```bash\nkc pause <connector>\n```\n\n###### Pause all connectors\n\n```bash\nkc pause --all-connectors [--connector-pattern=regex]\n```\n\n###### Resume a connector\n\n```bash\nkc resume <connector>\n```\n\n###### Resume all connectors\n\n```bash\nkc resume --all-connectors [--connector-pattern=regex]\n```\n\n###### Delete a connector\n\n```bash\nkc delete <connector>\n```\n\n###### Delete all connectors\n\n```bash\nkc delete --all-connectors [--connector-pattern=regex]\n```\n\n### Python\n\n```python\n# Import the class\nfrom kafka_connect import KafkaConnect\n\n# Instantiate the client\nclient = KafkaConnect(endpoint="http://localhost:8083")\n\n# Get the version and other details of the Kafka Connect cluster\ncluster = client.get_info()\nprint(cluster)\n\n# Get a list of active connectors\nconnectors = client.get_connectors()\nprint(connectors)\n\n# Create a new connector\nconfig = {\n    "name": "my-connector",\n    "config": {\n        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",\n        "tasks.max": "1",\n        "connection.url": "jdbc:postgresql://localhost:5432/mydatabase",\n        "connection.user": "myuser",\n        "connection.password": "mypassword",\n        "table.whitelist": "mytable",\n        "mode": "timestamp+incrementing",\n        "timestamp.column.name": "modified_at",\n        "validate.non.null": "false",\n        "incrementing.column.name": "id",\n        "topic.prefix": "my-connector-",\n    },\n}\nresponse = client.create_connector(config)\nprint(response)\n\n# Update an existing connector\nnew_config = {\n    "config": {\n        "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",\n        "tasks.max": "1",\n        "connection.url": "jdbc:postgresql://localhost:5432/mydatabase",\n        "connection.user": "myuser",\n        "connection.password": "mypassword",\n        "table.whitelist": "mytable",\n        "mode": "timestamp+incrementing",\n        "timestamp.column.name": "modified_at",\n        "validate.non.null": "false",\n        "incrementing.column.name": "id",\n        "topic.prefix": "my-connector-",\n    },\n}\nresponse = client.update_connector("my-connector", new_config)\nprint(response)\n\n# Restart a connector\nresponse = client.restart_connector("my-connector")\nprint(response)\n\n# Delete a connector\nresponse = client.delete_connector("my-connector")\nprint(response)\n```\n\n## Tests\n\n```\npython3 -m unittest tests/test_kafka_connect.py -v\n```',
    'author': 'Aidan Melen',
    'author_email': 'aidan-melen@protonmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aidanmelen/kafka-connect-py',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
