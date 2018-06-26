# -*- coding: utf-8 -*-
"""
Here we can put code that can be imported from other modules (or the REPL, or the terminal)

When a script is getting too long, that usally means there is too much stuff going
on it, this can cause problems and make it harder to manage.
A good practice is to split the script into different modules (e.g. , .py files)
grouped by their logic.

@author: manugarri
"""


def greet_function(name):
    print("Hi {}, this function is being imported from the module {}, {}".format(name, __file__, __name__))


def congratulate_function(name):
    print("¡Congratulations {}, yaaay!".format(name))


def main():
    """We can also call this script directly!"""
    greet_function("You")


if __name__ == "__main__":
    main()
