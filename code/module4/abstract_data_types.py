from base import Base
from typing import List


class AbstractDataTypes(Base):
    @staticmethod
    def stack_operations(cmds: List[str]) -> List[int]:
        counter = 1
        ary = []
        for cmd in cmds:
            if cmd in ["push", "enqueue"]:
                ary.append(counter)
                counter += 1
            elif cmd in ["pop", "dequeue"]:
                ary.pop()
                counter -= 1
        return ary

    @staticmethod
    def queue_operations(cmds: List[str]) -> List[int]:
        return AbstractDataTypes.stack_operations(cmds)
