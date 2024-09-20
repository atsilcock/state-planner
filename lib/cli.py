from models.state import State
from models.city import City



def main(): 
    while True:
        print("")
        view_all_states()
        print("")
        main_menu()
        try: 
            print("")
            choice = input("Enter your choice: ")
            print("")

            if choice == "1":
                view_all_states()
            elif choice == "2":
                add_a_state("name", "population", "region")
            elif choice == "3":
                delete_a_state("name")
            elif choice == "4":
                update_a_state("name", "region", "population")
            elif choice == "5":
                get_cities_by_state("state_id")
            else:
                if choice == "e":
                    exit_program()
                    break
        except ValueError:
            print("Invalid input. Please try again.")



def view_all_states():
    all_states = State.get_all()
    for i, state in enumerate(all_states, start=1):
        print(f"{i}. {state.name} | Population {state.population} | Region {state.region}")

def add_a_state(name, population, region):

    name = input("Please enter a name: ")
    region = input ("please enter a region: ")
    
    while True: 
        try: 
            population = int(input("Please enter the population"))
            break
        except ValueError:
            print("Population must be an integer")
    print("You have succsefully added the population")
    
    if isinstance(name, str):
        print("name is a string")
    else:
        print("not a string")

    if isinstance(region, str):
        print("region is a string")
    else:
        print("region is not a string")
    
    state_instance = State(name, population, region)
    state_instance.save()
    print(f"State {name} has now beend saved")

def delete_a_state(name):
    print("")
    all_states = State.get_all()
    view_all_states()
    print()

    try:
        delete_state = int(input("Please enter the state # that you would like to delete: "))
        print(f"You have entered {name}")
    except ValueError: 
        print("Invalid selection. Please try again.")

    state_by_name = all_states[delete_state -1]


    if state_by_name:
        state_by_name.delete()
        print(f"The {name} has been deleted")
        
    else:
        print("State not found")

def update_a_state(name, region, population):
    all_states = State.get_all()
    view_all_states()
    
    try:
        print("")
        update_state = int(input("Which state would you like to Update?: "))
        print("")
        print(f"Follow Directions: ")
        print("")
    except ValueError:
        ("Try Again")

    selected_state = all_states[update_state - 1]

    if selected_state:
        
        name = input(f"Provide updated name: ")
        if name.isalpha():
            print("You have updated the name")
        else:
            print("")
            print("Invalid name. Please try again.")
            print("")
            return update_a_state(name,region, population)
            print("")

        
        region = input(f"Please enter the new region: ")
        if region.isalpha():
            print("You have updated the region")
        else:
            print("")
            print("Invalid region name. Please try again.")
            print("")
            return update_a_state(name,region, population)
        print("")

        try:
            population = int(input("Please enter the new population: "))
        except ValueError:
            print("Population must be a number")
            return

        selected_state.name = name
        selected_state.region = region
        selected_state.population = population
        selected_state.update()

    else:
        print("try again ")

def get_cities_by_state(state_id):
    all_cities =  State.get_all()
    view_all_states()
    
    try:
    # write code where the user is choosing on of the available states
        select_state_to_view_cities = int(input("Choose the state which you would like to view the cities for: "))
        all_cities[select_state_to_view_cities -1]
    


def exit_program():
    print("You are now leaving - Goodbye!")

def main_menu():
    stars()
    print("1. View all states")
    print("2. Add a state")
    print("3. Delete a state")
    print("4. Update a state")
    print("5. Select State to view it's cities")



def stars():
    print("******************")

if __name__ == "__main__":
    main()
