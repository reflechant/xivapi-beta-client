from enum import Enum


class Format(str, Enum):
    PNG = "png"

    def __str__(self) -> str:
        return str(self.value)
