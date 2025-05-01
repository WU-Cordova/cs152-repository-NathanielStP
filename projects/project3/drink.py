

class Drink():
    
    def __init__(self, drinkname: str, price: float):
        self.drinkname = drinkname
        self.price = price

    def __str__(self) -> str:
        item = str(self.drinkname) + " (" + str(self.price) + "$)"
        return item