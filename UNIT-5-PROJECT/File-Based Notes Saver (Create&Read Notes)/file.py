def create_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Note saved successfully")

def read_notes():
    try:
        with open("notes.txt", "r") as f:
            data = f.read()
            print("\nYour Notes:")
            print(data)
    except FileNotFoundError:
        print("No notes found")

while True:
    print("1. Create Note")
    print("2. Read Notes")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        create_note()

    elif choice == 2:
        read_notes()

    elif choice == 3:
        print("Exited")
        break

    else:
        print("Invalid choice") 