from projects.project1.game import Game

def main():
    
    controller = Game()
    print("Play Blackjack.")
    go = input("Play? (y/n) ")
    while go == "Y" or go == "y":
        controller.run()
        go = input("Play again? (y/n) ")
        go.upper()



if __name__ == '__main__':
    main()
