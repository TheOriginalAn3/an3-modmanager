import os

# Get the current directory
current_directory = os.getcwd()

# Specify the name of the new folder
games_folder = "games"
modpacks_folder = "modpacks"
mods_folder = "mods"

#TODO: Add support for multiple games
# Create the new folder
new_folder_path = os.path.join(current_directory, games_folder, "StardewValley", modpacks_folder)
os.makedirs(new_folder_path)

print("Folder created successfully!")