from datastructures.array import Array
from datastructures.array2d import Array2D
from projects.project2.cell import Cell
from random import random


class Grid():

    def __init__(self, height, length, datatype: Cell):
        mylist = [datatype]*height
        self.gameGrid = Array2D([[mylist] for _ in range(length)])
        for i in range(height):
            for x in range(length):
                value = random.choice([True, False])
                self.gameGrid[i][x].setlife(value)
                if(x == length - 1):
                    self.gameGrid[i][x].setborder("right")
                if(x == 0):
                    self.gameGrid[i][x].setborder("left")
                if(i == 0):
                    self.gameGrid[i][x].setborder("up")
                    if(x == 0): self.gameGrid[i][x].setborder("upleft")
                    if(x == length - 1): self.gameGrid[i][x].setborder("upright")
                if(i == height - 1):
                    self.gameGrid[i][x].setborder("down")
                    if(x == 0): self.gameGrid[i][x].setborder("downleft")
                    if(x == length - 1): self.gameGrid[i][x].setborder("downright")
                

    def checkNeighbor(self, positionX: int, positionY: int):
        return self.gameGrid[positionX][positionY].getlife
