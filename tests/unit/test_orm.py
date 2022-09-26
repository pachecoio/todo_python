from todo_python import domain


def test_create_todo(session):
    todo = domain.Todo("Skate 1h")
    session.add(todo)
    session.commit()
    session.flush()

    todos = session.query(domain.Todo).all()
    assert len(todos) == 1