from projects.project2.cell import Cell
from projects.project2.grid import Grid
from projects.project2.kbhit import KBHit
import time

class GameController():

    def __init__(self, length, height):
        self.rows = length
        self.cols = height
        self.generation = Grid(length, height, Cell)
        self.idlist = []   

    def nextGen(self):
        # sets up a helping grid to save the new generation to
        helperGrid = Grid(self.rows, self.cols, Cell)
        for i in range(self.rows):
            for x in range(self.cols):
                # ensures that all cells in the helper grid are dead, as during their creation they were auto generated randomly
                helperGrid.setSelf(i, x, False)
                neighbors = self.generation.numNeighbors(i, x)
                # checks if the cell lives or dies
                if(self.generation.checkSelf(i, x) == True):
                    if neighbors < 2 or neighbors > 3:
                        helperGrid.setSelf(i, x, False)
                    else:
                        helperGrid.setSelf(i, x, True)
                else:
                    if neighbors == 3:
                        helperGrid.setSelf(i, x, True)
        # used for detecting repeating generations
        helperGrid.setid()
        self.generation = helperGrid

    # makes the game runnable
    def run(self):
        kbhit = KBHit()
        mode = "manual"
        counter = 0
        while True:
            # prints current generation
            self.generation.printGrid()
            print("Generation: " + str(counter))
            
            # checks for repetition or death, then appends the new id if not
            gen_id = self.generation.getid()
            if gen_id == (0, 0):
                print("All died. Ending simulation after " + str(counter) + " generations.")
                break

            if gen_id in self.idlist:
                print("Pattern repeating. Ending simulation after " + str(counter) + " generations.")
                break
            self.idlist.append(gen_id)

            print(f"Mode: {mode.upper()} | Press 'M' for Manual, 'A' for Auto, 'S' to Step, 'Q' to Quit")

            if mode == "manual":
                while True:
                    if kbhit.kbhit():
                        key = kbhit.getch().lower()
                        if key == 'q':
                            print("Quitting.")
                            kbhit.set_normal_term()
                            return
                        elif key == 'a':
                            print("Switched to Automatic Mode.")
                            mode = 'auto'
                            # prevents automatic mode from ending on the first generation
                            self.idlist.pop()
                            break
                        elif key == 's':
                            # generates next generation and increments the counter to detect how long it has survived
                            self.nextGen()
                            counter += 1
                            break
                        elif key == 'm':
                            print("Already in Manual Mode.")
                    time.sleep(0.1)  # prevent CPU spinning
            else:  # auto mode
                time.sleep(1)
                self.nextGen()
                counter += 1


                kbhit.set_normal_term()
