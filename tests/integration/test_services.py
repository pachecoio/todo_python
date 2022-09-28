import pytest

from todo_python import domain
from todo_python.services import UnitOfWork, handlers


@pytest.fixture
def todo_id(session):
    todo = domain.Todo("sample")
    session.add(todo)
    session.commit()
    todo_id = todo.id
    return todo_id


def test_create_todo(session_factory, session):
    uow = UnitOfWork(session_factory)
    todo = handlers.create_todo(uow, "Skate 1h")

    assert todo.title
    todos = uow.todos.filter()
    assert todos.count() == 1

    todo = todos.first()
    assert str(todo) == "Skate 1h"


def test_complete_todo(todo_id, session_factory, session):
    uow = UnitOfWork(session_factory)
    handlers.complete_todo(uow, todo_id)

    todo = session.query(domain.Todo).get(todo_id)
    assert todo.status == domain.TodoStatus.COMPLETED


def test_delete_todo(todo_id, session_factory, session):
    uow = UnitOfWork(session_factory)
    handlers.delete_todo(uow, todo_id)

    todo = session.query(domain.Todo).get(todo_id)
    assert todo.is_deleted
