from models.state import State
from models.city import City


def exit_program():
    print("")
    print("We can't wait for you to plan your next vacation!")
    print("")
    exit()

def get_states():
    return State.get_all()

def add_state(name, population, region):
    new_state = State(name, population, region)
    new_state.save()
    return new_state


def list_states(states):
    for i, state in enumerate(states, start=1):
        print(f"{i}. {state.name} | Population: {state.population} | Region: {state.region} ")

def display_states():
    states = get_states()
    if states:
        list_states(states)
    else:
        print("No states available.")

def display_state_details():
    return City.get_all

def list_cities(cities):
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city.name} | Population {city.city_population}")


def delete_city():
    pass

def delete_state(id):
    state = find_state(id)
    if state:   
        state.delete()
        print(f"State with id {id} has been deleted.")
    else:
        stars()
        print("No state matches the number that you have choosen. Please try again.")
        stars()

def update_state(id, name, population, region):
    state = find_state(id)
    if state:
        state.name = name
        state.population = population
        state.region = region
        state.update()
    else:
        print("State was not found")

def find_state(id):
    states = get_states()
    for state in states:
        if state.id == id:
            return state
    return None

def find_cities_by_state(state_id):
    return City.find_by_state(state_id)


def stars():
    print ("***********************")