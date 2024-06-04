import os
from utils.ProgramInfo import display_program_info
from utils.submenu.CreateModpack import create_modpack
from utils.submenu.ManageModpack import manage_modpack

CURRENT_MENU = "\033[1;4;36mMain Menu\033[0m"

def main_menu():
    # Clear the screen
    os.system("clear")
    # Display program info
    display_program_info(CURRENT_MENU)
    
    # Main Menu
    print("Please select an option:")
    print("\033[0;37m1. Create Modpack\033[0m")
    print("\033[0;37m2. Manage Modpack\033[0m")
    print("\033[0;37m3. Option 3\033[0m")
    print()
    print("\033[0;31m4. Exit\033[0m")

    while True:
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            # Perform action for Option 1
            create_modpack()
        elif choice == "2":
            # Perform action for Option 2
            manage_modpack()
        elif choice == "3":
            # Perform action for Option 3
            print("Option 3 selected")
        elif choice == "4":
            # Await user confirmation
            confirm = input("Are you sure you want to exit? (Y/n): ")
            if confirm.lower() == "y" or confirm.lower() == "yes" or confirm == "":
                # Exit the program
                print("Exiting...")
                break
        else:
            print("Invalid choice. Please try again.")
