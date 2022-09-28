from typing import Callable
from todo_python.adapters.orm import DEFAULT_SESSION_FACTORY
from todo_python.adapters.repositories import TodoRepository

class UnitOfWork:
    def __init__(self, session_factory: Callable = DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.todos = TodoRepository(self.session)

    def __exit__(self, *args):
        self.session.expunge_all()
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()