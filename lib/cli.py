from helpers import (
    exit_program,
    get_states,
    add_state, 
    list_states, 
    list_cities, 
    display_state_details, 
    delete_city, 
    delete_state, 
    update_state,
    find_state
)

def main():
    intro_message()
    select_state()

def select_state():
    while True:
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
            population = input("Enter population")
            region = input("Enter region: ")
            update_state(int(state_to_be_updated), name, int(population), region)

        elif user_action.isdigit():
            state = find_state(int(user_action))
            if state:
                # display state and cities
                print('state found')
            else:
                print("Entered number does not match a state.")

        else:
            print("Invalid choice, please try again.")

def select_city():
    while True:
        print("Cities : ")
        print("")
        cities = list_cities()
        display_state_details(cities)

        user_action = city_menu

        if user_action == 'e':
            exit_program()
            break  

        elif user_action == "add":
            name = input("Enter the state name: ")
            population = input("Enter the population: ")
            try:
                population = int(population)
            except ValueError:
                print("You must type an number ")
                continue
            region = input("Enter the region: ")
            new_city = (name, population, region) 
        
            print(f"You have now added the state {new_state.name} successfully ")
        
        elif user_action == "delete":
            delete_name = input("Enter the number you would like to delete: ")

            if delete_name.isdigit() and 1 <= len(delete_name) <= len(states):
                state_to_delete = states[int(delete_name) -1]
                state_to_delete.delete()
                print("")
                print(f"The State of {state_to_delete.name} has been deleted!")
                print("")

        elif user_action.isdigit() and 1 <= int(user_action) <= len(states):
            selected_state = states[int(user_action) -1]
            print(f"Selected State: {select_state.name} | Population: {select_state.population} | Region: {select_state.region}")
        

            
        else:
            print("Invalid choice, please try again.")
          
def select_state_menu():

    print("")
    print("******************")
    print("Type # in List to view state details")
    print("Type Add to add a new state")
    print("Type Delete to delete one of the states")
    print("Type Update to update state")
    print("Type e to Exit")
    print("******************")

    return input("Your choice: ").lower()

def adding_a_state():
    print("")
    print("******************")
    print("\nEnter the details below to add a new State: ")
    print("")

def city_menu():
    print("\nCity Options")
    print("******************")
    print("Type 'Add' to add a city.")
    print("Type 'View' to view all cities for this state.")
    print("Type 'Back' to go back to the previous menu.")
    print("******************")
    return input("Your choice: ").lower()

def intro_message():
    print("\nHello & Welcome to Your long awaited vacation!")
    print ("\n")

if __name__ == "__main__":
    main()
