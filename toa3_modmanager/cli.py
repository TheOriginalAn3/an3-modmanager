from math import log
import os
from .logger import get_logger
from .utils import display_program_info
from .manager import create_modpack
from .manager import manage_modpack

CURRENT_MENU = "\033[1;4;36mMain Menu\033[0m"
logger = get_logger(__name__)

def main_menu():
    # Clear the screen
    os.system("clear")
    # Display program info
    display_program_info(CURRENT_MENU)
    
    # Main Menu
    print(
    '''
    Please select an option:
    \033[0;37m1. Create Modpack\033[0m
    \033[0;37m2. Manage Modpack\033[0m
    \033[0;37m3. Option 3\033[0m
    
    \033[0;31m4. Exit\033[0m
    '''
    )
    
    logger.info("Main Menu displayed")
    logger.info("Awaiting user input")
    while True:
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            # Perform action for Option 1
            logger.info("Option 1 (Create Modpack) selected")
            create_modpack()
        elif choice == "2":
            # Perform action for Option 2
            logger.info("Option 2 (Manage Modpack) selected")
            manage_modpack()
        elif choice == "3":
            # Perform action for Option 3
            logger.info("Option 3 (-) selected")
            print("Option 3 selected")
        elif choice == "4":
            # Await user confirmation
            logger.info("Option 4 (Exit) selected")
            confirm = input("Are you sure you want to exit? (Y/n): ")
            if confirm.lower() == "y" or confirm.lower() == "yes" or confirm == "":
                # Exit the program
                print("Exiting...")
                break
        else:
            print("Invalid choice. Please try again.")
            logger.warning("Invalid choice. Please try again.")
