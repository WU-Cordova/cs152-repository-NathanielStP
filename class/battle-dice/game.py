import random
from character import Character

class Game:
    # Manages Dice Battle Game logic #

    def __init__(self, player1: Character, player2: Character):
        # Initializes the game with two players #
        self.__player1 = player1
        self.__player2 = player2

    def attack(self, attacker: Character, defender: Character):
        # Performs attack where attacker rolls dice to determine damage #
        num = random.randint(1, 6)
        attack = num * attacker.attack_power
        defender.health -= attack
        print(attacker.name +" attacks and does " + str(attack) + " damage.")
        print(defender.name +" has " + str(defender.health) + " health left")

    def start_battle(self):
        # Starts turn based battle between 2 players #
        gameGoing = True
        while gameGoing:
            self.attack(self.__player1, self.__player2)
            if(self.__player2.health <= 0): 
                gameGoing = False
                break
            self.attack(self.__player2, self.__player1)
            if(self.__player1.health <= 0): gameGoing = False
        if self.__player1.health > 0:
            print(self.__player1.name + " wins")
        else:
            print(self.__player2.name + " wins")
