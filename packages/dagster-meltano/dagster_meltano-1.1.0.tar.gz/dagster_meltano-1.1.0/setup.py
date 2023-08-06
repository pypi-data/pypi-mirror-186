# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dagster_meltano', 'dagster_meltano.log_processing']

package_data = \
{'': ['*']}

install_requires = \
['dagster>=1.0']

setup_kwargs = {
    'name': 'dagster-meltano',
    'version': '1.1.0',
    'description': 'A dagster plugin that allows you to run your Meltano project inside Dagster.',
    'long_description': '# Dagster-meltano\n\nA dagster plugin that allows you to run Meltano using Dagster.\n\n[![Downloads](https://pepy.tech/badge/dagster-meltano/month)](https://pepy.tech/project/dagster-meltano)\n\n## Installation\n\nYou can install using `pip install dagster-meltano`.\n\n## Examples\n\nAn example of automatically loading all jobs and schedules from your Meltano project.\n\n```python\nfrom dagster import repository\nfrom dagster_meltano import load_jobs_from_meltano_project\n\nmeltano_jobs = load_jobs_from_meltano_project("<path-to-meltano-root>")\n\n@repository\ndef repository():\n    return [meltano_jobs]\n```\n\nAn example of running a abitrary `meltano run` command.\n\n```python\nfrom dagster import repository, job\nfrom dagster_meltano import meltano_resource, meltano_run_op\n\n@job(resource_defs={"meltano": meltano_resource})\ndef meltano_run_job():\n    tap_done = meltano_run_op("tap-1 target-1")()\n    meltano_run_op("tap-2 target-2")(tap_done)\n\n@repository()\ndef repository():\n    return [meltano_run_job]\n```\n\nYou can inject Meltano config with the following Dagster config.\n\n```yaml\nops:\n  tap_smoke_test_target_jsonl:\n    config:\n      env:\n        TAP_SMOKE_TEST_STREAMS: \'[{"stream_name": "new-stream", "input_filename": "demo.json"}]\'\n```\n\n## Development using VSCode\n\n1. Open this repository in Visual Studio Code.\n2. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) plugin for Visual Studio Code.\n3. Go to the example Meltano project root `cd meltano_project`\n4. Install all plugins `meltano install`\n5. Start dagit `meltano invoke dagster:start`\n6. Visit `localhost:3000` to access Dagit.\n',
    'author': 'Jules Huisman',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
