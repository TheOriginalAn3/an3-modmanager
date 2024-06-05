import os
from toa3_modmanager import PROGRAM_NAME, PROGRAM_AUTHOR, PROGRAM_VERSION


def display_program_info():
    # Print the version of this program, and the author in color
    print(PROGRAM_NAME + " " + PROGRAM_VERSION)
    print(PROGRAM_AUTHOR)
    
def display_program_info(CURRENT_MENU):
    # Print the version of this program, and the author in color
    print(PROGRAM_NAME + " " + PROGRAM_VERSION)
    print(PROGRAM_AUTHOR)
    print(CURRENT_MENU)
    
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_unique_name(base_name, path):
    index = 1
    unique_name = base_name
    while os.path.exists(os.path.join(path, unique_name)):
        unique_name = f"{base_name}_{index}"
        index += 1
    return unique_name
