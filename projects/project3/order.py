from projects.project3.drink import Drink

class Order():

    def __init__(self, drink: Drink = None, custom: str = None):
        self.drinks = [drink, custom]
        self.count = 0

    def add(self, drink: Drink, custom: str = "None"):
        if(self.drinks[0] == None and len(self.drinks) > 0):
            self.drinks.pop(0)
            self.drinks.pop(0)
        self.drinks.append(drink)
        self.drinks.append(custom)
        self.count += 1
    
    def remove(self, index):
        self.drinks.remove(index)
        self.count -= 1

    def __str__(self) -> str:
        item = str(self.drinks[0]) + " " + str(self.drinks[1])
        for i in range(2, len(self.drinks) - 1, 2):
            item += "\n"
            item += str(self.drinks[i])
            item += " "
            item += str(self.drinks[i + 1])
        return item
    
    