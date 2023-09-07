import time

from src.app import App


if __name__ == "__main__":
    app = App('projects_and_contracts.db')
    app.db.create_tables()

    while True:
        print("1. Create Contract")
        print("2. Confirm Contract")
        print("3. Complete Contract")
        print("4. Add Contract to Project")
        print("5. Create Project")
        print("6. Print Projects")
        print("7. Print Contracts")
        print("8. Quit")

        choice = input("Enter option number: ")

        if choice == '1':
            name = input("Enter contract name: ")
            app.create_contract(name)
            print("Contract created successfully")
        elif choice == '2':
            contract_id = input("Enter contract id: ")
            app.confirm_contract(int(contract_id))
            print("Contract confirmed successfully")
        elif choice == '3':
            contract_id = input("Enter contract id: ")
            app.complete_contract(int(contract_id))
            print("Contract completed successfully")
        elif choice == '4':
            contract_id = input("Enter contract id: ")
            project_id = input("Enter project id: ")
            app.add_contract_to_project(int(contract_id), int(project_id))
            print("Contract added to project successfully")
        elif choice == '5':
            name = input("Enter project name: ")
            app.create_project(name)
            print("Project created successfully")
        elif choice == '6':
            app.print_projects()
        elif choice == '7':
            app.print_contracts()
        elif choice == '8':
            break
        else:
            print("Invalid choice")

    app.db.session.close()
