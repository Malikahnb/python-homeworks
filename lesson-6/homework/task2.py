def add_employee():
    with open('employees.txt', 'a') as f:
        e_id = input('Enter the employee ID: ')
        name = input('Enter the employee name: ')
        position = input('Enter the employee position: ')
        salary = input('Enter the employee salary: ')

        f.write(f'{e_id}, {name}, {position}, {salary}\n')
        print('Employee added')


def view_employees():
    with open('employees.txt', 'r') as f:
        first_char = f.read(1)
        if not first_char:
            print('No employees')
        else:
            for line in f:
                print(line)


def search_employee():
    e_id = input('Enter the employee ID: ')
    with open('employees.txt', 'r') as f:
        for record in f:
            if record.startswith(e_id + ','):
                print("The employee: ", record.strip(), "\n")
                return
    print('No employees found')


def update_employee():
    e_id = input('Enter the employee ID: ')
    updated_records = []
    found = False
    with open("employees.txt", "r") as file:
        for record in file:
            if record.startswith(e_id + ","):
                name = input("Enter new Name: ")
                position = input("Enter new Position: ")
                salary = input("Enter new Salary: ")
                updated_records.append(f"{e_id}, {name}, {position}, {salary}\n")
                found = True
            else:
                updated_records.append(record)
    if not found:
        print("Employee not found.\n")
        return
    with open("employees.txt", "w") as file:
        file.writelines(updated_records)
    print("Employee record updated ")


def delete_employee():
    e_id = input("Enter Employee ID to delete: ")
    updated_records = []
    found = False
    with open("employees.txt", "r") as file:
        for record in file:
            if record.startswith(e_id + ","):
                found = True
            else:
                updated_records.append(record)
    if not found:
        print("Employee not found.\n")
        return
    with open("employees.txt", "w") as file:
        file.writelines(updated_records)
    print("Employee record deleted ")


while True:
    print("1. Add new employee record")
    print("2. View all employee records")
    print("3. Search for an employee by Employee ID")
    print("4. Update an employee's information")
    print("5. Delete an employee record")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again.\n")

