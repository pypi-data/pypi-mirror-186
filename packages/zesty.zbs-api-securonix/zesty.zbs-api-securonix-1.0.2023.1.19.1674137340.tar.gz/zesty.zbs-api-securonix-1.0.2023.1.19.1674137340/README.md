## Description
Zesty Disk API

## Installation
pip install zesty.zbs-api

## Usage
from zesty.zbs-api import *

## Alembic and Postgres Data Models.
For instructions on how to manage the Postgres data model as well as using Alembic to automatically prepare database migrations, please refer to the `README.md` in the `alembic` folder which is located at the root of this repository.

## SQLAlchemy Dependency
Some of the models within this package require SQLAlchemy to be imported. To keep this package light as it's used across many places in our code base, we do not install SQLAlchemy with this package. Thus, if you need to use any of the models that depend on SQLAlchemy, please install the Postgres-Utils package with your requirements.txt.
