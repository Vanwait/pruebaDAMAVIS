
class Game:

    def __init__(self, labyrinth: list) -> None:
        self.labyrinth = labyrinth
        self.win0 = []
        self.win1 = []
        self.posWinning()


    def correctPlay(self, rectangle: list) -> bool:
        for coord in rectangle:
            if coord[0] < 0 or coord[1] < 0 or coord[0] >= len(self.labyrinth) or coord[1] >= len(self.labyrinth[coord[0]]):
                return False
            
            elif self.labyrinth[coord[0]][coord[1]] == '#':
                return False
        return True
    

    def isWin(self, rectangle: list) -> bool:
        """for coord in rectangle:
            if (coord[0] == (len(self.labyrinth) - 1)) and coord[1] == (len(self.labyrinth[(len(self.labyrinth) - 1)]) - 1):
                return True
        return False"""

        cent = False
        for coord in self.win0:
            cent = True
            if coord not in rectangle:
                cent = False
                break

        if not cent:
            for coord in self.win1:
                if coord not in rectangle:
                    return False
        return True
        
    

    def posWinning(self):
        
        for cont in range(len(self.labyrinth[len(self.labyrinth) - 1]) - 1, len(self.labyrinth[len(self.labyrinth) - 1]) - 4, -1):
            self.win0.append((len(self.labyrinth) - 1, cont))

        
        for cont in range(len(self.labyrinth) - 1, len(self.labyrinth) - 4, -1):
            self.win1.append((cont, len(self.labyrinth[len(self.labyrinth) - 1]) - 1))
