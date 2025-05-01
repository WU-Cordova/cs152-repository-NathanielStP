import copy
import random
from datastructures.bag import Bag
from projects.project1.card import Card, Suit, Face
from projects.project1.multideck import MultiDeck


class Game:
    def __init__(self):
        # creates the deck to draw cards from
        self.deck = MultiDeck()

    def run(self):
        # gives each player a hand
        dealerHand = self.deck.deal()
        dealerscore = self.score(dealerHand)
        playerHand = self.deck.deal()
        playerscore = self.score(playerHand)
        print(str(playerHand[0]) + " " + str(playerHand[1]) + " Player's hand, score: " + str(playerscore))
        print(str(dealerHand[0]) + " [unknown card] Dealer's hand, score: " + str(dealerscore - dealerHand[1].face.face_value()))
        while True:
            command = input("h to hit, s to stay ").strip().upper()
            if command != "H" and command != "S":
                print("invalid command")
            
            # if the player hits, they draw a card and the loop continues until they stay or bust
            if command == "H":
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
            elif command == "S":
                break

        # after a stay or bust, gets the dealer to at least 17 and then checks who won
        while dealerscore < 17:
            card = self.deck.draw()
            dealerHand.append(card)
            dealerscore = self.score(dealerHand)
        self.win(dealerscore, playerscore, dealerHand, playerHand)

    

    # detects who won
    def win(self, dealerscore, playerscore, dealerHand, playerHand):
        # creates string for ease of access when printing each player's hand
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
    
    # calculates the score, allowing for aces to be counted as 1 if necessary
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
      
