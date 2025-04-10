from game import Game
from character import Character
from charactertype import CharacterType

# Create Characters #
alice = Character(name="Alice", character_type=CharacterType.WARRIOR, health = 100, attack_power = 5)
bob = Character(name="Bob", character_type = CharacterType.MAGE, health = 70, attack_power = 7)

# start game #
game = Game(alice, bob)
game.start_battle()