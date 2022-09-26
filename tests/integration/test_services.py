from todo_python.adapters.repositories import TodoRepository
from todo_python.services import UnitOfWork, handlers


def test_create_todo(session_factory, session):
    uow = UnitOfWork(session_factory)
    handlers.create_todo(uow, "Skate 1h")

    todos = uow.todos.filter()
    assert todos.count() == 1

    todo = todos.first()
    assert str(todo) == "Skate 1h"
    