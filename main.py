import os
from utils.MainMenu import main_menu

def main():
    """
    Print the version of this program, and the author in color.
    The color codes are ANSI escape codes.
    
    Meaning of the color codes:
    - 0;32;40m: green
    - 0;33;40m: yellow
    - 0;31;40m: red
    - 0;34;40m: blue
    - 0;35;40m: purple
    - 0;36;40m: cyan
    - 0;37;40m: white
    - 0;30;40m: black
    - 0;90;40m: dark gray
    - 0;91;40m: light red
    - 0;92;40m: light green
    - 0;93;40m: light yellow
    
    Formatting codes:
    - bold, add a 1 before the color code.
    - italic, add a 3 before the color code.
    - underlined, add a 4 before the color code.
    - blink, add a 5 before the color code.
    - invisible, add a 8 before the color code.
    - crossed out, add a 9 before the color code.
    - To add a background color, add a 4 after the color code.
    - For bold and underlined, add a 1;4 before the color code.
    
    To reset the color, use the code 0m.
    To reset the color and other text attributes, use the code 0;0m.
    
    """
    
    # Clear the screen
    os.system("clear")

    # Call Main Menu
    main_menu()

if __name__ == "__main__":
    main()