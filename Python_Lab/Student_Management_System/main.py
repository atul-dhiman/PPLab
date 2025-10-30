
import database
import utils

def main():
    try:
        n = int(input("Enter the number of students to add initially (or 0 to skip): "))
        if n > 0:
            print(f"\n--- Please enter details for {n} students ---")
            for _ in range(n):
                name, roll, dept = utils.get_student_details_from_input()
                database.add_student(name, roll, dept)
            print("--- Initial students added! ---")
    except ValueError:
        print("Invalid number. Starting with no students.")
    while True:
        utils.print_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue  # Ask for choice again

        if choice == 1:
            # 1. Get details from user (using utils)
            name, roll, dept = utils.get_student_details_from_input()
            # 2. Add details to database (using database)
            database.add_student(name, roll, dept)

        elif choice == 2:
            # 1. Get data from database
            names, rolls, depts = database.get_all_students()
            # 2. Print the data (using utils)
            utils.print_all_students(names, rolls, depts)

        elif choice == 3:
            # 1. Get name to search (using utils)
            search_name = utils.get_search_name()
            # 2. Find student in database
            student_data = database.search_student_details(search_name)
            
            # 3. Print results (using utils or a simple message)
            if student_data:
                utils.print_student_details(student_data)
            else:
                print(f"\nSorry, the student '{search_name}' was not found.")

        elif choice == 4:
            print("Exiting program. Goodbye!")
            break  # Exit the while loop

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()