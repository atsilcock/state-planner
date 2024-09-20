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

def to_update_state():
    name = input("Enter the name of the state to update: ")
    state = find_state_by_name(name)
    if state:
        new_name = input("Enter new state name: ")
        new_population = int(input("Enter new population: "))
        new_region = input("Enter new region: ")
        update_state(state, new_name, new_population, new_region)
        print(f"State '{new_name}' updated successfully.")
    else:
        print(f"State '{name}' not found.")

def handle_select_state_by_name():
    name = input("Enter the name of the state to select: ")
    state = find_state_by_name(name)
    if state:
        manage_cities(state)
    else:
        print(f"State '{name}' not found.")

def manage_cities(state):
    while True:
        print(f"\n--- Managing Cities for {state.name} ---")
        print("1. View All Cities")
        print("2. Add City")
        print("3. Delete City")
        print("4. Update City")
        print("5. Go Back")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            view_all_cities(state)
        elif choice == '2':
            handle_add_city(state)
        elif choice == '3':
            handle_delete_city(state)
        elif choice == '4':
            handle_update_city(state)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def view_all_cities(state):
    cities = get_cities_by_state(state.id)
    if cities:
        for i, city in enumerate(cities, start=1):
            print(f"{i}. {city.name} | Population: {city.city_population}")
    else:
        print(f"No cities found for {state.name}.")

def handle_add_city(state):
    name = input("Enter city name: ")
    population = int(input("Enter population: "))
    add_city(name, population, state.id)
    print(f"City '{name}' added to {state.name} successfully.")

def handle_delete_city(state):
    name = input("Enter the name of the city to delete: ")
    delete_city(state.id, name)

def handle_update_city(state):
    name = input("Enter the name of the city to update: ")
    city = next((c for c in get_cities_by_state(state.id) if c.name.lower() == name.lower()), None)
    if city:
        new_name = input("Enter new city name: ")
        new_population = int(input("Enter new population: "))
        update_city(city, new_name, new_population)
        print(f"City '{new_name}' updated successfully.")
    else:
        print(f"City '{name}' not found.")


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
