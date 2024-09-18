from __init__ import CURSOR, CONN
from state import State

class City: 
    def __init__(self, name, city_population, state_id, id=None):
        self.name = name
        self.city_population = city_population
        self.id = id
        self.state_id = state_id


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def city_population(self):
        return self._city_population

    @city_population.setter
    def city_population(self, city_population):
        if isinstance(city_population, int):
            self._city_population = city_population
        else:
            raise ValueError("Population must be an integer")

    @property
    def state_id(self):
        return self._state_id

    @state_id.setter
    def state_id(self, state_id):
        if isinstance(state_id, int) and State.find_by_id(state_id):
            self._state_id = state_id
        else:
            raise ValueError("state_id must reference a valid state in the database")
            
