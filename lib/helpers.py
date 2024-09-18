from models.state import State

def display_states():
    states = State.get_all()
    if states:
        print("\nAll States:")  # Added newline for better output formatting
        for state in states:
            print(f"\n {state.name} | Population: {state.population} | Region: {state.region})")
    else:
        print("No States found")

def exit_program():
    print("Goodbye!")
    exit()
