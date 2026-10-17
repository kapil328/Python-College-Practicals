
undo = []
redo = []
document = ""

while True:
    print("\n1. Make Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        undo.append(document)
        document = input("Enter new text: ")
        redo.clear()

    elif choice == 2:
        if undo:
            redo.append(document)
            document = undo.pop()
        else:
            print("Nothing to undo")

    elif choice == 3:
        if redo:
            undo.append(document)
            document = redo.pop()
        else:
            print("Nothing to redo")

    elif choice == 4:
        print("Document:", document)

    elif choice == 5:
        break

    else:
        print("Invalid choice")
