
import os
import requests

from tabulate import tabulate
from utils.ProgramInfo import display_program_info

CURRENT_MENU = "\033[1;4;36mManage Modpack(s)\033[0m"

def manage_modpack():
    # Clear the screen
    os.system("clear")
    # Display program info
    display_program_info(CURRENT_MENU)
    
    # Show selected modpack
    print("\033[0;35mSelected Modpack: n/a\033[0m")
    print("Please input a Modpack name from list or press ENTER to exit:")
    
    # List all modpacks
    modpacks = os.listdir(os.path.join("games", "StardewValley", "modpacks"))
    for i in range(len(modpacks)):
        print("|- " + modpacks[i])
        
    
    selected_modpack = input("\033[1;34mModpack to select:\033[0m ")
    
    # Check to see if the user wants to go back
    if selected_modpack.isspace() or selected_modpack == "":
        exit(1)
    
    # Check to see if the modpack exists
    if not os.path.exists(os.path.join("games", "StardewValley", "modpacks", selected_modpack)):
        print("The modpack does not exist.")
        manage_modpack()
    
    # Clear the screen
    os.system("clear")
    # Display program info
    display_program_info(CURRENT_MENU)
    
    # Show selected modpack
    print("\033[0;35mSelected Modpack: " + selected_modpack + "\033[0m")
    print("\033[0;37m1. Add Mods\033[0m")
    print("\033[0;37m2. Update Mods\033[0m")
    print("\033[0;37m3. Remove Mods\033[0m")
    print("\033[0;37m4. Rename Modpack\033[0m")
    print("\033[0;91m5. Delete Modpack\033[0m")
    print()
    print("\033[0;90m6. Back\033[0m")
    print("\033[0;31m7. Exit\033[0m")
    
    while True:
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            # Perform action for Option 1
            add_mods(selected_modpack)
            break
        elif choice == "2":
            # Perform action for Option 2
            #update_mods(selected_modpack)
            break
        elif choice == "3":
            # Perform action for Option 3
            remove_mods(selected_modpack)
            break
        elif choice == "4":
            # Perform action for Option 4
            rename_modpack(selected_modpack)
            break
        elif choice == "5":
            # Perform action for Option 5
            delete_modpack(selected_modpack)
            break
        elif choice == "6":
            # Go back
            manage_modpack()
        elif choice == "7":
            # Await user confirmation
            confirm = input("Are you sure you want to exit? (Y/n): ")
            if confirm.lower() == "y" or confirm.lower() == "yes" or confirm == "":
                # Exit the program
                print("Exiting...")
                exit(1)  
        else:
            print("Invalid choice. Please try again.")
    
    
    
def add_mods(selected_modpack):
    # Clear the screen
    os.system("clear")
    # Display program info
    display_program_info(CURRENT_MENU)
    # Display selected modpack
    print("\033[0;35mSelected Modpack: " + selected_modpack + "\033[0m")
    
    # Ask for mod to search for on NexusMods
    mod_to_search = input("Enter the name of the mod to search for on NexusMods: ")
    
    # Search for the mod on NexusMods
    # Get the API key from the text file
    with open("nexusmods_api_key_prv.txt", "r") as f:
        API_KEY = f.read()
        # close the file
        f.close()
    
    GAME_DOMAIN_NAME = "stardewvalley"
    
    # Nexus Mods API endpoint for game details
    game_details_url = f'https://api.nexusmods.com/v1/games/{GAME_DOMAIN_NAME}.json'
    
    # Headers for the API request
    headers = {
        'apikey': API_KEY,
        'accept': 'application/json'
    }
    
    # Fetch the game details
    game_details = requests.get(game_details_url, headers=headers)
    # Check if the request was successful
    if game_details.status_code == 200:
        # Get the game ID from the response 
        game_id = game_details.json()['id']
    else:
        print("Failed to fetch game details.")
        # print the status code and the response
        
        # Await user confirmation
        confirm = input("Go back? (Y/n): ")
        if confirm.lower() == "y" or confirm.lower() == "yes" or confirm == "":
            manage_modpack()
        else:
            exit(1)
            
    # Nexus Mods API endpoint for mod search
    mod_search_url = f'https://api.nexusmods.com/v1/games/{GAME_DOMAIN_NAME}/mods/'
    
    # Fetch the mod search results
    mod_search_results = requests.get(mod_search_url, headers=headers)
    # Check if the request was successful
    if mod_search_results.status_code == 200:
        # Get the search results from the response
        search_results = mod_search_results.json()
    else:
        print("Failed to fetch mod search results.")
        # Print the status code and the response
        print(mod_search_results.status_code)
        print(mod_search_results.text)
        # Await user confirmation
        confirm = input("Go back? (Y/n): ")
        if confirm.lower() == "y" or confirm.lower() == "yes" or confirm == "":
            manage_modpack()
        else:
            exit(1)
    
    # Display the search results
    search_results_table = []
    for i in range(len(search_results['results'])):
        search_results_table.append([i+1, search_results['results'][i]['name'], search_results['results'][i]['version'], search_results['results'][i]['author']])
    
    # Display the search results in a table
    print(tabulate(search_results_table, headers=["#", "Name", "Version", "Author"]))
    
    # Ask for the mod to download
    # Download the mod
    # Extract the mod
    # Move the mod to the selected modpack
    # Await user confirmation
    # Go back
    
    
