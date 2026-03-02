password = input("Enter your password: ")

lower = upper = digit = special = 0
for ch in password:
    if ch.islower():
        lower = 1
    elif ch.isupper():
        upper = 1
    elif ch.isdigit():
        digit = 1
    elif ch in "@#$%&*!?":
        special = 1

length = 1 if len(password) >= 8 else 0

strength = lower + upper + digit + special + length
if strength <= 2:
    print("Weak Password")
elif strength == 3 or strength == 4:
    print("Medium Password")
else:
    print("Strong Password")