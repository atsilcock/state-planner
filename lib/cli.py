from helpers import (
    exit_program,
    get_states,
    add_state, 
    list_states, 
    list_cities, 
    display_state_details, 
    delete_city, 
    find_cities_by_state,
    delete_state, 
    update_state,
    find_state,
    stars
)

def main():
    intro_message()
    select_state()

def select_state():
    while True:
        print("")
        print("Your States: ")
        print("")
        states = get_states()
        list_states(states)

        user_action = select_state_menu()

        if user_action == 'e':
            exit_program()
            break  

        elif user_action == "add":
            adding_a_state()
            name = input("Enter the state name: ")
            population = input("Enter the population: ")
            try:
                population = int(population)
            except ValueError:
                print("You must type an number ")
                continue
            region = input("Enter the region: ")
            new_state = add_state(name, population, region) 
        
            print(f"You have now added the state {new_state.name} successfully ")
        
        elif user_action == "delete":
            delete_name = input("Enter the number you would like to delete: ")
            delete_state(int(delete_name))

        elif user_action == "update":
            state_to_be_updated = input("Enter the number that you would ike to update")
            name = input("Enter a name: ")
            population = input("Enter population: ")
            region = input("Enter region: ")
            update_state(int(state_to_be_updated), name, int(population), region)

        elif user_action.isdigit(): #view state details
            state = find_state(int(user_action))
            if state:
                print(f"\nSelected State: {state.name}")
                print(f"Population: {state.population}")
                print(f"Region: {state.region}")
                select_city(state)  # Go to city-specific menu for the selected state
            else:
                print("Entered number you have entered does not match a state.")

        else:
            print("Invalid choice, please try again.")

def select_city(state):
    while True:
        cities = find_cities_by_state(state.id)  # Use the helper function
        print(f"\nCities in {state.name}:")
        if cities:
            list_cities(cities)  # Display the cities
        else:
            print("No cities found for this state.")

        user_action = city_menu()

        if user_action == 'e':
            break  # Exit the city menu




def select_state_menu():

    print("")
    stars()
    print("Type # in List to view state details")
    print("Type Add to add a new state")
    print("Type Delete to delete one of the states")
    print("Type Update to update state")
    print("Type e to Exit")
    stars()

    return input("Your choice: ").lower()

def adding_a_state():
    print("")
    stars()
    print("\nEnter the details below to add a new State: ")
    print("")

def city_menu():
    print("\nCity Options")
    stars()
    print("Type 'Add' to add a city.")
    print("Type 'View' to view all cities for this state.")
    print("Type 'Back' to go back to the previous menu.")
    stars()
    return input("Your choice: ").lower()

def intro_message():
    print("\nHello & Welcome to Your long awaited vacation!")
    print ("\n")

if __name__ == "__main__":
    main()
