### Incorporating alembic to your SQLAlchemy project

Youtube tutorial: https://www.youtube.com/watch?v=cWdMPIVEIW0

## Install alembic

$ python3 -m venv env

$ source env/bin/activate

$ pip install alembic

$ alembic init migrations

## Configure almebic

* Edit migrations/env.py
* Edit migrations/alembic.ini

## Use alembic

$ alembic revision -m "Create initial user table" --autogenerate

$ alembic upgrade head

$ alembic revision -m "Add password to user" --autogenerate

$ alembic history

$ alembic downgrade -1 

$ alembic revision -m 'my manual change'