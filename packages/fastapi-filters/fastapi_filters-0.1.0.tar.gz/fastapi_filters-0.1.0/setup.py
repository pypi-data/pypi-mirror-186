# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_filters', 'fastapi_filters.ext']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.89.1,<0.90.0',
 'pydantic>=1.10.4,<2.0.0',
 'typing-extensions>=4.4.0,<5.0.0']

extras_require = \
{'sqlalchemy': ['sqlalchemy>=1.4.46,<2.0.0']}

setup_kwargs = {
    'name': 'fastapi-filters',
    'version': '0.1.0',
    'description': 'fastapi-filters',
    'long_description': '<h1 align="center">\n<img alt="logo" src="https://raw.githubusercontent.com/uriyyo/fastapi-filters/main/logo.png">\n</h1>\n\n<div align="center">\n<img alt="license" src="https://img.shields.io/badge/License-MIT-lightgrey">\n<img alt="test" src="https://github.com/uriyyo/fastapi-filters/workflows/Test/badge.svg">\n<img alt="codecov" src="https://codecov.io/gh/uriyyo/fastapi-filters/branch/main/graph/badge.svg?token=QqIqDQ7FZi">\n<a href="https://pepy.tech/project/fastapi-filters"><img alt="downloads" src="https://pepy.tech/badge/fastapi-filters"></a>\n<a href="https://pypi.org/project/fastapi-filters"><img alt="pypi" src="https://img.shields.io/pypi/v/fastapi-filters"></a>\n<img alt="black" src="https://img.shields.io/badge/code%20style-black-000000.svg">\n</div>\n\n## Introduction\n\n`fastapi-filters` is a library that provides filtering/sorting feature for [FastAPI](https://fastapi.tiangolo.com/)\napplications.\n\n----\n\n## Installation\n\n```bash\npip install fastapi-filters\n```\n\n## Quickstart\n\nTo create filters you need either define them manually using `create_filters` function or automatically generate them\nbased on model using `create_filters_from_model` function.\n\n```py\nfrom typing import List\n\nfrom fastapi import FastAPI, Depends\nfrom pydantic import BaseModel, Field\n\n# import all you need from fastapi-filters\nfrom fastapi_filters import create_filters, create_filters_from_model, FilterValues\n\napp = FastAPI()  # create FastAPI app\n\n\nclass UserOut(BaseModel):  # define your model\n    name: str = Field(..., example="Steve")\n    surname: str = Field(..., example="Rogers")\n    age: int = Field(..., example=102)\n\n\n@app.get("/users")\nasync def get_users_manual_filters(\n    # manually define filters\n    filters: FilterValues = Depends(create_filters(name=str, surname=str, age=int)),\n) -> List[UserOut]:\n    pass\n\n\n@app.get("/users")\nasync def get_users_auto_filters(\n    # or automatically generate filters from pydantic model\n    filters: FilterValues = Depends(create_filters_from_model(UserOut)),\n) -> List[UserOut]:\n    pass\n```\n\nCurrently, `fastapi-filters` supports `SQLAlchemy` integration.\n\n```py\nfrom fastapi_filters.ext.sqlalchemy import apply_filters\n\n\n@app.get("/users")\nasync def get_users(\n    db: AsyncSession = Depends(get_db),\n    filters: FilterValues = Depends(create_filters_from_model(UserOut)),\n) -> List[UserOut]:\n    query = apply_filters(select(UserOut), filters)\n    return (await db.scalars(query)).all()\n```',
    'author': 'Yurii Karabas',
    'author_email': '1998uriyyo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/uriyyo/fastapi-filters',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
