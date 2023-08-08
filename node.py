

class Node:

    def __init__(self, childs: list, rectangle: list, depth: int, move: int) -> None:
        self.childs = childs
        self.rectangle = rectangle
        self.depth = depth
        self.move = move


    def show(self) -> str:
        labyrinth = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["#", ".", ".", ".", "#", ".", ".", ".", "."],
                 [".", ".", ".", ".", "#", ".", ".", ".", "."],
                 [".", "#", ".", ".", ".", ".", ".", "#", "."],
                 [".", "#", ".", ".", ".", ".", ".", "#", "."]
                 ]
        for coord in self.rectangle:
            labyrinth[coord[0]][coord[1]] = 'X'

        
        print(f"PROFUNDIDAD -> {self.depth}")
        for row in labyrinth:
            print(row)

        print("--------------------------------")