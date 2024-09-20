from models.state import State
from models.city import City


def exit_program():
    print("")
    print("We can't wait for you to plan your next vacation!")
    print("")
    exit()

#States

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


def get_cities():
    return City.get_all()


def add_city(name, city_population, state_id):
    new_city = City(name, city_population, state_id)
    new_city.save()
    return new_city

def delete_state_by_number(states, number):
    state_to_delete = states[number - 1]
    state_to_delete.delete()
    print(f"State '{state_to_delete.name}' has been deleted.")

def update_state(id, name, population, region):
    state = find_state(id)
    if state:
        state.name = name
        state.population = population
        state.region = region
        state.update()
    else:
        print("State was not found")


def find_state(name):
    states = get_states()
    for state in states:
        if state.name.lower() == name.lower():  # Case-insensitive match
            return state
    return None

#Cities 

def list_cities(cities):
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city.name} | Population {city.city_population}")

def delete_city_by_number(cities, number):
    city_to_delete = cities[number - 1]
    city_to_delete.delete()
    print(f"City '{city_to_delete.name}' has been deleted.")

def update_city_by_number(cities, number, name, population):
    city_to_update = cities[number - 1]
    city_to_update.name = name
    city_to_update.city_population = population
    city_to_update.update()
    print(f"City '{city_to_update.name}' has been updated.")

def update_state_by_name(states, name, new_name, population, region):
    for state in states:
        if state.name.lower() == name.lower(): 
            updated_state = state
            break

    if updated_state:
        updated_state.name = new_name
        updated_state.population = population
        updated_state.region = region
        updated_state.update() #updating the database in our system
        print(f"State '{updated_state.name}' has been updated.")
        return updated_state 
    return None           

def update_city(id, name, population):
    city = find_city(id)
    if city:
        city.name = name
        city.city_population = population
        city.update()
    else:
        print("City was not found")


def find_city(state_id):
    cities = get_cities()
    for city in cities:
        if city.state_id == state_id:
            return city
    return None

def find_cities_by_state(state_id):
    return City.find_by_state(state_id)


def stars():
    print ("***********************")