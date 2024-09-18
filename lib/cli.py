from helpers import (
    exit_program,
    display_states
)

def main():
    while True:
        options()
        choice = ">"
        if choice == "1":
            display_states()
        elif choice == "2":
            exit_program()
        else:
            print("You have made an incorrect choice")
    

def options():
    print("SELECT AND OPTION")
    print("1. Select the State")
    print("2. Exit the Prorgram")

if __name__ == "__main__":
    main()
