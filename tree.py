from node import Node
from game import Game

class Tree:

    def __init__(self, game: Game, maxDepth: int = 20) -> None:
        self.root = Node([], [(0, 0), (0, 1), (0, 2)], 0, -1, 0)
        self.game = game
        self.maxDepth = maxDepth
        self.minDepth = -1
        self.creationRecursive(self.root, 1)
        
        if self.minDepth == -1:
            print(f"No hay solución -> {-1}")
        else:
            self.recorridoPreorden(self.root)
        

    def creationRecursive(self, node: Node, depth: int):
        if depth <= self.maxDepth: 
            if not self.game.isWin(node.rectangle):
                for type in range(5):
                    rectangleM, rotation = self.rectangleMove(type, node.rectangle.copy(), node.rotation)
                    if rectangleM != -1 and self.goodMove(node.move, type):
                        child = Node([], rectangleM, depth + 1, type, rotation)
                        self.creationRecursive(child, depth + 1)
                        node.childs.append(child)
            else:
                self.minDepth = depth


    def rectangleMove(self, type: int, rectangle: list, rotation: int):
        newRectangle = []
        if type == 0:
            #Move up
            for coord in rectangle:
                newRectangle.append((coord[0] - 1, coord[1]))

        elif type == 1:
            #Move Down
            for coord in rectangle:
                newRectangle.append((coord[0] + 1, coord[1]))
            
        elif type == 2:
            #Move Left
            for coord in rectangle:
                newRectangle.append((coord[0], coord[1] - 1))
            
        elif type == 3:
            #Move Right
            for coord in rectangle:
                newRectangle.append((coord[0], coord[1] + 1))
                
        else:
            #Change Orientation
            if rotation == 0:
                newRectangle = [(rectangle[0][0] - 1, rectangle[0][1] + 1), rectangle[1], (rectangle[2][0] + 1, rectangle[2][1] - 1)]
            else:
                newRectangle = [(rectangle[0][0] + 1, rectangle[0][1] - 1), rectangle[1], (rectangle[2][0] - 1, rectangle[2][1] + 1)]

            rotation = (rotation + 1) % 2

        if self.game.correctPlay(newRectangle):
            return newRectangle, rotation
        return -1, rotation
    

    #Esta función sirve para quitar movimiento innecesarios. Por ejemplo, si el turno anterior se movió a la derecha, hacemos
    # que este turno no se pueda mover a la izquierda.
    def goodMove(self, oldType: int, newType: int) -> bool:
        if oldType == 0 and newType == 1:
            return False
        elif oldType == 1 and newType == 0:
            return False
        elif oldType == 2 and newType == 3:
            return False
        elif oldType == 3 and newType == 2:
            return False
        elif oldType == 4 and newType == 4:
            return False
        return True
    
    
    def recorridoPreorden(self, nodo: Node): 
        
        if self.game.isWin(nodo.rectangle) and nodo.depth == self.minDepth:
            nodo.show()
            print(nodo)
            print("ES VICTORIA!!!")
            input("VICTORY")

        for node in nodo.childs:
            self.recorridoPreorden(node)



        