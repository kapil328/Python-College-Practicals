# Call Center Queue using FIFO
queue = []

while True:
    print("\n--- CALL CENTER ---")
    print("1. Add Call")
    print("2. Answer Call")
    print("3. View Pending Calls")
    print("4. Check Queue Empty")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customerID = input("Enter Customer ID: ")
        callTime = int(input("Enter Call Time: "))
        queue.append((customerID, callTime))
        print("Call added.")

    elif choice == 2:
        if len(queue) == 0:
            print("No calls to answer.")
        else:
            call = queue.pop(0)
            print("Answering Customer ID:", call[0])
            print("Call Time:", call[1], "minutes")

    elif choice == 3:
        if len(queue) == 0:
            print("No pending calls.")
        else:
            print("Pending Calls:")
            for call in queue:
                print("Customer ID:", call[0],
                      "Call Time:", call[1], "minutes")

    elif choice == 4:
        if len(queue) == 0:
            print("Queue is Empty.")
        else:
            print("Queue is Not Empty.")

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid choice.")
