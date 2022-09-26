import os
from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    String,
    Integer,
    orm,
    Table,
    Enum,
)
from todo_python import domain

metadata = MetaData()

def get_database_uri() -> str:
    host = os.environ.get("POSTGRES_HOST", "agenda-db")
    port = 5432
    username = os.environ.get("POSTGRES_USER", "root")
    password = os.environ.get("POSTGRES_PASSWORD", "root")
    db_name = os.environ.get("POSTGRES_DB", "agenda")
    return f"postgresql://{username}:{password}@{host}:{port}/{db_name}"

DEFAULT_ENGINE = create_engine(get_database_uri())

DEFAULT_SESSION_FACTORY = orm.sessionmaker(
    bind=DEFAULT_ENGINE
)

todo_table = Table(
    "todos",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String, nullable=False),
    Column("status", Enum(domain.TodoStatus), nullable=False),
    Column("is_deleted", String, nullable=True, default=False),
)


def start_mappers():
    todo_mapper = orm.mapper(domain.Todo, todo_table)
