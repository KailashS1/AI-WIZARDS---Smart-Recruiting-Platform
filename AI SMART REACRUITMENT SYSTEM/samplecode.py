# Pre-populated data
users = {
    "john@example.com": {"name": "John", "password": "password123"},
    "jane@example.com": {"name": "Jane", "password": "secure456"}
}

categories = [
    {"type": "IT", "name": "Software Development"},
    {"type": "Finance", "name": "Accounting"},
    {"type": "Healthcare", "name": "Nursing"}
]

jobs = [
    {"status": "draft", "title": "Frontend Developer", "description": "Develop user interfaces using React."},
    {"status": "published", "title": "Accountant", "description": "Manage financial records and reporting."}
]

def start_program():
    while True:
        print("\n--- Welcome ---")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Press 1 to Login, 2 to Register, 3 to Exit: ")

        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def register():
    print("\n--- Register ---")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    while True:
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")
        if password == confirm_password:
            break
        else:
            print("Passwords do not match. Try again.")
    users[email] = {'name': name, 'password': password}
    print("Registration successful. Please login.")
    login()

def login():
    print("\n--- Login ---")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    
    if email in users and users[email]['password'] == password:
        print(f"Welcome back, {users[email]['name']}!")
        dashboard()
    else:
        print("Invalid email or password. Try again.")

def dashboard():
    while True:
        print("\n--- Dashboard ---")
        print("1. Job Creation")
        print("2. Job Categories")
        print("3. Logout")
        choice = input("Select an option: ")

        if choice == '1':
            job_creation()
        elif choice == '2':
            job_categories()
        elif choice == '3':
            print("Logging out...")
            return
        else:
            print("Invalid choice. Try again.")

def job_creation():
    print("\n--- Job Creation ---")
    job_title = input("Enter Job Title: ")
    job_description = input("Enter Job Description: ")
    job_location = input("Enter Job Location: ")
    employment_type = input("Enter Employment Type (Part-Time/Full-Time): ")
    salary_range = input("Enter Salary Range: ")
    application_deadline = input("Enter Application Deadline: ")
    required_qualification = input("Enter Required Qualification: ")
    responsibilities = input("Enter Responsibilities: ")

    while True:
        print("\n1. Save as Draft")
        print("2. Publish")
        choice = input("Select an option: ")

        if choice == '1':
            jobs.append({'status': 'draft', 'title': job_title, 'description': job_description})
            print("Job moved to draft.")
            break
        elif choice == '2':
            jobs.append({'status': 'published', 'title': job_title, 'description': job_description})
            print("Job published successfully.")
            break
        else:
            print("Invalid choice. Try again.")

def job_categories():
    while True:
        print("\n--- Job Categories ---")
        print("1. Add Category")
        print("2. View Categories")
        print("3. Back to Dashboard")
        choice = input("Select an option: ")

        if choice == '1':
            category_type = input("Enter Category Type: ")
            category_name = input("Enter Category Name: ")
            if not category_name.strip():
                print("Category Name is required. Try again.")
                continue
            categories.append({'type': category_type, 'name': category_name})
            print("Category added successfully.")
        elif choice == '2':
            print("\n--- Categories List ---")
            if not categories:
                print("No categories available.")
            else:
                for idx, category in enumerate(categories, start=1):
                    print(f"{idx}. {category['type']} - {category['name']}")
                delete_choice = input("Enter category number to delete or press Enter to skip: ")
                if delete_choice.isdigit():
                    idx = int(delete_choice) - 1
                    if 0 <= idx < len(categories):
                        deleted = categories.pop(idx)
                        print(f"Category '{deleted['name']}' deleted.")
                    else:
                        print("Invalid category number.")
        elif choice == '3':
            return
        else:
            print("Invalid choice. Try again.")

# Run the program
start_program()
