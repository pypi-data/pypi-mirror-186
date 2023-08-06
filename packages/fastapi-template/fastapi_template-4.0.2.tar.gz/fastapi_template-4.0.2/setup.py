# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_template',
 'fastapi_template.template.hooks',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_ormar',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_ormar.dao',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_ormar.migrations',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_ormar.migrations.versions',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_ormar.models',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_piccolo',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_piccolo.dao',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_piccolo.migrations',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_piccolo.models',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_psycopg',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_psycopg.dao',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_psycopg.models',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_sa',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_sa.dao',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_sa.migrations',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_sa.migrations.versions',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_sa.models',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_tortoise',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_tortoise.dao',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_tortoise.models',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.services',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.services.kafka',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.services.rabbit',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.services.redis',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.tests',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.api',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.api.docs',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.api.dummy',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.api.echo',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.api.kafka',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.api.monitoring',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.api.rabbit',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.api.redis',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.gql',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.gql.dummy',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.gql.echo',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.gql.kafka',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.gql.rabbit',
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.web.gql.redis',
 'fastapi_template.tests']

package_data = \
{'': ['*'],
 'fastapi_template': ['template/*',
                      'template/{{cookiecutter.project_name}}/*',
                      'template/{{cookiecutter.project_name}}/.github/workflows/*',
                      'template/{{cookiecutter.project_name}}/deploy/*',
                      'template/{{cookiecutter.project_name}}/deploy/kube/*'],
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}': ['static/docs/*'],
 'fastapi_template.template.{{cookiecutter.project_name}}.{{cookiecutter.project_name}}.db_tortoise': ['migrations/models/*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'cookiecutter>=1.7.3,<2.0.0',
 'pre-commit>=2.14.0,<3.0.0',
 'prompt-toolkit>=3.0.36,<4.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'simple-term-menu>=1.5.2,<2.0.0',
 'termcolor>=1.1.0,<2.0.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['fastapi_template = fastapi_template.__main__:main']}

setup_kwargs = {
    'name': 'fastapi-template',
    'version': '4.0.2',
    'description': 'Feature-rich robust FastAPI template',
    'long_description': '![python version](https://img.shields.io/pypi/pyversions/fastapi_template?style=for-the-badge) [![version](https://img.shields.io/pypi/v/fastapi_template?style=for-the-badge)](https://pypi.org/project/fastapi-template/)\n[![](https://img.shields.io/pypi/dm/fastapi_template?style=for-the-badge)](https://pypi.org/project/fastapi-template/)\n<div align="center">\n<img src="https://raw.githubusercontent.com/s3rius/FastAPI-template/master/images/logo.png" width=700>\n<div><i>Flexible general-purpose template for FastAPI.</i></div>\n</div>\n\n## Usage\n\n⚠️ [Git](https://git-scm.com/downloads), [Python](https://www.python.org/) and [Poetry](https://python-poetry.org/) must be installed and accessible ⚠️\n\nPoetry version must be greater or equal than 1.1.8. Otherwise it won\'t be able to install SQLAlchemy.\n\n<div align="center">\n <a href="https://asciinema.org/a/ig0oi0fOq1hxqnW5X49XaaHIT" target="_blank"><img src="https://asciinema.org/a/ig0oi0fOq1hxqnW5X49XaaHIT.svg" /></a>\n  <p>Templator in action</p>\n</div>\n\nYou can install it directly from pypi with pip.\n```bash\npython3 -m pip install fastapi_template\npython3 -m fastapi_template\n# or fastapi_template\n# Answer all the questions\n# 🍪 Enjoy your new project 🍪\ncd new_project\ndocker-compose -f deploy/docker-compose.yml --project-directory . build\ndocker-compose -f deploy/docker-compose.yml --project-directory . up --build\n```\n\nIf you want to install it from sources, try this:\n```shell\npython3 -m pip install poetry\npython3 -m pip install .\npython3 -m fastapi_template\n```\n\nAlso you can use it with docker.\n```bash\ndocker run --rm -it -v "$(pwd):/projects" s3rius/fastapi_template\n```\n\n## Features\n\nOne of the coolest features is that this project is extremely configurable.\nYou can choose between different databases and even ORMs, or\nyou can even generate a project without a database!\nCurrently SQLAlchemy1.4, TortoiseORM, Piccolo and Ormar are supported.\n\nThis project can run as TUI or CLI and has excellent code documentation.\n\nGenerator features:\n- You can choose between GraphQL and REST api;\n- Different databases support;\n- Different ORMs support;\n- Optional migrations for each ORM except raw drivers;\n- Optional redis support;\n- Optional rabbitmq support;\n- different CI\\CD;\n- Optional Kubernetes config generation;\n- Optional Demo routers and models (This helps you to see how project is structured);\n- Pre-commit integration;\n- Generated tests with almost 90% coverage;\n- Tests for the generator itself;\n- Optional Prometheus integration;\n- Optional Sentry integration;\n- Optional Loguru logger;\n- Optional Opentelemetry integration.\n\n\nThis project can handle arguments passed through command line.\n\n```shell\n$ python -m fastapi_template --help\n\nUsage: fastapi_template [OPTIONS]\n\nOptions:\n  -n, --name TEXT                 Name of your awesome project\n  -V, --version                   Prints current version\n  --force                         Owerrite directory if it exists\n  --quite                         Do not ask for features during generation\n  --api-type [rest|graphql]       Select API type for your application\n  --db [none|sqlite|mysql|postgresql]\n                                  Select a database for your app\n  --orm [none|ormar|sqlalchemy|tortoise|psycopg|piccolo]\n                                  Choose Object–Relational Mapper lib\n  --ci [none|gitlab_ci|github]    Select a CI for your app\n  --redis                         Add redis support\n  --rabbit                        Add RabbitMQ support\n  --migrations                    Add Migrations\n  --kube                          Add kubernetes configs\n  --dummy                         Add dummy model\n  --routers                       Add example routers\n  --swagger                       Add self hosted swagger\n  --prometheus                    Add prometheus compatible metrics\n  --sentry                        Add sentry integration\n  --loguru                        Add loguru logger\n  --opentelemetry                 Add opentelemetry integration\n  --traefik                       Adds traefik labels to docker container\n  --kafka                         Add Kafka support\n  --help                          Show this message and exit.\n```\n',
    'author': 'Pavel Kirilin',
    'author_email': 'win10@list.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/s3rius/FastAPI-template',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
