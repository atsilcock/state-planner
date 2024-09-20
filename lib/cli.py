from helpers import (
    exit_program,
    get_states,
    get_cities,
    add_state,
    add_city,
    list_states, 
    list_cities, 
    display_state_details, 
    delete_city_by_number, 
    find_cities_by_state,
    delete_state_by_number, 
    update_state_by_name,
    update_city_by_number,
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
            while True:
                population_input = input("Enter the population: ")
                try:
                    population = int(population_input)
                    break
                except ValueError:
                    print("Error: Population must be an integer. Please try again.")

            region = input("Enter the region: ")
            new_state = add_state(name, population, region) 
            print(f"You have now added the state {new_state.name} successfully ")

        elif user_action == "update":
            state_name_to_be_updated = input ("Enter the state that needs to be updated: ")
            state_to_update = find_state(state_name_to_be_updated)

            if not state_to_update:
                print("State not found. Please try again.")
                

            if state_to_update:
                new_name = input ("Enter a new name: ")
                while True:
                    population_input = input ("Enter the population: ")
                    try:
                        population  = int(population_input)
                        break
                    except ValueError:
                        print("Must be a integer")
            new_region = input("Enter the new region: ")

            update_state = update_state_by_name(states, state_name_to_be_updated, new_name, population, new_region)

            print(f"You have updated {update_state.name}!")
   
        elif user_action == "delete":
            states = get_states()
            list_states(states)
            delete_name_by_number = input("Enter the number of the state you would like to delete: ")
            
            if delete_name_by_number.isdigit():
                delete_number = int(delete_name_by_number)
                if 1 <= delete_number <= len(states):
                    delete_state_by_number(states, delete_number)  # Delete the state based on the number
                else:
                    print("Invalid number, please try again.")
            else:
                print("Please enter a valid number.")

       

def select_city(state):
    pass

            
def select_state_menu():

    print("")
    stars()
    print("Type # in List to view state details")
    print("Type 'Add' to add a new state")
    print("Type 'Delete' to delete one of the states")
    print("Type 'Update' to update state")
    print("Type e to Exit")
    stars()

    return input("Your choice: ").lower()

def adding_a_state():
    print("")
    stars()
    print("\nEnter the details below to add a new State: ")
    print("")

def updating_a_state():
    print("")
    stars()
    print("\nEnter the details below to update a State: ")
    print("")


def adding_a_city():
    print("")
    stars()
    print("\nEnter the details below to add a new City: ")
    print("")

def city_menu():
    print("\nCity Options")
    stars()
    print("Type 'Update' to update a city")
    print("Type 'Add' to add a city.")
    print("Type 'Delete' to delete a city")
    print("Type 'Back' to go back to the previous menu.")
    stars()
    return input("Your choice: ").lower()

def intro_message():
    print("\nHello & Welcome to Your long awaited vacation!")
    print ("\n")

if __name__ == "__main__":
    main()
