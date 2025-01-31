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
        num = random.random(1, 6)
        attack = num * attacker.attack_power
        defender.health -= attack

    def start_battle(self):
        # Starts turn based battle between 2 players #
        while self.__player1.health > 0 and self.__player2.health > 0:
            self.__player1.attack()
            self.__player2.attack()
        if self.__player1.health > 0:
            print(self.__player1.name + "wins")
        else:
            print(self.__player2.name + "wins")
