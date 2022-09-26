from todo_python.services import UnitOfWork
from todo_python import domain


def create_todo(uow: UnitOfWork, task: str) -> domain.Todo:
    with uow:
        todo = domain.Todo(task)
        uow.todos.save(todo)
        uow.commit()
