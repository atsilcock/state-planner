from helpers import (
    view_all_states, 
    add_a_state, 
    delete_a_state, 
    update_a_state, 
    get_cities_by_state

)

def main(): 
    while True:
        print("")
        view_all_states()
        print("")
        main_menu()
        try: 
            choice = input("Enter your choice: ")
            print("")

            if choice == "1":
                view_all_states()
            elif choice == "2":
                add_a_state("name", "population", "region")
            elif choice == "3":
                delete_a_state("name")
            elif choice == "4":
                update_a_state("name", "region", "population")
            elif choice == "5":
                get_cities_by_state("state_id")
            else:
                if choice == "e":
                    exit_program()
                    break
        except ValueError:
            print("Invalid input. Please try again.")

def exit_program():
    print("You are now leaving - Goodbye!")

def main_menu():
    stars()
    print("1. View all states")
    print("2. Add a state")
    print("3. Delete a state")
    print("4. Update a state")
    print("5. Select State to view its cities")
    stars()

def stars():
    print("******************")

if __name__ == "__main__":
    main()