def update_mods(selected_modpack):
    manage_modpack()
    
def remove_mods(selected_modpack):
    # Clear the screen
    os.system("clear")
    # Display program info
    display_program_info(CURRENT_MENU)
    # Display selected modpack
    print("\033[0;35mSelected Modpack: " + selected_modpack + "\033[0m")
    
    deleted_mods = []
    
    # List all mods in the selected modpack
    mods = os.listdir(os.path.join("games", "StardewValley", "modpacks", selected_modpack))
    for i in range(len(mods)):
        print("|- " + mods[i])
        
    # Ask user for the mod or mods to remove
    print("Enter the name of the mod or mods to remove")
    input_mods = input("separate by comma and space eg: mod, mod2): ")
    
    # Check every mod to see if it exists
    input_mods = input_mods.split(", ")
    for mod in input_mods:
        if not os.path.exists(os.path.join("games", "StardewValley", "modpacks", selected_modpack, mod)):
            print("The mod " + mod + " does not exist.")
            # Await user confirmation
            confirm = input("Go back? (Y/n): ")
            if confirm.lower() == "y" or confirm.lower() == "yes" or confirm == "":
                manage_modpack()
            else:
                exit(1)
        else:
            # Keep track of the mods removed
            deleted_mods.append(mod)
            # Remove folder
            os.rmdir(os.path.join("games", "StardewValley", "modpacks", selected_modpack, mod))
    
    # Clear the screen
    os.system("clear")
    # Display program info
    display_program_info(CURRENT_MENU)
    # Display selected modpack
    print("\033[0;35mSelected Modpack: " + selected_modpack + "\033[0m")
    
    # Display the mods removed
    print("Mods removed:")
    for mod in deleted_mods:
        print("|- " + mod)
        
    # Await user confirmation
    confirm = input("Go back? (Y/n): ")
    if confirm.lower() == "y" or confirm.lower() == "yes" or confirm == "":
        manage_modpack()
    else:
        exit(1)

def rename_modpack(selected_modpack_name):
    # Get the name of the path to the selected modpack
    selected_modpack = "./games/StardewValley/modpacks/"+selected_modpack_name
    # Clear the screen
    os.system("clear")
    # Display program info
    display_program_info(CURRENT_MENU)
    # Display selected modpack
    print("\033[0;35mSelected Modpack: " + selected_modpack_name + "\033[0m")
    
    # Rename modpack
    input_name = input("Enter the new name: ")
    
    # Change the name of the selected modpacks directory
    os.rename(selected_modpack, "./games/StardewValley/modpacks/"+input_name)
    
    # Clear the screen
    os.system("clear")
    # Display program info
    display_program_info(CURRENT_MENU)
    # Display selected modpack
    print("\033[0;35mSelected Modpack: " + input_name + "\033[0m")
    
    # Await user input for confirmation
    confirm = input("Go back? (Y/n): ")
    if confirm.lower() == "y" or confirm.lower() == "yes" or confirm == "":
        manage_modpack()
    else:
        exit(1)
    
    
def delete_modpack(selected_modpack_name):
    # Get the name of the path to the selected modpack
    selected_modpack = "./games/StardewValley/modpacks/"+selected_modpack_name
    # Clear the screen
    os.system("clear")
    # Display program info
    display_program_info(CURRENT_MENU)
    # Display selected modpack
    print("\033[0;35mSelected Modpack: " + selected_modpack_name + "\033[0m")
    
    # Confirm deletion
    confirm = input("Are you sure you want to delete the modpack? (Y/n): ")
    if confirm.lower() == "y" or confirm.lower() == "yes" or confirm == "":
        # Delete the modpack
        os.rmdir("./games/StardewValley/modpacks/"+selected_modpack_name)
        
        print("Modpack deleted.")
        # Await user input for confirmation
        confirm = input("Go back? (Y/n): ")
        if confirm.lower() == "y" or confirm.lower() == "yes" or confirm == "":
            manage_modpack()
        else:
            exit(1)
    else:
        # Go back
        manage_modpack()
    
