from todo_python.services import UnitOfWork
from todo_python import domain


def create_todo(uow: UnitOfWork, task: str) -> domain.Todo:
    with uow:
        todo = domain.Todo(task)
        uow.todos.save(todo)
        uow.commit()
    return todo


def complete_todo(uow, todo_id: int):
    with uow:
        todo = uow.todos.get(todo_id)
        todo.complete()
        uow.commit()


def delete_todo(uow, todo_id: int):
    with uow:
        todo = uow.todos.get(todo_id)
        todo.delete()
        uow.commit()
