# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['forgeheroku']

package_data = \
{'': ['*']}

install_requires = \
['click>=2.0.0',
 'forge-core>=1.0.0,<2.0.0',
 'gunicorn>=20.1.0,<21.0.0',
 'psycopg2-binary>=2.9.3,<3.0.0']

entry_points = \
{'console_scripts': ['forge-heroku = forgeheroku:cli']}

setup_kwargs = {
    'name': 'forge-heroku',
    'version': '1.0.0',
    'description': 'Work library for Forge',
    'long_description': '# forge-heroku\n\nDeploy a Django project to Heroku with minimal configuration.\n\nThis package is specifically designed to work with the [Forge Heroku Buildpack](https://github.com/forgepackages/heroku-buildpack-forge).\n\n```console\n$ forge heroku\nUsage: forge heroku [OPTIONS] COMMAND [ARGS]...\n\n  Commands for deploying and managing Heroku apps\n\nOptions:\n  --help  Show this message and exit.\n\nCommands:\n  create          Create a new Heroku app with Postgres...\n  pre-deploy      Pre-deploy checks for release process\n  serve           Run a production server using gunicorn\n  set-buildpacks  Automatically determine and set buildpacks\n  shell           Open a remote Django shell\n```\n\n## Default Procfile\n\nWhen you use the Forge buildpack,\nHeroku will automatically set up a `Procfile` for you.\nHere\'s what it does:\n\n```yaml\nweb: forge heroku serve\nrelease: forge heroku pre-deploy\n```\n\nIf you need to customize your `Procfile`, simply add one to your repo!\n\n## Deploy checks\n\nIn the Heroku ["release" phase](https://devcenter.heroku.com/articles/release-phase) we run `manage.py check --deploy --fail-level WARNING` as part of `forge heroku pre-deploy`.\n\n[This runs a number of Django system checks](https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/#run-manage-py-check-deploy) (many related to the settings above) and will prevent deploying your app if any checks fail.\nYou can also [create your own checks](https://docs.djangoproject.com/en/4.1/topics/checks/) that will run during this process.\n\n## Migrations\n\nThe `forge heroku pre-deploy` will also run `manage.py migrate` to ensure that your database is up to date.\n',
    'author': 'Dave Gaeddert',
    'author_email': 'dave.gaeddert@dropseed.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://www.forgepackages.com/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
