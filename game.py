
class Game:

    def __init__(self, labyrinth: list) -> None:
        self.labyrinth = labyrinth 


    def correctPlay(self, rectangle: list) -> bool:
        for coord in rectangle:
            if coord[0] < 0 or coord[1] < 0 or coord[0] >= len(self.labyrinth) or coord[1] >= len(self.labyrinth[coord[0]]):
                return False
            
            elif self.labyrinth[coord[0]][coord[1]] == '#':
                return False
        return True
    

    def isWin(self, rectangle: list) -> bool:
        for coord in rectangle:
            if (coord[0] == (len(self.labyrinth) - 1)) and coord[1] == (len(self.labyrinth[(len(self.labyrinth) - 1)]) - 1):
                return True
        return False