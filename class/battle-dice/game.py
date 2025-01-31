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
        pass # TODO implement dice roll 1-6 and apply scaled attack #

    def start_battle(self):
        # Starts turn based battle between 2 players #
        pass # TODO implement battle loop where players take turns #
    