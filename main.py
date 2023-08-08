from tree import Tree
from game import Game


if __name__ == "__main__":
    labyrinth = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
                 ["#", ".", ".", ".", "#", ".", ".", ".", "."],
                 [".", ".", ".", ".", "#", ".", ".", ".", "."],
                 [".", "#", ".", ".", ".", ".", ".", "#", "."],
                 [".", "#", ".", ".", ".", ".", ".", "#", "."]
                 ]
    
    game = Game(labyrinth)
    for row in labyrinth:
        print(row)
    print("--------------------------------")
    tree = Tree(game)
    
    