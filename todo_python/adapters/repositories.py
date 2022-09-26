from dataclasses import dataclass
from sqlalchemy.orm import Session
from todo_python import domain


@dataclass
class TodoRepository:
    session: Session

    def save(self, entity: domain.Todo):
        self.session.add(entity)

    
    def commit(self):
        self.session.commit()


    def filter(self, **kwargs):
        return self.session.query(domain.Todo).filter_by(**kwargs)
