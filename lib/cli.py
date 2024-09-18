from helpers import (
    exit_program,
    display_states
)

def main():
    while True:
        home_options()  # Show the menu
        choice = input("Please select your choice: ")
        
        if choice == "1":
            display_states()  # Display states when user selects option 1
        elif choice == "2":
            exit_program()  # Exit the program when user selects option 2
        else:
            print("You have made an incorrect choice. Please try again.")  # Error message for invalid input

def home_options():
    print("\n SELECT AN OPTION")  # Added newline for better readability
    print("1. View States")
    print("2. Exit the Program")

if __name__ == "__main__":
    main()
