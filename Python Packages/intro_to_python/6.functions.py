# -*- coding: utf-8 -*-
"""
Here we explain functions in python

@author: manugarri
"""

"""
Python scripts are executed line by line

Functions are a way to separate logic in pieces instead of having to execute 
everything line after line. They are also a good way to reuse pieces of code that we
use multiple times
"""

"""
Functions are defined this way:

def function_name(argument1, argument2,...):
    function logic goes here

"""
#%%
def greet():
    print("Hello World!")


# Now we don't have to type print every single time we want to greet.
print(type(greet))
greet()
#%%

# Main reason to use functions is that they accept arguments, and make our code more flexible

def greet(name):
    print(f"Hello {name}, how are you?")

greet("Manuel")
greet("John")

#%%
# This function now requires an argument, if we call it without an argument it
# will throw an error
greet()

#%%
# We can define default values for arguments, this way we can call the function
# without argument
def greet_forgot_name(name="friend"):
    greet(name)

greet_forgot_name("Manuel")
greet_forgot_name()

#%%
# Functions can return a value.

def sum_numbers(a, b):
    return a + b # we return this
    print("This will never get printed, function stops at return")

sum_result1 = sum_numbers(2.5, 5)
print(sum_result1)

#%%
# Now we can use the result as input for another function
sum_result2 = sum_numbers(sum_result1, 50)
print(sum_result2)

#%%
# A function that doesnt have a return will return None
def wrong_sum(a, b):
    results = a + b

result_sum3 = wrong_sum(2.5, 5)
print(result_sum3)


#%% Functions only return once, but they can return multiple things

def sum_and_substract(a, b):
    sum_result = a + b
    substract_result = a - b
    return sum_result, substract_result

result = sum_and_substract(10, 5)
print(result)
print(type(result))

#%%
# if we expect multiple return values, we can unpack them into multiple variablers
sum_result, substract_result = sum_and_substract(10, 5)
print(sum_result)
print(substract_result)


#%%
"""
There is another way to define functions, we call them lambda functions (anonymous functions)

lambda functions are defined:
func_lambda = lambda input: output

lambda functions are usually used in those cases where we want to apply simple
logic and we dont want to define a function
"""

sum_lambda = lambda a, b: a + b
sum_result1 = sum_lambda(2.5, 5)
print(sum_result1)

#%%
# Now we can use the result of the lambda function the same way we would do with
# a regular function
sum_result2 = sum_lambda(sum_result1, 50)
print(sum_result2)


#%%
"""
******************************************************************************

EXERCISES

******************************************************************************
"""

#%%
"""
 Create a function that substract 2 numbers and returns the result

"""

#%%
"""
 Create a function that substract 2 numbers and returns the result
"""

#%%
"""
 Create a function that takes 3 arguments, 2 numbers and a string. If the string
 is "sum", return the sum of the two numbers, if the string is "substract", 
 return the substraction
"""

#%%
"""
 Create a function that asks the user for a phrase and returns the phrase
 with the words reversed
 For example if the user writes "Green eggs and ham", the function would
 return "han and eggs Green"
"""

#%% 
"""
Create a function that detects if a word phrase is a palindrome (a phrase
is a palindrome if its read same way if read backwards. Ignore punctuation symbols.

For example, "A car a man a maraca" would return True
"""

#%%
"""
 Create a function that given a list of lists, returns a simple list (that is 
 a list with no lists inside it)

 for example, if we call this function with the argument

 nested_list = [
        [1,2,3],
        [4,5, 6, 7],
        [8, 9]
 ]

 the function will return the list [1,2,3,4,5,6,7,8,9]
"""




