from models.state import State
from models.city import City

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
    except ValueError: 
        print("Invalid selection. Please try again.")
        return

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

def get_cities_by_state(state_id):
    all_states = State.get_all()
    view_all_states()
    try:
        select_state_to_view_cities = int(input("Choose the state which you would like to view the cities for: "))
    except ValueError:
        print("Invalid input. Please try again.")
        return

    all_cities = City.get_cities_by_state(select_state_to_view_cities)
    if all_cities:
        for i, city in enumerate(all_cities, start=1):
            print(f"{i}. {city.name} | Population: {city.city_population}")
    else:
        print(f"No cities found for this state.")
