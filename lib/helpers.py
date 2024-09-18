from models.state import State

def display_state():
    states = State.get_all()
    if states:
        print("All States: ")
        for state in states:
            print(f"- {state.name} (Poplation: {state.population} | Region: {state.region})")
        else:
            print("No States found")

def exit_program():
    print("Goodbye!")
    exit()