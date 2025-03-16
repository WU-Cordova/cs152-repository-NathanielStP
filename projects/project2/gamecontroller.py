from projects.project2.cell import Cell
from projects.project2.grid import Grid
from random import random

class GameController():

    def __init__(self, length, height):
        self.rows = length
        self.cols = height
        self.generation = Grid(length, height, Cell)
        for i in range(length):
            for x in range(height):
                self.generation[i][x].setlife(random.choice(True, False))
                num = i*length + x
                self.generation[i][x].setvalue(num)

    def nextGen(self):
        for i in range(self.rows):
            for x in range(self.cols):
                neighbors = self.generation[i][x].survives(i, x)

    def numNeighbors(self,xPos, yPos) -> int:
        count = 0
        if(self.generation.checkNeighbor(xPos-1, yPos-1)):
            count += 1
        if(self.generation.checkNeighbor(xPos-1, yPos)):
            count += 1
        if(self.generation.checkNeighbor(xPos-1,yPos+1)):
            count += 1
        if(self.generation.checkNeighbor(xPos,yPos-1)):
            count += 1
        if(self.generation.checkNeighbor(xPos,yPos+1)):
            count += 1
        if(self.generation.checkNeighbor(xPos+1,yPos-1)):
            count += 1
        if(self.generation.checkNeighbor(xPos+1,yPos)):
            count += 1
        if(self.generation.checkNeibor(xPos+1,yPos+1)):
            count += 1                        
        return count      
