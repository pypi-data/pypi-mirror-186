# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['flowmancer',
 'flowmancer.executors',
 'flowmancer.jobspecs',
 'flowmancer.loggers',
 'flowmancer.managers',
 'flowmancer.observers',
 'flowmancer.observers.notifications',
 'flowmancer.tasks',
 'flowmancer.typedefs']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'pyaml-env>=1.1.4,<2.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'rich>=12.0.0,<13.0.0',
 'tqdm>=4.62.3,<5.0.0']

setup_kwargs = {
    'name': 'flowmancer',
    'version': '0.4.9',
    'description': 'The Python Thing-Doer',
    'long_description': '# Flowmancer\n\n[![pypi-version](https://img.shields.io/pypi/v/flowmancer?style=flat-square)](https://pypi.org/project/flowmancer)\n[![python-version](https://img.shields.io/badge/dynamic/json?query=info.requires_python&label=python&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fflowmancer%2Fjson&style=flat-square)](https://pypi.org/project/flowmancer)\n[![license](https://img.shields.io/github/license/natsunlee/flowmancer?style=flat-square)](LICENSE)\n[![circle-ci](https://img.shields.io/circleci/build/github/natsunlee/flowmancer?style=flat-square)](https://app.circleci.com/pipelines/github/natsunlee/flowmancer)\n[![coveralls](https://img.shields.io/coveralls/github/natsunlee/flowmancer?style=flat-square)](https://coveralls.io/github/natsunlee/flowmancer?branch=main)\n[![pypi-downloads](https://img.shields.io/pypi/dm/flowmancer?style=flat-square)](https://pypistats.org/packages/flowmancer)\n[![Ko-Fi](https://img.shields.io/badge/Support%20Me%20On%20Ko--fi-F16061?style=flat-square&logo=ko-fi&logoColor=white)](https://ko-fi.com/natsunlee)\n\nFlowmancer aims to help you do *things* in a sequential or parallel manner. It enables you to write tasks in Python, describe their order, then execute them with as little effort as possible.\n\nBut why do I need this? Couldn\'t I just write my own Python code to do *stuff*?\n\nYou certainly could!\n\nThough Flowmancer provides gives you a head-start to building your custom processes with optional add-ons for logging, checkpoint/restarts in the event of failures, or even custom task observers to do...things while your things do things!\n\n## Installation\nSimply install the `flowmancer` package with:\n```bash\npip install flowmancer\n```\n\nNOTE: `flowmancer` supports only Python 3.6 and higher.\n\n## Usage\nLet\'s assume you have a new project with a basic structure like so:\n```\nmy_project\n├─ job.yaml\n├─ main.py\n└─ tasks/\n   └─ mytasks.py\n```\n\nTo use `flowmancer`, you\'ll need to provide a few things:\n* `Task` implementations (`mytasks.py`)\n* A job YAML file (`job.yaml`)\n* Your main/driver code (`main.py`)\n\n### Tasks\nA `flowmancer` task is simply a class that extends the `Task` abstract class, which, at minimum requires that the `run` method be implemented:\n```python\nfrom flowmancer import Task\nimport time\n\nclass WaitAndSucceed(Task):\n    def run(self):\n        self.logger.info("Starting up and sleeping for 5 seconds!")\n        time.sleep(5)\n        self.logger.info("Done!")\n\nclass FailImmediately(Task):\n    def run(self):\n        raise RuntimeError("Let this be caught by Flowmancer")\n```\n\nBeing an extension of the `Task` you\'ll have a few features available, however, in the above example we only use the `self.logger`. This will write the log message to any configured logging system (zero or more loggers may be defined).\n\n### Job YAML File\nThis file describes what code to run, in what order, as well as additional add-ons to supplement the job during execution:\n```yaml\nversion: 0.1\n\nname: my_project\n\n# Make sure the tasks directory is in the PYTHONPATH\npypath:\n  - ./tasks\n\nloggers:\n  # Assign only a file logger for this job\n  file-logger:\n    module: flowmancer.loggers.file\n    logger: FileLogger\n    kwargs:\n      log_dir: ./logs\n      retention_days: 0\n\nobservers:\n  # Saves state of the job in case of failures\n  # to allow restart from point-of-failure\n  checkpoint:\n    module: flowmancer.observers.checkpoint\n    observer: Checkpoint\n    kwargs:\n      checkpoint_name: my_project\n      checkpoint_dir: ./checkpoint\n  # Show progress bar on STDOUT to see job progress\n  progress-bar:\n    module: flowmancer.observers.progressbar\n    observer: RichProgressBar\n\ntasks:\n  # No dependency - run right away\n  succeed-task-a:\n    module: mytasks\n    task: WaitAndSucceed\n\n  # No dependency - run right away\n  succeed-task-b:\n    module: mytasks\n    task: WaitAndSucceed\n\n  # Only run if prior 2 tasks complete successfully\n  final-fail-task:\n    module: mytasks\n    task: FailImmediately\n    dependencies:\n      - succeed-task-a\n      - succeed-task-b\n```\n\n### Driver\nThe driver is super simple and simply requires running an instance of `Flowmancer`\n```python\nimport sys\nfrom flowmancer import Flowmancer\n\nif __name__ == \'__main__\':\n    ret = Flowmancer("./job.yaml").start()\n    sys.exit(ret)\n```\n\n### Executing the Job\n```bash\npython main.py\n```\n\nTo run from point-of-failure (if any), if Checkpoint observer is enabled:\n```bash\npython main.py -r\n```\nIf no prior failure is detected, the job will start as if no `-r` flag were given.',
    'author': 'Nathan Lee',
    'author_email': 'lee.nathan.sh@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
