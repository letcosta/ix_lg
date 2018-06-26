# -*- coding: utf-8 -*-
"""
Here we explain the most common datatypes

@author: manugarri
"""

#%%
"""
python has many types of variables that are a part of the core language, they 
are called primitives.
"""

"""
The most common primitives are strings, numbers (integers and decimals) and booleans
"""

"""
*******************************************************************************
STRINGS
*******************************************************************************
"""
print("We use strings to represent text")

#%%
var_str = 'Hello'
var_str2 = "World!"
print(var_str)
print(var_str2)
print(var_str, var_str2)

print(type(var_str2))

#%%

"""
Strings can be joined to create longer strings. There are many ways to join strings
(this is called string interpolation).
"""

# We can use the simbol `+` to "sum" (concatenate) strings
var_str_joined = var_str + " " + var_str2
print(var_str_joined)

#%%
# We can also "multiply" strings
n = "hello"
print(n * 10)

#%%
"""
We can also use the method `format()` that allows us to insert strings inside other strings
"""

name = "Manuel"
city = "Lisbon"

presentation = "Hi, I'm {}, and I'm from {}"

print(presentation.format(name, city))

#%%

name2 = "Maria"
city2 = "Madrid"
print(presentation.format(name2, city2))

#%%
"""
Python is a language with "batteries included" this means it includes a lot of 
functionalities when we install python.

Those functionalities are usually grouped in packages (or modules) and we can 
"load" them and use them with the keyword `import`

For example, if we want to use the `math` module, that has many mathematical functions,
we can access it if we type `import math`
"""

import math

# Now we can access all the functionalities in the math module
print(math.pi)

#%%
# When using the `format` method we can specify how do we want to format the 
# variables. For example, we can round the variables.

pi_str = "The first digits of pi are: {}".format(math.pi)
print(pi_str)

#%%
# We can print the string rounded to 2 digits
pi_str = "The first digits of pi are: {:.2f}".format(math.pi)
print(pi_str)



#%%
"""
Another method to do string interpolation (python>=3.6) is referencing the variable
directly in the string by using an f-string
"""

presentation2 = f"Hi, I'm {name}, and I'm from {city}"

print(presentation2)

#%%
name = "John"
print(presentation2)

#%%
"""
MORE STRING OPERATIONS
"""

title = "introduction to PYTHON"

print("We can convert a string to uppercase with upper()")
print(title.upper())

#%%
print("We can convert a string to lowercase with lower()")
print(title.lower())

#%%
print("We can convert the first letter to upper case with capitalize()")
print(title.capitalize())

#%%
name_with_commas = ",manuel,"
print("We can use `strip()` to remove characters from the beginning and the end of a string")
print(name_with_commas.strip(","))

#%%
print("We use `replace()` to replace parts of a string for something else")
print(name_with_commas.replace("nuel", "ry"))

#%%
print("We can chain methods together")
print(
      name_with_commas
      .strip(",")
      .replace("nuel", "ry")
      .upper()
)


#%%
# We can split a string in multiple strings by using `split()`

colors_str = "red|yellow|green|blue"
colors_list = colors_str.split("|")
print(colors_list)

#%%
"""
*******************************************************************************
NUMBERS
*******************************************************************************
"""
print("There are two basic numeric primitives in python, int(integers) and float(decimals)")

integer = 23
print(type(integer))

#%%
decimal = 23.1
print(type(decimal))

#%%
print(type(23.))

#%%
print("We can convert numbers to strings easilty")
print(type(str(integer)))
print("two + " + str(decimal))

#%%
print("We can also use numbers in string interpolation")
name = "Manuel"
city = "Lisbon"
age = 34
print(f"Hi, I'm {name}, I'm from {city} and I'm {age} years old")

#%%
print("Similarly, we can convert strings to numbers")
number_string = "24"
print(int(number_string) + 5)
print(float(number_string) + 5)

#%%
print("We have to make sure the numbers are valid!")
invalid_number_string = "24,5"
print(float(invalid_number_string))

#%%
print("We can't convert a float to integer either")
print(int("24.1"))

#%%
"""
OPERATIONS WITH NUMBERS

We can use the basic arithmetic symbols to perform operations with numbers
"""

#sum
print("2+2=",2+2)

#substraction
print("4-9=",4-9)

#multiplication
print("3*2=",3*2)

#division
print("7/2=",7/2)

#%%
"""
There are other operations
"""
a = 7
b = 2
# floor division, do a division and remove the remainder
print(f"{a}//{b}=", a//b)

# modulo, do a division and return the remainder
print(f"{a}%{b}=", a%b)

#negation, change the sign of a number
print(f"negation of {a}=", -a)

#square, cube, fourth power, etcetera
print(f"{a}**{b}=",a**b)

#%%
"""
*******************************************************************************
BOOLEANS
*******************************************************************************

A boolean variable is a primitive that can only be True or False
"""

truth = True
falsehood = False

print(type(truth))

#%%
"""
As an additional primitive we have `None` which is the null variable
"""

null = None
print(type(null))

#%%

#Most variables can be converted to a boolean, usually they are converted to True
print(bool("potato"))


# The null values (0, "", None, and empty lists and dicts) are converted to False
#%%
print(bool(""))
#%%
print(bool(0))
print(bool(null))
print(bool([]))
print(bool({}))

#%%
"""
LOGIC COMPARISONS

We can compare variables, the result of a comparison is always a boolean
"""

a = 7
b = 2
# a greater or equal to b
print(f"{a} > {b}", a > b)
# b smaller or equal to a
print(f"{b}<={a}", b <= a)
# b equals 2
print(f"{b}==2", b == 2)
# a is different than 23
print(f"{a}!=23", a != 23)

#%%
# We can evaluate the opposite of a logic comparisons with `not`
print(f"not {a}!=23", not a != 23)
#%%

# We can evaluate that multiple conditions are true with `and`
print(f"{a}!=23 and {a}<{b}=", a != 23 and a < b)
# We can evaluate that any condition is true with `or`
print(f"{a}!=23 or {b}<{a}=", a != 23 or a < b)

#%%
"""
When we want to check if something is True or False, we dont use `==`, we use `is`
"""

print("truth is True=", truth is True)
