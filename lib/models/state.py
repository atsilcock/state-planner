from __init__ import CURSOR, CONN

class State: 
    def __init__(self, name, population, region, id=None):
        self.name = name
        self.population = population
        self.region = region
        self.id = id

# Table Classes (create table, drop table, alter table, delete table)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS states (
            id INTEGER PRIMARY KEY,
            name TEXT,
            population INT, 
            region TXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql= "DROP TABLE IF NOT EXISTS states"

        CURSOR.execute(sql)
        CONN.commit()


# Getter & Setter Function         

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if  not 1<= len(name) <= 15:
            raise Exception("Length must be between 1 and 15 characters")
        self._name = name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, population):
        if not isinstance(population,int): 
            raise Exception("Population must be an Integer")
        self._population = population

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if not isinstance(region, str):
            raise Exception("Region must be a string")
        self._region = region


#create crud defitions
# ADD (save), DELETE, ALTER (update)

    def save(self):
        sql = """
            INSERT INTO states (name, population, region)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.population, self.region))
        CONN.commit()

        self.id = CURSOR.lastrowid

    
    def delete(self): 
        sql = "DELETE FROM states WHERE id = ?" 

        CURSOR.execute(sql, (self.id))
        CONN.commit()

        self.id = None 

    def update(self):
        sql= "UPDATE states SET name = ?, population =?, region = ? WHERE id = ?"

        CURSOR.execute(sql, (self.name, self.population, self.region, self.id))
        CONN.commit()




    









    
        


    