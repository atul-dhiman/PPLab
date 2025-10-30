
names = []
roll_numbers = []
departments = []

def add_student(name, roll_number, department):
    names.append(name)
    roll_numbers.append(roll_number)
    departments.append(department)
    print("...student added.\n")

def get_all_students():
    return names, roll_numbers, departments

def search_student_details(search_name):
    try:
        index = names.index(search_name)
        roll = roll_numbers[index]
        dept = departments[index]
        return (search_name, roll, dept)  
    except ValueError:
        return None  