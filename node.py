

class Node:

    def __init__(self, childs: list, rectangle: list, depth: int, move: int) -> None:
        self.childs = childs
        self.rectangle = rectangle
        self.depth = depth
        self.move = move