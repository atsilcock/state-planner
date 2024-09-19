from models.__init__ import CONN, CURSOR
from models.city import City
from models.state import State

def seed_database():
    City.drop_table()
    City.create_table()
    State.drop_table()
    State.create_table()


# Add states for testing
    State.create("California", 39538223, "West")
    State.create("Texas", 29145505, "South")
    State.create("Florida", 21538187, "Southeast")
    State.create("New York", 20201249, "Northeast")

seed_database()