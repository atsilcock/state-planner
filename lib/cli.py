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
    update_state,
    update_city,
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

        elif user_action == "update":
            state = get_states()
            list_states(states)
            state_to_be_updated = input("Enter the number that you would like to update")
            
            if state_to_be_updated.isdigit():
                state_id = int(state_to_be_updated)
                if 1<= state_id <= len(states):
                    name = input("Enter a name: ")
                    while True:
                        population = input("Enter the population: ")

                        if population.isdigit():  # Check if the input is a valid integer
                            population = int(population)  # Convert to an integer
                            break  # Exit the loop once we have valid input
                        else:
                            print("Error: Population must be an integer. Please try again.")

                    region = input("Enter region: ")
                    update_state(state_id, name, population, region)
                    print(f"State {name} has been sucessfully updated")
                else:
                    print("invalid state number")
            else:
                print("Please enter a valid number")

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
        print("")
        if cities:
            list_cities(cities)  # Display the cities
        else:
            print("No cities found for this state.")
        user_action = city_menu()
       
        if user_action == 'e':
            break
        
        elif user_action == "add":
            adding_a_city()
            name = input("Enter the city name: ")
            population = input("Enter the population: ")
            try:
                population = int(population)
            except ValueError:
                print("Error: You must type a number! ")
                continue

            new_city = add_city(name, population, state.id) 
            print(f"You have now added the state {new_city.name} successfully ")
    
        elif user_action == "delete":
            cities = find_cities_by_state(state.id)
            list_cities(cities)  
            delete_city_by_number_input = input("Enter the number of the city you would like to delete: ")

            if delete_city_by_number_input.isdigit():
                delete_number = int(delete_city_by_number_input)
            if 1 <= delete_number <= len(cities):
                city_to_delete = cities[delete_number - 1]  # Get the city object to delete
                delete_city_by_number(cities, delete_number)  # Delete the city based on its ID
                print(f"City {city_to_delete.name} has been successfully deleted.")
            else:
                print("Invalid number, please try again.")
        
        elif user_action == "update":
            pass

        elif user_action == "back":
            print("Go back")
            return

        
        else:
            print("Please enter a valid number.")

            
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
