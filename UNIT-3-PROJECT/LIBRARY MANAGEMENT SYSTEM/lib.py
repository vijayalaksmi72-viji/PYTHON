print("Mini Library Management System")

books = ["python", "java", "c++", "html", "css"]

while True:
    print("\n1. Show Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Available Books:", books)

    elif choice == "2":
        book = input("Enter book name to borrow: ")
        if book in books:
            books.remove(book)
            print("You borrowed:", book)
        else:
            print("Book not available")

    elif choice == "3":
        book = input("Enter book name to return: ")
        books.append(book)
        print("Book returned:", book)

    elif choice == "4":
        print("Thank you")
        break

    else:
        print("Invalid choice") 


