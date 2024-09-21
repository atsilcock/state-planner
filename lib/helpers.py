from models.state import State
from models.city import City

#State functions

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
    
    print("You have successfully added the population")

    state_instance = State(name, population, region)
    state_instance.save()
    print(f"State {name} has now been saved")

def delete_a_state(name):
    all_states = State.get_all()
    view_all_states()

    try:
        delete_state = int(input("Please enter the state # that you would like to delete: "))
        if 1<= delete_state <= len(all_states):
            selected_state = all_states[delete_state -1]
            selected_state.delete()
            print(f"The state of {selected_state.name} has been deleted")
        else:
            print(" Please try again")
    except ValueError: 
        print("Invalid selection. Please try again.")
        
def update_a_state(name, region, population):
    all_states = State.get_all()
    view_all_states()

    try:
        update_state = int(input("Which state would you like to update?: "))
    except ValueError:
        print("Invalid input. Please try again.")
        return

    selected_state = all_states[update_state - 1]

    if selected_state:
        name = input(f"Please enter the updated name: ")
        region = input(f"Please enter the updated region: ")

        try:
            population = int(input("Please enter the updated population: "))
        except ValueError:
            print("Population must be a number")
            return

        selected_state.name = name
        selected_state.region = region
        selected_state.population = population
        selected_state.update()

    else:
        print("State not found. Try again.")

#Cities functions
def view_all_cities():
    all_cities = City.get_all()
    for i, city in enumerate(all_cities, start=1):
        print(f"{i}. {city.name} | Population {city.population}")

def get_cities_by_state(state_id):
    all_cities = City.find_by_state(state_id)
    
    if all_cities:
        print("")
        print(f"Cities: ")
        for i, city in enumerate(all_cities, start=1):
            print("")
            print(f"{i}. {city.name} | Population: {city.city_population}")
            print("")
    else:
        print(f"No cities found for this state.")

def add_a_city():
    pass

def delete_a_city():
    pass

def update_a_city(state_id):
    get_cities_by_state(state_id)
    all_cities = City.find_by_state(state_id)

    if not all_cities:
        print("No cities to display")

    try:
        city_selection = int(input("Please select the city: "))
        selected_city = all_cities[city_selection - 1]
    except (ValueError, IndexError):
        print("Invalid option")
        return

    if selected_city:
        update_name = input(f"Please enter the updated name for {selected_city.name}: ")

        try:
            update_population = input(f"Please enter the updated population for {selected_city.name}: ")
        except ValueError:
            print("Population must be a number")
            return

        selected_city.name = update_name
        selected_city.population = update_population
        selected_city.update()

    else:
        print("State not found. Try again.")

