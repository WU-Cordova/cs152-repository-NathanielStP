import copy
from dataclasses import dataclass
from enum import Enum
import random


class Suit(Enum):
    HEARTS = "Hearts"
    SPADE = "Spades"
    CLUBS = "Clubs"
    DIAMONDS = "Diamonds" 

class Face(Enum):
    TWO = "2" 
    THREE = "3"
    FOUR = "4"
    FIVE = "5"
    SIX = "6"
    SEVEN = "7"
    EIGHT = "8"
    NINE = "9"
    TEN = "10"
    JACK = "Jack"
    QUEEN = "Queen"
    KING = "King" 
    ACE = "Ace"

    def face_value(self)-> int:
        match self:
            case Face.JACK | Face.QUEEN | Face.KING:
                return 10
            case Face.ACE:
                return 11
            case _:
                return int(self.value)
    
    # returns if the card is an ace, for detection of 1 or 11 logic
    def face_card(self)-> str:
        match self:
            case Face.ACE:
                return "Ace"
            case _:
                return "None"
    
@dataclass
class Card:
    face: Face
    suit: Suit

    def __hash__(self)-> int:
        return hash(self.face.name) * hash(self.suit.name)
    
    def __str__(self)-> str:
        return f"[{self.face.value} of {self.suit.value}]"
