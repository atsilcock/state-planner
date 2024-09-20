from models.state import State
from models.city import City

# State operations
def get_states():
    return State.get_all()

def find_state_by_name(name):
    return State.find_by_name(name)

def add_state(name, population, region):
    state = State(name, population, region)
    state.save()

def delete_state(name):
    state = find_state_by_name(name)
    if state:
        state.delete()
        print(f"State '{state.name}' deleted successfully.")
    else:
        print(f"State '{name}' not found.")

def update_state(state, name, population, region):
    state.name = name
    state.population = population
    state.region = region
    state.update()

def view_all_states():
    states = get_states()
    if states:
        for i, state in enumerate(states, start=1):
            print(f"{i}. {state.name} | Population: {state.population} | Region: {state.region}")
    else:
        print("No states found.")

# City operations
def get_cities_by_state(state_id):
    return City.find_by_state(state_id)

def add_city(name, population, state_id):
    city = City(name, population, state_id)
    city.save()

def delete_city(state_id, name):
    cities = City.find_by_state(state_id)
    for city in cities:
        if city.name.lower() == name.lower():
            city_to_delete = city
            break
    if city_to_delete:
        city_to_delete.delete()
        print(f"City '{city_to_delete.name}' deleted successfully.")
    else:
        print(f"City '{name}' not found.")

def update_city(city, name, population):
    city.name = name
    city.city_population = population
    city.update()


