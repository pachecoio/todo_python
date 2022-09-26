from todo_python import domain
import pytest


def test_todo_instance():
    todo = domain.Todo("Read 10 pages")
    assert str(todo) == "Read 10 pages"
    assert todo.status == domain.TodoStatus.PENDING
    assert not todo.is_deleted


def test_complete_todo():
    todo = domain.Todo("Read 10 pages")
    todo.complete()
    assert todo.status == domain.TodoStatus.COMPLETED


def test_delete_todo():
    todo = domain.Todo("Read 10 pages")
    todo.delete()
    assert todo.is_deleted


def test_cannot_complete_deleted_todo():
    todo = domain.Todo("Read 10 pages")
    todo.delete()
    assert todo.is_deleted
    with pytest.raises(domain.TodoError) as e:
        todo.complete()

    assert e.value.message == "Cannot complete a deleted todo"

