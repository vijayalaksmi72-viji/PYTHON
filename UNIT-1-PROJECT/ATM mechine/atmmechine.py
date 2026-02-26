balance = 10000
pin = 2026

print("WELCOME TO SIMPLE ATM")

user_pin = int(input("Enter PIN: "))

if user_pin == pin:
    print("\nLogin Successful!\n")

    while True:
        print("------ MENU ------")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your Balance:", balance)

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            balance += amount
            print("Amount Deposited Successfully!")
            print("New Balance:", balance)

        elif choice == "3":
            amount = int(input("Enter withdraw amount: "))
            if amount <= balance:
                balance -= amount
                print("Withdraw Successful!")
                print("Remaining Balance:", balance)
            else:
                print("Insufficient Balance!")

        elif choice == "4":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid Option! Try again.")

else:
    print("Wrong PIN! Try again.")