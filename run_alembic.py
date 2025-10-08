from alembic.config import Config
from alembic.config import CommandLine

if __name__ == "__main__":
    CommandLine().main()

from alembic import command

# Caminho para o arquivo alembic.ini
alembic_cfg = Config("alembic.ini")

# Gera uma nova revisão
command.revision(alembic_cfg, message="init_db", autogenerate=True)
