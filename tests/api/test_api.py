from flask import Flask
from todo_python.app import create_app
import pytest
from todo_python import domain
from todo_python.services.unitofwork import UnitOfWork

@pytest.fixture
def mock_default_uow(session_factory, mocker):
    uow = UnitOfWork(session_factory)
    mocker.patch("todo_python.resources.todos.get_default_uow", lambda: uow)


@pytest.fixture
def todo_ids(session):
    todo1 = domain.Todo("simple todo 1")
    todo2 = domain.Todo("simple todo 2")
    session.add(todo1)
    session.add(todo2)
    session.commit()
    return [todo1.id, todo2.id]


def test_app_instance():
    app = create_app()
    assert type(app) == Flask


def test_app_client():
    app = create_app()
    test_client = app.test_client()
    assert test_client


@pytest.mark.usefixtures("mock_default_uow", "session")
def test_get_todos(test_client, todo_ids):
    res = test_client.get("/api/v1/todos")
    assert res.status_code == 200
    assert len(res.json["items"]) == 2
    ids_found = [item.get("id") for item in res.json["items"]]
    for id in todo_ids:
        assert id in ids_found


@pytest.mark.usefixtures("mock_default_uow")
def test_create_todo(test_client, session):
    res = test_client.post("/api/v1/todos", json={"title": "sample todo"})
    assert res.status_code == 201

    assert res.json["title"] == "sample todo"


@pytest.mark.usefixtures("mock_default_uow", "session")
def test_complete_todo(test_client, session, todo_ids):
    todo_id = todo_ids[0]

    res = test_client.post(f"/api/v1/todos/{todo_id}/complete")
    assert res.status_code == 204

    todo = session.query(domain.Todo).get(todo_id)
    assert todo.status == domain.TodoStatus.COMPLETED


@pytest.mark.usefixtures("mock_default_uow")
def test_delete_todo(test_client, session, todo_ids):
    todo_id = todo_ids[0]

    res = test_client.delete(f"/api/v1/todos/{todo_id}")
    assert res.status_code == 204

    todo = session.query(domain.Todo).get(todo_id)
    assert todo.is_deleted

