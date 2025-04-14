import copy
import random
from datastructures.bag import Bag
from projects.project1.card import Card, Suit, Face

class MultiDeck:
    def __init__(self):
        deck = [Card(face, suit) for suit in Suit for face in Face]

        amount = random.choice([2, 4, 6, 8])
        multiDeck = [card for _ in range(amount) for card in copy.deepcopy(deck)]

        self.deckBag = Bag(*multiDeck)
    
    def deal(self) -> list:
        cards = list(self.deckBag.distinct_items())
        card = random.choice(cards)
        self.deckBag.remove(card)
        card2 = random.choice(cards)
        self.deckBag.remove(card2)
        hand = [card, card2]
        return hand
    
    def draw(self) -> Card:
        cards = list(self.deckBag.distinct_items())
        card = random.choice(cards)
        self.deckBag.remove(card)
        return card
