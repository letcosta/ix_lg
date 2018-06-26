# -*- coding: utf-8 -*-
"""
This is the module doctstring, here we explain the logic included in the file.

Example:
    This script, when executed, if the first argument is "greet" and the second
    a name it will greet that name

@author: manugarri
"""
# Imports are usually located at the top of the script
import sys
from greeting_module import greet_function, congratulate_function


def parse_arguments():
    arguments = sys.argv[1:]
    return arguments


def main(arguments):
    """
    Here would go the main functionality of our script
    """
    name = arguments[1]
    if arguments[0] == "greet":
        greet_function(name)
    elif arguments[0] == "congratulate":
        congratulate_function(name)


if __name__ == "__main__":
    # This code will only be executed if this file is called from the terminal directly
    arguments = parse_arguments()
    print("Arguments passed to the script: ", arguments)
    main(arguments)
