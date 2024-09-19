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
    for i, in enumerate(cities, start =1):
        print(f"{i}. {cities.name} | Population {cities.population}")


def delete_city():
    pass

def delete_state(id):
    states = get_states()
    for i, state in enumerate(states):
        if state.id == id:
            state.delete()
            print(f"State with id {id} has been deleted.")
            return
    print(f"State with id {id} not found.")


def update_state():
    return State.update()


