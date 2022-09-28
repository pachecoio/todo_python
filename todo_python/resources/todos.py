from flask import Blueprint, jsonify, request
from todo_python.utils import get_default_uow
from todo_python import domain
from todo_python.services import handlers


todo_blueprint = Blueprint("todos", __name__)


@todo_blueprint.route("/todos", methods=["GET"])
def get_all_todos():
    """
    Get all the todos.
    """
    uow = get_default_uow()
    with uow:
        todos = uow.todos.filter()

        return jsonify({
            "items": [{
                "id": todo.id,
                "title": todo.title,
                "status": str(todo.status),
            } for todo in todos]
        })


@todo_blueprint.route("/todos", methods=["POST"])
def create_todo():
    """
    Create a new todo.
    """
    title = request.json.get("title")
    uow = get_default_uow()
    
    todo = handlers.create_todo(uow, title)

    return jsonify({
        "id": todo.id,
        "title": todo.title,
    }), 201


@todo_blueprint.route("/todos/<int:todo_id>/complete", methods=["POST"])
def complete_todo(todo_id: int):
    uow = get_default_uow()
    handlers.complete_todo(uow, todo_id)

    return "", 204


@todo_blueprint.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id: int):
    uow = get_default_uow()
    handlers.delete_todo(uow, todo_id)
    return "", 204

