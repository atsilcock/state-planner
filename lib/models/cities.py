class City: 
    def __init__(self, name, city_population, id=None):
        self.name = name
        self.city_population = city_population
        self.id = id


    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str): 
            raise Exception ("Name must be a string")
        self._name = name

    @property
    def city_population(self):
        return self._city_population
    
    @city_population.setter
    def city_population(self, city_population):
        if not isinstance(city_population, int):
            raise Exception("Popluation must be a Integer")
        self._city_population = city_population
            
