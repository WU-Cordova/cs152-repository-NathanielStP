import copy
import random
from datastructures.bag import Bag
from projects.project1.card import Card, Suit, Face
from projects.project1.multideck import MultiDeck


class Game:
    def __init__(self):
        self.deck = MultiDeck()

    def run(self):
        dealerHand = self.deck.deal()
        dealerscore = self.score(dealerHand)
        playerHand = self.deck.deal()
        playerscore = self.score(playerHand)
        print(str(playerHand[0]) + " " + str(playerHand[1]) + " Player's hand, score: " + str(playerscore))
        print(str(dealerHand[0]) + " [unknown card] Dealer's hand, score: " + str(dealerscore - dealerHand[1].face.face_value()))
        while True:
            command = input("h to hit, s to stay ")
            if command != "h" and command != "s":
                print("invalid command")
                
            if command == "h":
                card = self.deck.draw()
                playerHand.append(card)
                playercards = ""
                for i in range(len(playerHand)):
                    playercards += str(playerHand[i])
                    playercards += " "
                    playerscore = self.score(playerHand)
                print(playercards + " Player's hand, score: " + str(playerscore))
                print(str(dealerHand[0]) + " [unknown card] Dealer's hand, score: " + str(dealerscore - dealerHand[1].face.face_value()))
                if playerscore >= 21:
                    break
            elif command == "s":
                break


        while dealerscore < 17:
            card = self.deck.draw()
            dealerHand.append(card)
            dealerscore = self.score(dealerHand)
        self.win(dealerscore, playerscore, dealerHand, playerHand)

    

    # detects who won
    def win(self, dealerscore, playerscore, dealerHand, playerHand):
        dealercards = ""
        for i in range(len(dealerHand)):
            dealercards += str(dealerHand[i])
            dealercards += " "
        playercards = ""
        for i in range(len(playerHand)):
            playercards += str(playerHand[i])
            playercards += " "
        if dealerscore >= 17:
            print(playercards + " Player's hand, score: " + str(playerscore))
            print(dealercards + " Dealer's hand, score: " + str(dealerscore))
            if playerscore > 21:
                print("Bust. You lose.")
            elif dealerscore > playerscore and dealerscore < 21:
                print("You lose.")
            elif dealerscore == playerscore:
                print("Draw.")
            elif dealerscore == 21:
                print("Dealer has blackjack. You lose.")
            elif playerscore == 21:
                print("Blackjack. You win. Yay.")
            else:
                print("You win.")
    
    def score(self, hand):
        aces = 0
        score = 0
        for card in hand:
            value = card.face.face_value()
            if card.face.face_card() == "Ace":
                aces += 1
                value = 11
            score += value
        while score > 21 and aces > 0:
            aces -= 1
            score -= 10
        return score
      
