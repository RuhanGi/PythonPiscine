import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates 15 random letters"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Your docstring for DataClass"""
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Your docstring for Post Initialization"""
        self.login = (self.name[0] + self.surname).capitalize()
        self.id = generate_id()
