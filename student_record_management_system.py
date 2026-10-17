
# Student Record Management System using Singly Linked List

# Node class
class Node:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.next = None


# Linked List class
class StudentLinkedList:
    def __init__(self):
        self.head = None

    # Add student
    def add(self, roll_no, name, marks):
        new_node = Node(roll_no, name, marks)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

        print("Student record added successfully.")

    # Display students
    def display(self):
        if self.head is None:
            print("No student records available.")
            return

        print("\n----- STUDENT RECORDS -----")
        temp = self.head

        while temp is not None:
            print("Roll No :", temp.roll_no)
            print("Name    :", temp.name)
            print("Marks   :", temp.marks)
            print("--------------------------")
            temp = temp.next

    # Delete student
    def delete(self, roll_no):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.roll_no == roll_no:
            self.head = self.head.next
            print("Student record deleted successfully.")
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.roll_no == roll_no:
                temp.next = temp.next.next
                print("Student record deleted successfully.")
                return
            temp = temp.next

        print("Student record not found.")

    # Update student
    def update(self, roll_no):
        temp = self.head

        while temp is not None:
            if temp.roll_no == roll_no:
                print("Current Name :", temp.name)
                print("Current Marks:", temp.marks)

                temp.name = input("Enter new name: ")
                temp.marks = float(input("Enter new marks: "))

                print("Student record updated successfully.")
                return

            temp = temp.next

        print("Student record not found.")


# Main program
students = StudentLinkedList()

while True:
    print("\n--- STUDENT RECORD MANAGEMENT ---")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        students.add(roll, name, marks)

    elif choice == "2":
        students.display()

    elif choice == "3":
        roll = int(input("Enter Roll No to delete: "))
        students.delete(roll)

    elif choice == "4":
        roll = int(input("Enter Roll No to update: "))
        students.update(roll)

    elif choice == "5":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")
