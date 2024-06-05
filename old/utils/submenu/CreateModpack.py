import os

from utils.ProgramInfo import display_program_info
from utils.submenu.ManageModpack import manage_modpack

CURRENT_MENU = "\033[1;4;36mCreate Modpack\033[0m"

def create_modpack():
    # Clear the screen
    os.system("clear")
    # Display program info
    display_program_info(CURRENT_MENU)
    
    # Create Modpack
    path = ""
    print("Please enter the name of the modpack:")
    print("Ctrl+C to terminate the program. Or press ENTER to go to the main menu.")
    name = input("Name: ")
    
    # Check to see if the name is valid or already exists
    if name == "":
        return manage_modpack()
    if name.isspace():
        return create_modpack()
    if os.path.exists(os.path.join("games", "StardewValley", "modpacks", name)):
        print("The name already exists, adding number to the name.")
        
        # Check to see what number to add to the name
        i = 1
        while os.path.exists(os.path.join("games", "StardewValley", "modpacks", name + "(" + str(i) + ")")):
            i += 1
        
        path = os.path.join("games", "StardewValley", "modpacks", name + "(" + str(i) + ")")
        os.makedirs(path)
    else:
        path = os.path.join("games", "StardewValley", "modpacks", name)
        os.makedirs(path)
    
    manage_modpack()
    