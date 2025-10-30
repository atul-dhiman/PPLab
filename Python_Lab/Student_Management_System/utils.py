
def print_menu():
    """Prints the main menu options."""
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search for Student")
    print("4. Exit")

def get_student_details_from_input():
    """
    Prompts the user for student details and returns them as a tuple.
    Includes basic error handling for the roll number.
    """
    name = input("Enter the name: ")
    while True:
        try:
            roll_number = int(input("Enter the roll number: "))
            break  # Exit loop if conversion to int is successful
        except ValueError:
            print("Invalid input. Please enter a number for the roll number.")
    department = input("Enter the name of the department: ")
    return name, roll_number, department

def get_search_name():
    """Prompts the user for a name to search for."""
    return input("Enter the name of the student to search: ")

def print_all_students(names_list, rolls_list, depts_list):
    """
    Takes the student lists as arguments and prints them.
    """
    if not names_list:
        print("\n--- No students in the database. ---")
        return

    print("\n--- All Students ---")
    for i in range(len(names_list)):
        print(f"  {i+1}. Name: {names_list[i]}, Roll: {rolls_list[i]}, Dept: {depts_list[i]}")

def print_student_details(student_data):
    name, roll, dept = student_data 
    print(f"\n--- Student Found ---")
    print(f"Name: {name}")
    print(f"Roll Number: {roll}")
    print(f"Department: {dept}")