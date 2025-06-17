from base import Base

class Subtasks(Base):
    def __init__(self, value: str):
        self.value = value

    @staticmethod
