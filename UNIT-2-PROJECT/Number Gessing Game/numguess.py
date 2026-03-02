import random
number = random.randint(1, 10)
guess = 0
print("Guess the number between 1 and 10!")
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct! You guessed the number!")