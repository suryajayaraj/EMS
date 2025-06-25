# Step 1: Initial employee data
employee_data = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Anjali', 'age': 30, 'department': 'Finance', 'salary': 60000},
    103: {'name': 'Ravi', 'age': 25, 'department': 'IT', 'salary': 55000},
    104: {'name': 'Divya', 'age': 28, 'department': 'Marketing', 'salary': 52000}
}


# Menu display function
def display_menu():
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search for Employee")
    print("4. Exit")


# Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print("\n--- Add New Employee ---")
        while True:
            try:
                emp_id = int(input("Enter Employee ID: "))
                if emp_id in employee_data:
                    print("❌ This Employee ID already exists. Please enter a unique ID.")
                else:
                    break
            except ValueError:
                print("❌ Invalid ID. Please enter a numeric value.")

        name = input("Enter Name: ")
        while True:
            try:
                age = int(input("Enter Age: "))
                break
            except ValueError:
                print("❌ Please enter a valid number for age.")

        department = input("Enter Department: ")
        while True:
            try:
                salary = float(input("Enter Salary: "))
                break
            except ValueError:
                print("❌ Please enter a valid number for salary.")

        employee_data[emp_id] = {
            'name': name,
            'age': age,
            'department': department,
            'salary': salary
        }

        print("✅ Employee added successfully!")

    elif choice == '2':
        print("\n--- All Employees ---")
        if not employee_data:
            print("No employees available.")
        else:
            print("{:<10} {:<15} {:<5} {:<15} {:<10}".format("Emp_ID", "Name", "Age", "Department", "Salary"))
            print("-" * 60)
            for emp_id, details in employee_data.items():
                print("{:<10} {:<15} {:<5} {:<15} {:<10.2f}".format(
                    emp_id,
                    details['name'],
                    details['age'],
                    details['department'],
                    details['salary']
                ))
    elif choice == '3':
        print("\n--- Search for Employee ---")
        try:
            search_id = int(input("Enter Employee ID to search: "))
            if search_id in employee_data:
                emp = employee_data[search_id]
                print("\nEmployee Found:")
                print(f"ID         : {search_id}")
                print(f"Name       : {emp['name']}")
                print(f"Age        : {emp['age']}")
                print(f"Department : {emp['department']}")
                print(f"Salary     : {emp['salary']:.2f}")
            else:
                print("❌ Employee not found.")
        except ValueError:
            print("❌ Invalid input. Please enter a numeric Employee ID.")

    elif choice == '4':
        print("\nThank you for using the Employee Management System. Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")