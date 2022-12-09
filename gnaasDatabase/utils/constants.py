from enum import Enum, auto

class Leadership(Enum):
    def _get_next_value(name, start, count, last_value):
        return name.lower()

    NATIONAL = auto()
    UNION = auto()
    ZONE = auto()
    FELLOWSHIP = auto()