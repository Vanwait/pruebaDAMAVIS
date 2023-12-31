from tree import Tree
from game import Game

def typeLabyrinth(type: int):
    if type == 0:
        labyrinth = [
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                ["#", ".", ".", ".", "#", ".", ".", ".", "."],
                [".", ".", ".", ".", "#", ".", ".", ".", "."],
                [".", "#", ".", ".", ".", ".", ".", "#", "."],
                [".", "#", ".", ".", ".", ".", ".", "#", "."]
                 ]

    elif type == 1:
        labyrinth = [
                [".", ".", ".", ".", ".", ".", ".", ".", "."],
                ["#", ".", ".", ".", "#", ".", ".", "#", "."],
                [".", ".", ".", ".", "#", ".", ".", ".", "."],
                [".", "#", ".", ".", ".", ".", ".", "#", "."],
                [".", "#", ".", ".", ".", ".", ".", "#", "."]
                ]

    elif type == 2:
        labyrinth = [
                [".", ".", "."],
                [".", ".", "."],
                [".", ".", "."]
                 ]

    else:
        labyrinth = [
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", "#", ".", ".", ".", ".", "#", ".", ".", "."],
                [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", "#", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", "#", ".", ".", ".", "#", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", "#", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
                [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
                 ]
    
    return labyrinth


if __name__ == "__main__":
    for type in range(4):
        with open(f"resultados_Test{type + 1}.txt", 'w', encoding='UTF-8') as f:
            f.write(f"------------- Test {type + 1} -------------\n")
            labyrinth = typeLabyrinth(type)
            game = Game(labyrinth)
            for row in labyrinth:
                f.write(str(row))
                f.write("\n")
            f.write("--------------------------------\n")
            tree = Tree(game)

            resultado = tree.minDepth
            if resultado == 10000:
                resultado = -1

            f.write(f"El resultado es -> {resultado} \n")
            del(tree)
            del(game)
            f.write("\n")
    
    