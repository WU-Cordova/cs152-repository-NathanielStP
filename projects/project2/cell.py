

class Cell():

    def __init__(self, life: bool = False, firstIndex: int = 0):
        #initializes cell. alive tells you if the cell is alive, the value is used to determine grid repetition
        self.alive = life
        self.value = firstIndex + 1
    
    #sets the life value for the cell
    def __setlife__(self, living: bool) -> None:
        self.alive = living

    #sets the cell's value
    def __setvalue__(self, number: int) -> None:
        self.value = number

    #returns if the cell is alive
    def __getlife__(self) -> bool:
        return self.alive

    #returns cell's value    
    def __getvalue__(self) -> int:
        return self.value

    
    #prints the cell "X" if alive, "O" if not
    def __str__(self):
        if(self.alive):
            return "X"
        else: return "O"
