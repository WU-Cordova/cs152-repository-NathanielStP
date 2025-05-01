from projects.project3.order import Order

class OrderItem():

    def __init__(self, name: str, order: Order = None):
        self.name = name
        self.order = order

    def drinks(self, order: Order):
        self.order = order
    
    def __str__(self):
        item = self.name
        item += "\n"
        item += str(self.order)
        return item