# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastramqpi']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.88.0,<0.89.0',
 'gql>=3.4.0,<4.0.0',
 'more-itertools>=9.0.0,<10.0.0',
 'prometheus-fastapi-instrumentator>=5.9.1,<6.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'ra-utils>=1.7.1,<2.0.0',
 'raclients>=3.0.3,<4.0.0',
 'ramqp>=6.6.2,<7.0.0',
 'structlog>=22.3.0,<23.0.0']

setup_kwargs = {
    'name': 'fastramqpi',
    'version': '1.3.1',
    'description': 'Rammearkitektur AMQP framework (FastAPI + RAMQP)',
    'long_description': '<!--\nSPDX-FileCopyrightText: 2021 Magenta ApS <https://magenta.dk>\nSPDX-License-Identifier: MPL-2.0\n-->\n\n# FastRAMQPI\n\nFastRAMQPI is an opinionated library for FastAPI and RAMQP.\n\nIt is implemented as a thin wrapper around `FastAPI` and `RAMQP`.\nIt is very MO specific.\n\n## Usage\n\n```python\nfrom pydantic import BaseSettings\nfrom fastramqpi import FastRAMQPI\nfrom fastramqpi import FastRAMQPISettings\n\n\nclass Settings(BaseSettings):\n    class Config:\n        frozen = True\n        env_nested_delimiter = "__"\n\n    fastramqpi: FastRAMQPISettings = Field(\n        default_factory=FastRAMQPISettings,\n        description="FastRAMQPI settings"\n    )\n\n    # All your program settings hereunder...\n\n\nfastapi_router = APIRouter()\n\n@fastapi_router.post("/trigger/all")\nasync def update_all(request: Request) -> dict[str, str]:\n    context: dict[str, Any] = request.app.state.context\n    graphql_session = context["grapqh_session"]\n    program_settings = context["user_context"]["settings"]\n    ...\n    return {"status": "OK"}\n\n\namqp_router = MORouter()\n\n@amqp_router.register("*.*.*")\nasync def listen_to_all(context: dict, payload: PayloadType) -> None:\n    graphql_session = context["grapqh_session"]\n    program_settings = context["user_context"]["settings"]\n    ...\n\n\ndef create_fastramqpi(**kwargs: Any) -> FastRAMQPI:\n    settings = Settings(**kwargs)\n    fastramqpi = FastRAMQPI(\n        application_name="orggatekeeper", settings=settings.fastramqpi\n    )\n    fastramqpi.add_context(settings=settings)\n\n    # Add our AMQP router(s)\n    amqpsystem = fastramqpi.get_amqpsystem()\n    amqpsystem.router.registry.update(amqp_router.registry)\n\n    # Add our FastAPI router(s)\n    app = fastramqpi.get_app()\n    app.include_router(fastapi_router)\n\n    return fastramqpi\n\n\ndef create_app(**kwargs: Any) -> FastAPI:\n    fastramqpi = create_fastramqpi(**kwargs)\n    return fastramqpi.get_app()\n```\n\n### Metrics\nFastRAMQPI Metrics are exported via `prometheus/client_python` on the FastAPI\'s `/metrics`.\n\n## Development\n\n### Prerequisites\n\n- [Poetry](https://github.com/python-poetry/poetry)\n\n### Getting Started\n\n1. Clone the repository:\n```\ngit clone git@git.magenta.dk:rammearkitektur/FastRAMQPI.git\n```\n\n2. Install all dependencies:\n```\npoetry install\n```\n\n3. Set up pre-commit:\n```\npoetry run pre-commit install\n```\n\n### Running the tests\n\nYou use `poetry` and `pytest` to run the tests:\n\n`poetry run pytest`\n\nYou can also run specific files\n\n`poetry run pytest tests/<test_folder>/<test_file.py>`\n\nand even use filtering with `-k`\n\n`poetry run pytest -k "Manager"`\n\nYou can use the flags `-vx` where `v` prints the test & `x` makes the test stop if any tests fails (Verbose, X-fail)\n\n## Authors\n\nMagenta ApS <https://magenta.dk>\n\n## License\n\nThis project uses: [MPL-2.0](LICENSES/MPL-2.0.txt)\n\nThis project uses [REUSE](https://reuse.software) for licensing.\nAll licenses can be found in the [LICENSES folder](LICENSES/) of the project.\n',
    'author': 'Magenta ApS',
    'author_email': 'info@magenta.dk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://magenta.dk/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
