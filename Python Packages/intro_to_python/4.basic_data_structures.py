# -*- coding: utf-8 -*-
"""
Here we talk about basic data structures

@author: manugarri
"""

"""
Data structures are those objects we use to store information (data)
There are many different types, here we are going to see the basics
"""

"""
*******************************************************************************
LISTS
*******************************************************************************

Lists are ordered groups of elements where each list has a position
"""

#%%
fruits = ["orange", "apple", "pear", "strawberry"]

print(fruits)

print(type(fruits))
#%%
# We access elements in a list with brackets []
# The index (position) for python lists starts at 0, this means we access the first
# element by [0]

first_fruit = fruits[0]
print(first_fruit)
#%%
# We can access a range of elements by doing [start:end-1:order]
print(fruits[:2])
#%%
# get the elements after the second one
print(fruits[2:])
#%%
"""We can select ranges starting  from the last one by using negative numbers
For example, we can get the last 2 elements by doing:
"""
print(fruits[-2:])
#%%
# We can skip elements by using [::n], for example, if we just want to select the odd elements:
print(fruits[::2])

#%%
# if we use a negative number  for the order we will get the list reversed
print(fruits[::-1])

#%%
# We can see the number of elements in a list with `len`
print(len(fruits))
#%%
# We can add elements to the end of a list with `append()`.
fruits.append("melon")
print(fruits)

#%%
fruits.append(5)
#%%
fruits.extend(["pineapple", "grape"])

#%%

#%%
# we can repeat a list multiplying it by a number
print(fruits * 2)
#%%
# We can add lists together with `+`
cities = ["Lisbon", "Porto"]
print(fruits + cities) # Prints concatenated lists

#%%
# We can modify elements in a list
fruits[0] = "mango"
print(fruits)
#%%
# We can extend a list regardless of its initial size
fruits[3:] = ["banana", "fig", "pommegranate", "watermelon"]
print(fruits)


#%% 
vegetables = ["tomato", "lettuce"]
#%%
# we can check if an element exists on a list
print(fruits)
print("tomato" in vegetables)

#%%
print("tomato" in fruits)
#%%
# We can find the position of an element on a list

fruits = ["orange", "apple", "pear", "strawberry"]

print(fruits)

print("Position on the list for the word pear is {}".format(fruits.index("pear")))
#%%

# we can remove an element at a specific position from a list with `pop()`

a = fruits.pop(2)
print(fruits)
print(a)
#%%

# So combining index and pop we can remove a specific element from a list
index_orange = fruits.index("orange")
fruits.pop(index_orange)
print(fruits)
#%%
# lists can be sorted with the method `sort()`

ages = [23, 33, 10,54,65,34,25]
ages.sort()
print(ages)
#%%
fruits = ["orange", "apple", "pear", "strawberry"]

print(fruits.sort())
print(fruits)
#%%
# We can generate lists of numbers with `range()`

#%% 
range(10)
#%%
print(list(range(10)))
#%%
# strings can be considered lists of letters, and can be accessed same the way as lists

name = "Manuel"

print(name[0])
print(name[2:])


#%%
len(name)

#%%
"""
We can convert lists to strings with `.join()`
"""

fruits = ["orange", "apple", "pear", "strawberry"]

comma_separated_fruits = ",".join(fruits)

print(comma_separated_fruits)
print(type(comma_separated_fruits))
#%%
line_separated_fruits = "\n".join(fruits)

print("Shopping list: {}".format(line_separated_fruits))


#%%
"""
*******************************************************************************
TUPLES
*******************************************************************************

Tuples are like lists, but once created can't be modified

"""
musketeers = ("Athos", "Porthos", "Aramis")
print(type(musketeers))
print(musketeers)

#%%
# We can access tuple elements like we do with lists
print(musketeers[1:])

#%%
# however, we can't modify a tuple
musketeers[3] = "D'artagnan"

#%%
a = 5,4

print(type(a))

#%%
"""
*******************************************************************************
Dictionaries
*******************************************************************************

Dictionaries are pairs of keys associated to values. We can easily (and fast) a value
if we know its associated key
"""

inventory = {
        "peaches": 3,
        "strawberries": 1,
        "apples": 4
        }
print(type(inventory))
print(inventory)
#%%

# We can see all the keys in a dictionary with `keys()`
print(inventory.keys())
#%%
# the method `keys()` doesnt return a list, if we want to access the keys like a 
# list we need to convert them to a list

# this will fail
print(inventory.keys()[0])
#%%
print(list(inventory.keys())[0])
#%%
# Similarly, we can see the values in a dictionary with `values()`
print(inventory.values())
#%%
# We can read the value associated with a specific key with brackets
print(inventory["strawberries"])
#%%
# If the key doesnt exist it will throw an error (KeyError)
print(inventory["melon"])
#%%
# We can check if a key exists in a dictionary
print("melon" in inventory)
print("peaches" in inventory)

#%%
# We can remove a key from a dictionary with `pop()`

kilos_strawberries = inventory.pop("strawberries")
print("We have {} kilos of strawberries".format(kilos_strawberries))
print(inventory)

#%%
# Each data structure can store other data structures!

# a list with lists inside
flights =[
        ["Lisbon", "New York City"],
        ["Lisbon", "Madrid"],
        ["Madrid", "Paris"],
        ["Madrid", "Berlin"]
        ] 

print(flights[1][1])
#%%
# a dictionary with tuples and lists as values
dict_flights = {
        "Madrid": ("Lisbon", "Paris", "Berlin"),
        "Lisbon": ("New York City", "Madrid")
        }


print(dict_flights["Madrid"])

#%%
# a list containing dictionaries
dictionaries_list = [
        {"origin": "Lisbon", "destination": "Madrid"},
        {"origin": "Madrid", "destination": "Paris"}
        ]
#%%
"""
******************************************************************************

EXERCISES

******************************************************************************
"""
#%%
"""
 Create a dictionary where the keys are the first 3 days of the week and the values
 are the position of that day in the week.
"""

#%%
"""
 transform all keys in that dictionary to uppercase
"""
