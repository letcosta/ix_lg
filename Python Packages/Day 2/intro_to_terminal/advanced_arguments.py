# -*- coding: utf-8 -*-
"""
Here we are going to explain how to use advanced script arguments

@author: manugarri
"""

# Imports are usually located at the top of the script
import argparse
from greeting_module import greet_function, congratulate_function


def parse_arguments_advanced():
    parser = argparse.ArgumentParser(
        description="Script Description"
    )

    parser.add_argument("method", help="""
                        Indicates the greeting method to use
                        Valid methods are "greet" or "congratulate"
                        """, choices=["greet", "congratulate"])

    parser.add_argument("name", help="""
                        Indicates the name of the user we want to greet
                        """)

    parser.add_argument("--capitalize", help="Capitalizes the user's name",
                    action="store_true")
    arguments = parser.parse_args()
    return arguments


def main(arguments):
    """
    Here would go the main functionality of our script
    """
    name = arguments.name
    if arguments.capitalize:
        name = name.capitalize()
    if arguments.method == "greet":
        greet_function(name)
    elif arguments.method == "congratulate":
        congratulate_function(name)


if __name__ == "__main__":
    # This code will only be executed if this file is called from the terminal directly
    arguments = parse_arguments_advanced()
    print("Arguments passed to the script: ", arguments)
    main(arguments)
