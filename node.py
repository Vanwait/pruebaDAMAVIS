
import copy
class Node:

    def __init__(self, childs: list, rectangle: list, depth: int, move: int, rotation: int, lab: list) -> None:
        self.childs = childs
        self.rectangle = rectangle
        self.depth = depth
        self.move = move
        self.rotation = rotation # 0 horizontal, 1 vertical
        self.lab = lab

    # Hace un print de la información de los nodos, esta función ya no es ñutil, me ha servido durante el desarrollo
    def show(self) -> str:
        labyrinth = copy.deepcopy(self.lab)
        for coord in self.rectangle:
            labyrinth[coord[0]][coord[1]] = 'X'

        
        print(f"PROFUNDIDAD -> {self.depth}")
        for row in labyrinth:
            print(row)

        print("--------------------------------")