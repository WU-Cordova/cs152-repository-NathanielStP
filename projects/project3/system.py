from projects.project3.order import Order
from projects.project3.orderitem import OrderItem
from projects.project3.drink import Drink
from datastructures.deque import Deque

class System():
    
    def __init__(self):
        Mocha = Drink("Mocha", 3.50)
        Latte = Drink("Latte", 4.00)
        Water = Drink("Water", 0.50)
        Cocoa = Drink("Cocoa", 3.00)
        Lemonade = Drink("Lemonade", 3.50)
        self.menu = [Mocha, Latte, Water, Cocoa, Lemonade]

        self.dayinreview = []
        self.orders = Deque(data_type=OrderItem)
        
        
    def run(self):
        printer = 'Main Menu' + "\n" + "1. Menu" '\n' \
             + "2. New Order" + "\n" + "3. Orders" + "\n" \
               + "4. Complete" + "\n" + "5. Report" + "\n" + "6. Exit" \
               + "\n" + "\n"
        exit = False
        print(printer)
        while not exit:
            cmd = input("Choice: ")
            cmd = int(cmd)
            if cmd == 1:
                for i in range(len(self.menu)):
                    print(str(i + 1) + ". " + str(self.menu[i]))
            elif cmd == 2:
                name = input("Name? ")
                product = OrderItem(name)
                drinks = input("Amount of Drinks? ")
                drinks = int(drinks)
                order = Order()
                for _ in range(drinks):
                    item = input("Drink #: ")
                    item = int(item)
                    drink = self.menu[item - 1]
                    cust = input("Customization: ")
                    order.add(drink, cust)
                product.drinks(order)
                self.orders.enqueue(product)
                print("New order added.")
            elif cmd == 3:
                for item in self.orders:
                    print(item)
            elif cmd == 4:
                item = self.orders.dequeue()
                self.orders.dequeue()
                print("Order finished")
                self.dayinreview.append(item)
            elif cmd == 5:
                for item in self.dayinreview:
                    print(item)
            elif cmd == 6:
                exit = True
            else:
                print("Invalid Command.")
        print("Have a nice day.")

