from helpers import (
    view_all_states, 
    add_state, 
    delete_state, 
    update_state, 
    find_state_by_name, 
    get_cities_by_state, 
    add_city, 
    delete_city, 
    update_city
)

def main():
    while True:
        main_menu()
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_all_states()
        elif choice == '2':
            add_state()
        elif choice == '3':
            delete_state()
        elif choice == '4':
            to_update_state()
        elif choice == '5':
            handle_select_state_by_name()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


def add_state():
    name = input("Enter state name: ")
    population = int(input("Enter population: "))
    region = input("Enter region: ")
    add_state(name, population, region)
    print(f"State '{name}' added successfully.")

def delete_state():
    name = input("Enter the name of the state to delete: ")
    delete_state(name)


def main_menu():
    print("\n--- Main Menu ---")
    print("1. View All States")
    print("2. Add State")
    print("3. Delete State")
    print("4. Update State")
    print("5. Select State by Name")
    print("6. Exit")

if __name__ == "__main__":
    main()
