# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['apscheduler_di']

package_data = \
{'': ['*']}

install_requires = \
['APScheduler>=3.8.1,<4.0.0', 'rodi>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'apscheduler-di',
    'version': '0.1.0',
    'description': 'Lightweight and beneficial Dependency Injection plugin for apscheduler ',
    'long_description': '# Implementation of dependency injection for `apscheduler`\n[![PyPI version](https://img.shields.io/pypi/v/apscheduler-di.svg)](https://pypi.org/project/apscheduler-di/)[![codecov](https://codecov.io/gh/GLEF1X/apscheduler-di/branch/master/graph/badge.svg?token=X71JFESNL5)](https://codecov.io/gh/GLEF1X/apscheduler-di)[![Downloads](https://pepy.tech/badge/apscheduler-di/week)](https://pepy.tech/project/apscheduler-di)\n\n### Motivation:\n\n* `apscheduler-di` solves the problem since `apscheduler` doesn\'t support Dependency Injection\n  natively, and it\'s real problem for developers to pass on complicated objects to jobs without\n  corruptions\n\n## Features:\n\n* Supports type hints ([PEP 561](https://www.python.org/dev/peps/pep-0561/))\n* Extend `apscheduler` and provide handy aliases for events(such as `on_startup`, `on_shutdown` and\n  etc)\n* Provide an opportunity to implement [Dependency Inversion](https://en.wikipedia.org/wiki/Dependency_inversion_principle) SOLID principle\n\n"Under the hood" `apscheduler-di` just\nimplements [Decorator](https://en.wikipedia.org/wiki/Decorator_pattern) pattern and wraps up the\nwork of native `BaseScheduler` using [rodi](https://github.com/Neoteroi/rodi) lib\n\n### Quick example:\n\n```python\nimport os\nfrom typing import Dict\n\nfrom apscheduler.jobstores.redis import RedisJobStore\nfrom apscheduler.schedulers.blocking import BlockingScheduler\n\nfrom apscheduler_di import ContextSchedulerDecorator\n\n# pip install redis\njob_stores: Dict[str, RedisJobStore] = {\n    "default": RedisJobStore(\n        jobs_key="dispatched_trips_jobs", run_times_key="dispatched_trips_running"\n    )\n}\n\n\nclass Tack:\n\n    def tack(self):\n        print("Tack!")\n\n\ndef tick(tack: Tack, some_argument: int):\n    print(tack)\n\n\ndef main():\n    scheduler = ContextSchedulerDecorator(BlockingScheduler(jobstores=job_stores))\n    scheduler.ctx.add_instance(Tack(), Tack)\n    scheduler.add_executor(\'processpool\')\n    scheduler.add_job(tick, \'interval\', seconds=3, kwargs={"some_argument": 5})\n    print(\'Press Ctrl+{0} to exit\'.format(\'Break\' if os.name == \'nt\' else \'C\'))\n\n    try:\n        scheduler.start()\n    except (KeyboardInterrupt, SystemExit):\n        pass\n\n\nif __name__ == \'__main__\':\n    main()\n\n```\n',
    'author': 'Gleb Garanin',
    'author_email': 'glebgar567@gmail.com',
    'maintainer': 'GLEF1X',
    'maintainer_email': 'glebgar567@gmail.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
