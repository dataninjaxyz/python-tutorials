Generic single-database configuration.

$ alembic init

$ alembic revision -m "Create initial user table" --autogenerate

$ alembic upgrade head

$ alembic revision -m "Add password to user" --autogenerate

$ alembic history

$ alembic downgrade -1 

$ alembic revision -m 'my manual change'