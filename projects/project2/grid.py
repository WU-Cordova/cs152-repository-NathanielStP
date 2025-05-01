from datastructures.array import Array
from datastructures.array2d import Array2D
from projects.project2.cell import Cell
import random


class Grid():

    def __init__(self, height, length, datatype: Cell):
        self.height = height
        self.length = length
        self.id = ()
        self.gameGrid = Array2D([[Cell() for _ in range(length)] for _ in range(height)])
        for i in range(height):
            for x in range(length):
                value = random.choice([True, False])
                self.gameGrid[i][x].__setlife__(value)
                # converts grid position from 2d to it's 1d position
                firstIndex = i*self.length + x
                # sets the cell's value to it's firstIndex + 1 (so we count from 1 and not 0)
                self.gameGrid[i][x].__setvalue__(firstIndex+1)
        self.setid()
        
    # checks if neighbors are alive at the given x and y
    # returns false if the grid attmepts to check out of bounds
    def checkNeighbor(self, positionX: int, positionY: int) -> bool:
        if 0 <= positionX < self.height and 0 <= positionY < self.length:
            return self.gameGrid[positionX][positionY].__getlife__()
        return False
    
    def checkSelf(self, x: int, y: int) -> bool:
        return self.gameGrid[x][y].__getlife__()
    
    # sets the life status of the cell at the specified position
    def setSelf(self, x: int, y: int, alive: bool) -> None:
        self.gameGrid[x][y].__setlife__(alive)

    def getid(self) -> int:
        return self.id

    # sets the grid's id, which is used to check for death/repetition
    # each living cell's value is added to get a sum and multiplied to get a product
    # originally, these numbers were then multiplied to get the id
    # but numbers got very big very quickly
    # so now it's a tuple of the 2 values
    # it is stored in a list, if an id is already in the list, we are repeating
    # if the id is (0,0), we are all dead
    # it is possible for 2 different sets of numbers to have the same sum and product, for example (8, 12, 15)     (9, 10, 16)
    # but it is highly unlikely for large amounts of numbers, and in many examples, like the one provided above, it doesn't matter
    # because the generations would die and likely not reach each other anyway
    # i suppose they could possibly survive (in a 2x2 structure), but then would repeat and have to stop anyway 
    def setid(self) -> None:
        helpersum = 0
        helperprod = 1
        found_live = False
        for i in range(self.height):
            for x in range(self.length):
                if self.gameGrid[i][x].__getlife__():
                    helpersum += self.gameGrid[i][x].__getvalue__()
                    helperprod *= self.gameGrid[i][x].__getvalue__()
                    found_live = True
        if not found_live:
            self.id = (0, 0)
        else:
            self.id = (helperprod, helpersum)

    # checks the number of neighbors a cell at position x, y has
    def numNeighbors(self,xPos, yPos) -> int:
        count = 0
        if(self.checkNeighbor(xPos-1, yPos-1)):
            count += 1
        if(self.checkNeighbor(xPos-1, yPos)):
            count += 1
        if(self.checkNeighbor(xPos-1,yPos+1)):
            count += 1
        if(self.checkNeighbor(xPos,yPos-1)):
            count += 1
        if(self.checkNeighbor(xPos,yPos+1)):
            count += 1
        if(self.checkNeighbor(xPos+1,yPos-1)):
            count += 1
        if(self.checkNeighbor(xPos+1,yPos)):
            count += 1
        if(self.checkNeighbor(xPos+1,yPos+1)):
            count += 1                        
        return count  
    
    # prints the grid. "x" for a live cell, "o" for not
    def printGrid(self):
        for i in range(self.height):
            linestr = ""
            for x in range(self.length):
                linestr += str(self.gameGrid[i][x])
            print(linestr)