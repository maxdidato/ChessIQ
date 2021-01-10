from enum import Enum


class Color(Enum):
    WHITE = 'grey'
    BLACK = 'black'
    DARK = 'brown'
    LIGHT = 'beige'

    @classmethod
    def from_index(cls, index):
        if index % 2 == 0:
            return cls.DARK
        else:
            return cls.LIGHT
