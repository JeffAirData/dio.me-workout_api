import sys
import os

# Caminho absoluto para a raiz do projeto
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Adiciona a raiz ao sys.path
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
from logging.config import fileConfig

from sqlalchemy.engine import Connection
from sqlalchemy import engine_from_config, pool

from alembic import context
from workoutapi.contrib.models import BaseModel
from workoutapi.contrib.repository.models import *

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = BaseModel.metadata

def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        do_run_migrations(connection)

    connectable.dispose()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
