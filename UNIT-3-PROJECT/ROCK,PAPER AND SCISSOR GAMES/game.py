print("Rock Paper Scissors Game")
user = input("Enter rock / paper / scissors: ")
computer = "rock"
if user not in ["rock", "paper", "scissors"]:
    print("Invalid input. Please enter rock, paper, or scissors.")
else:
    print("Computer choice:", computer)
    if user == computer:
        print("Match Draw")
    elif user == "rock" and computer == "scissors":
        print("User Win")

    elif user == "paper" and computer == "rock":
        print("User Win")
    elif user == "scissors" and computer == "paper":
        print("User Win")
    else:
        print("Computer Win")









