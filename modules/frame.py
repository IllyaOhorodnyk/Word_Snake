# організувати фнцію для випадкового вибору незанятих клітинок
# механізм для статусу загаданого слова
from abc import ABC, abstractmethod, abstractproperty


class Block(ABC):
    pass

class Chunk(Block):
    pass


class Wall(Block):
    pass

class Food(Block):
    pass

class Head(Chunk):
    pass

class Table:
    pass
