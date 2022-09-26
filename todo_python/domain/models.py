from dataclasses import dataclass
import enum

class TodoStatus(enum.Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"


@dataclass
class TodoError(Exception):
    message: str = "An error occurred"


@dataclass
class Todo:
    title: str
    status: TodoStatus = TodoStatus.PENDING
    is_deleted: bool = False

    def __str__(self):
        return self.title

    
    def complete(self):
        if self.is_deleted:
            raise TodoError("Cannot complete a deleted todo")
        self.status = TodoStatus.COMPLETED

    
    def delete(self):
        self.is_deleted = True
