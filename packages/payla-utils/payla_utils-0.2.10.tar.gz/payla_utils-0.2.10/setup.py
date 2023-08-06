# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['payla_utils',
 'payla_utils.access',
 'payla_utils.logging',
 'payla_utils.management',
 'payla_utils.management.commands',
 'payla_utils.models']

package_data = \
{'': ['*']}

install_requires = \
['Django>=4.0',
 'django-admin-interface==0.24.1',
 'django-ipware>=4.0.0,<5.0.0',
 'python-json-logger>=2.0.0,<3.0.0',
 'sentry-sdk>=1.0',
 'structlog-sentry>=2.0.0,<3.0.0',
 'structlog>=22.3.0,<23.0.0']

setup_kwargs = {
    'name': 'payla-utils',
    'version': '0.2.10',
    'description': 'payla_utils python package',
    'long_description': '# payla_utils python package\n\n## Features\n\n### Structlog config\n\n#### Example, structlog configuration, django\nin django settings.py\n\n    from payla_utils.logging import LoggingConfigurator\n\n    LoggingConfigurator(\n        \'testapp\',\n        log_level=\'INFO\',\n        own_apps=settings.OWN_APPS,\n        setup_logging_dict=True,\n    ).configure_structlog(formatter=\'plain_console\')\n\n\n#### Example, structlog configuration, passing extra loggers names\nin django settings.py\n\n    from payla_utils.logging import LoggingConfigurator\n\n    LoggingConfigurator(\n        \'testapp\',\n        log_level=\'INFO\',\n        own_apps=settings.OWN_APPS,\n        setup_logging_dict=True,\n    ).configure_structlog(formatter=\'plain_console\', extra_loggers_name=[\'mylogger1\', \'mylogger2\'])\n\n\n#### If you want to use structlog in django celery\n\nin celery.py\n\n    from django.conf import settings\n    from payla_utils.logging import LoggingConfigurator\n\n    @signals.setup_logging.connect\n    def receiver_setup_logging(\n        loglevel, logfile, format, colorize, **kwargs\n    ):  # pragma: no cover\n\n        LoggingConfigurator(\n            \'testapp\',\n            log_level=\'INFO\',\n            own_apps=settings.OWN_APPS,\n            setup_logging_dict=True,\n        ).configure_structlog(formatter=\'plain_console\')\n\n#### If you want to use structlog with Sentry\n\nYou will have to set `PaylaLoggingIntegration` in sentry sdk setup\n\n```python\nsentry_sdk.init(\n    # take sentry DSN from environment or add a default value here:\n    dsn=env.str(\'SENTRY_DSN\'),\n    integrations=[DjangoIntegration(), CeleryIntegration(), PaylaLoggingIntegration()],\n    auto_session_tracking=False,\n    traces_sample_rate=0.01,\n    send_default_pii=True,\n    attach_stacktrace=True,\n    request_bodies=\'medium\',\n    release=PROJECT_VERSION,\n    environment=ENVIRONMENT,\n)\n```\n\n### If you want to use a structlog, not Django based project\n\n    from payla_utils.logging import LoggingConfigurator\n\n    LoggingConfigurator(\n        \'testapp\',\n        log_level=\'INFO\',\n        own_apps=[],\n        setup_logging_dict=True,\n    ).configure_structlog(formatter=\'plain_console\')\n\n\n#### How to use generic structured logger:\n\n    logger = structlog.get_logger(__name__)\n    logger.warning("Here is your message", key_1="value_1", key_2="value_2", key_n="value_n")\n\n\n#### Using request middleware to inject request_id and/or trace_id:\n\nThis middleware will inject reqest_id and/or trace_id to all logs producer during a request/response cycle.\n\n    MIDDLEWARE += [\'payla_utils.logging.middlewares.RequestMiddleware\']\n\n- Pass your custom request id header via the PAYLA_UTILS settings: `REQUEST_ID_HEADER`, defaults to `X-Request-ID`\n- Enable tracing (Only supports opentelemetry) via `configure_structlog(tracing_enabled=True)`\n\n[See configuration section](#Configuration-and-settings)\n\n### Why structured logger\n\n- By default, the logging frameworks outputs the traces in plain text and tools like EFK stack or Grafana Loki can’t fully process these traces.\n- Therefore, if we “structure” or send the traces in JSON format directly, all the tools can benefit of.\n- As a developer, it would be nice to be able to filter all logs by a certain customer or transaction.\n- The goal of structured logging is to solve these sorts of problems and allow additional analytics.\n\n\n- When you log something, remember that the actual consumer is the machine Grafana Loki (EFK stack), not only humans.\n- Our generic logger comes with some default context structure, but as you can see, you can introduce new keys.\n- We use structlog as wraper on standard logging library, you can check for more details [structlog](https://www.structlog.org/en/stable/).\n\n\n## Access decorator\n\nTo prohibit access to only internal IPs for a specific view it\'s possible to use the `only_internal_access` decorator.\n\nSERVER_IP is required to be set on payla_utils settings.\n\n[See configuration section](#Configuration-and-settings)\n\nExample usage\n\n```python\n@only_internal_access\ndef test_view(request):\n    return HttpResponse(\'OK\')\n```\nOr inline\n\n```python\npath(\'test/\', only_internal_access(test_view), name="test-view"),\n```\n\n## Management command to init environment\n\nThis management command will init environment based on the current env (local.dev, dev, stage, playground and prod)\n\n- load fixtures on the first run (when the DB is empty)\n- setup custom theme for admin_interface\n- create user when not in prod if `LOCAL_DJANGO_ADMIN_PASSWORD` is set\n\nAPP_NAME and ENVIRONMENT settings are required. [See configuration section](#Configuration-and-settings)\n\n## Configuration and settings\n\nSettings for Payla Utils are all namespaced in the PAYLA_UTILS setting.\nFor example your project\'s `settings.py` file might look like this:\n\n```python\nPAYLA_UTILS = {\n    \'APP_NAME\': \'My App\',\n    # Used for json logging\n    \'MICROSERVICE_NAME: \'myapp\',\n    # dev, stage, prod ...\n    \'ENVIRONMENT\': ENVIRONMENT,\n    \'INITIAL_FIXTURES\': [\n        os.path.join(BASE_DIR, \'testapp\', \'fixtures\', \'users.json\'),\n    ],\n    \'SERVER_IP\': \'192.168.1.4\',\n    \'REQUEST_ID_HEADER\': \'X-Request-ID\',\n    \'RUN_EXTRA_COMMANDS\': [\'loadinitialusers\', \'setup_something\'],\n    \'LOCAL_DJANGO_ADMIN_PASSWORD\': os.environ.get(\'LOCAL_DJANGO_ADMIN_PASSWORD\', \'admin\'),\n    # Only in case you need to change the defaults\n    \'ENV_THEMES\': {\n        \'local.dev\': {\n            ...\n        },\n        \'dev\': {\n            ...\n        },\n        \'stage\': {\n            ...\n        },\n        \'playground\': {\n            ...\n        },\n        \'prod\': {\n            ...\n        },\n    }\n}\n```\n\n## Payla Generic model\n\n### Usage\n\n    from payla_utils.models import PaylaModel\n\n    class MyModel(PaylaModel):\n        ...\n\nThis model will add the following fields:\n\n- `created_at` - datetime\n- `modified_at` - datetime\n\nIt has also a QuerySet that will add the following methods:\n\n- `get_or_none` - returns the object or None\n',
    'author': 'Payla Services',
    'author_email': 'tools@payla.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4',
}


setup(**setup_kwargs)
