import random

def roll_dice():
    return random.randint(1, 6)

while True:
    print("\n1. Play Game")
    print("2. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        input("Press Enter to roll the dice...")
        
        player = roll_dice()
        computer = roll_dice()
        
        print("You rolled:", player)
        print("Computer rolled:", computer)

        if player > computer:
            print("You win!")
        elif player < computer:
            print("Computer wins!")
        else:
            print("It's a tie!")

    elif choice == 2:
        print("Game exited")
        break

    else:
        print("Invalid choice")  