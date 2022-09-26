from todo_python import domain
from todo_python.adapters.repositories import TodoRepository


def test_todo_repository(session):
    repo = TodoRepository(session)
    repo.save(domain.Todo("Skate 1h"))
    repo.commit()

    todos = repo.filter()

    assert todos.count() == 1
    todo = todos.first()
    assert str(todo) == "Skate 1h"
