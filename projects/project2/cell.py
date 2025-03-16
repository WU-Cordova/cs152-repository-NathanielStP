

class Cell():

    def __init__(self, life: bool = False, firstIndex: int = 0, border: str = "False"):
        self.alive = life
        self.value = firstIndex + 1
        self.border = border
    
    def __setlife__(self, living: bool):
        self.alive = living

    def __setvalue__(self, number: int):
        self.value = number

    def __setborder__(self, border: str):
        self.border = border

    def __getlife__(self) -> bool:
        return self.alive
    
    def __getvalue__(self) -> int:
        return self.value
    
    def __getborder__(self) -> bool:
        return self.border
    
    def __str__(self):
        if(self.alive):
            return "X"
        else: return "O"
