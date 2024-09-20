



def view_all_states():
    all_states = State.get_all()
    for i, state in enumerate(all_states, start=1):
        print(f"{i}. {state.name} | Population {state.population} | Region {state.region}")