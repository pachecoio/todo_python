from flask import Flask
from todo_python.resources.todos import todo_blueprint

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(todo_blueprint, url_prefix="/api/v1")
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
