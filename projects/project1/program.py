from projects.project1.game import Game

def main():
    
    # runs the gam
    controller = Game()
    print("Play Blackjack.")
    go = input("Play? (y/n) ").strip().upper()
    while go == "Y":
        controller.run()
        go = input("Play again? (y/n) ").strip().upper()



if __name__ == '__main__':
    main()
