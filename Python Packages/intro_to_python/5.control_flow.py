# -*- coding: utf-8 -*-
"""
Here we talk about control flow

@author: manugarri
"""


"""
*******************************************************************************
IF-ELSE
*******************************************************************************

We use if-else to take decissions and execute different parts of the code depending
on a condition


NOTE: in python, the way we declare we are inside a loop (or a function) is by indenting,
that is, if we are inside an if-else loop we put the code inside the loop 4 spaces to the right
(in Spyder you can press tab to insert 4 spaces automatically)
"""
#%%
# We can use an if loop to execute something based on one condition
temperature = 95

if temperature <= 65:
    #we indent this line to declare that it is inside the if loop
    print("Better get a sweater, its chilly out")
print("this gets printed no matter what")
#%%
"""
 If we want to add many different conditions to an if loop we can use if-else
"""

temperature = 50


if temperature <= 30:
    mom_answer = "Get a coat, its freezing outside!"
elif temperature <= 65:
    mom_answer = "Get a sweater, its chilly out!"
elif temperature <= 85:
    mom_answer = "Don't come back late!"
# The else block will run only if none of the previous conditions take place
else:
    mom_answer = "Its too hot out!"

print(mom_answer)

#%%
# We can insert loops inside other loops (nested loops)


temperature = 75
rain = True

if 65 < temperature and temperature < 85:
    # True evaluates to True, using not we get the opposite
    if not rain:
        print("Let's go picnic!")
#%%
"""
*******************************************************************************
FOR LOOPS
*******************************************************************************

FOR loops are used to iterate the elements of a list one by one(or anything that is iterable)
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 80, 9, 10]

for n in numbers:
    if n <= 10:
        print(f"valid number {n}")
    else:
        print(f"ERROR! number {n} greater than 10")

#%%
"""
 Sometimes we want to break a for loop if a condition happens, we can break a loop
 with the keyword `break`
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 80, 9, 10]

for n in numbers:
    if n <= 10:
        print(f"valid number {n}")
    else:
        print(f"ERROR! number {n} greater than 10. EXITING THE LOOP")
        break

#%%
# There are times where we dont want to break a loop, we just want to continue if
# something happens and do nothing, we can use `pass` for this

numbers = [1, 2, 3, 4, 5, 6, 7, 80, 9, 10]

for n in numbers:
    if n <= 10:
        print(f"valid number {n}")
    else:
        # pass is a placeholder, we have to put something inside an else block
        # we use pass so nothing happens.
        pass


#%%
# continue, opposite to pass, will skip this loop iteration and go to the next one

numeros = [1, 2, 3, 4, 5, 6, 7, 80, 9, 10]

for n in numbers:
    if n <= 10:
        print(f"valid number {n}")
    else:
        continue
        print("this will never get printed")

#%%
# A simplified way to iterate elements in a list is using a list comprehension

[number for number in numbers if number <= 10]

#%%
inventory = {
        "peaches": 3,
        "strawberries": 1,
        "apples": 4
        }

# We can iterate the keys in a dictionary with a for loop
for fruit in inventory:
    print(fruit)

#%%
# We can iterate the keys and values together if we use `.items()`:
for fruit, amount in inventory.items():
    print(fruit, amount)
    print("We have{} kilo/s of {}".format(amount, fruit))

#%%
# We can iterate strings too! (remember, strings are just lists of characters).

name = "LISBON"

for letter in name:
    print("GIVE ME A {}!".format(letter))

#%%
"""
*******************************************************************************
TRY-EXCEPT
*******************************************************************************
Sometimes scripts fail, they throw an exception. Usually this means that the 
program stops its execution (and we lose all the stuff that was doing).
We can avoid a program, stopping because of an error by "catching" that execption.
We use a try-except block for this.
"""

#%% 
number_str = "10.5"

try:
    # We try to do this
    number_int = int(number_str)
except Exception as e: #but if it fails, don't stop and do this instead.
    print("Error!")

#%%
"""

IMPORTANT! Anytime we capture an exception, it is recommended that at least we print
the error message.
This way at least we can check that the program is not failing catastrophically  and 
we can fix the error.
It is ok to use this approach when we are starting to build a project.
"""
number_str = "10.5"

try:
    number_int = int(number_str)
except Exception as e: #Exception is a python object
    print("Error, the  value {} can't be converted to an integer".format(number_str))
    print("The error message:")
    print(e, type(e))

#%%
"""
 The problem with capturing all errors in our program is that we can be ignoring
 errors that could have dangerous consecuences.
 The appropiate way to handle errors is to catch those errors that we are aware of,
 and that we know we can handle, and let the rest fail. 
"""
number_str = "10.5"

try:
    number_int = int(number_str)
except ValueError: # We will catch ValueErrors but not other kinds of errors
    print("Error: the value {} can't be converted to integer".format(number_str))

#%%
"""
*******************************************************************************
WHILE
*******************************************************************************

While loops continue running until a condition takes place
"""

n_beer_bottles = 99
while n_beer_bottles > 0:
    print("""
        🎜🎝♩ {} bottles of beer on the wall, {} bottles of beer.
        Take one down and pass it around, {} bottles of beer on the wall.🎜🎝♩
        """.format(n_beer_bottles, n_beer_bottles, n_beer_bottles - 1))
    n_beer_bottles -= 1

#%%
"""
 We need to be carefull when using a while loop, we might get stuck in an INFINITE LOOP!
 (use CTRL+z to exit the execution)
"""
n = 1
while n > 0:
    print("Stuck in the loop!")

#%%
"""
 A common use case for a while loop is to validate user input
 we can get user input with the function `input()`
"""

while 1:
    input_user = input("Write a number from 1 to 10, type 'exit' to exit: ")
    try:
        if input_user == "exit":
            print("Bye!")
            break
        elif int(input_user) <= 10:
            square = int(input_user) ** 2
            print("The square of number {} is {}".format(input_user, square))
        else:
            print("the value {} is not valid".format(input_user))
    except ValueError:
        print("Error: the value {} can't be converted to an integer".format(input_user))
#%%

"""
******************************************************************************

EXERCISES

******************************************************************************
"""

#%%
# Given the dictionary
days_week = {
       "monday": 1,
       "tuesday": 2,
       "wednesday": 3,
       "thursday": 4,
       "friday": 5,
       "saturday": 6,
       "sunday": 7
       }

#%%
"""
turn all of the keys to uppercase, using a for loop.
"""

#%%
"""
# Create a list containing all of the keys in the dictionary that have the letter "r"

"""
