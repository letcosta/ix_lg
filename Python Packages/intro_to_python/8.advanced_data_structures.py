# -*- coding: utf-8 -*-
"""
Aquí se explican estructuras de datos avanzadas 

@author: manugarri
"""


"""
*******************************************************************************
SETS
*******************************************************************************
Sets are groups of non repeated elements.
"""


# Sets can be created from a list
friends_group1 = set(["Manuel", "Nicole", "Michale", "Tom"])
print(type(friends_group1))

#%%
# Sets can also be created with {}
friends_group2 = {"Manuel", "Alex", "Tom", "Mary", "Jane"}
print(type(friends_group2))

#%%
# Sets are used to evaluate if an element belongs to a group

print("Manuel" in friends_group1)

#%% 
# With sets its easy to see common or different elements among groups

all_friends = friends_group1.union(friends_group2)
print(all_friends)

#%%
common_friends = friends_group1.intersection(friends_group2)
print(common_friends)

#%%
group1_exclusive_friends = friends_group1 - friends_group2
print(group1_exclusive_friends)

#%%
# We can add or remove elements from a set

avengers = {"Iron Man", "Thor", "Hulk", "Black Widow", "Captain America", "Hawkeye"}
avengers.add("Spiderman")
print(avengers)

#%%
avengers.remove("Hawkeye")
print(avengers)

#%%
# Sets are useful to remove duplicated elements from a list

repeated_avengers = ["Iron Man", "Thor", "Hulk", "Black Widow", "Captain America",
                      "Hawkeye", "Iron Man", "Thor", "Hulk", "Black Widow",
                      "Hulk", "Black Widow"]

print(len(repeated_avengers))

unique_avengers = list(set(repeated_avengers))
print(unique_avengers)

#%%
# It's easy to compare sets

set1 = {"strawberry", "apple"}

set2 = {"apple", "strawberry"}

print(set1 == set2)

#%%
# A set is greater than another one if it contains all of the elements of the other set
# and at least one more

set3 = {"strawberry", "apple", "banana"}

print(set3 > set2)

#%%
set4 = {"blackberry", "apple"}
print(set3 > set4)

#%%
"""
*******************************************************************************
Counter
*******************************************************************************

we use Counters to, well, count things
"""

from collections import Counter


votes = ['INDEPENDENT',
         'REPUBLICAN',
         'REPUBLICAN',
         'INDEPENDENT',
         'DEMOCRAT',
         'REPUBLICAN',
         'DEMOCRAT',
         'DEMOCRAT',
         'DEMOCRAT',
         'INDEPENDENT',
         'REPUBLICAN',
         'DEMOCRAT',
         'REPUBLICAN',
         'DEMOCRAT',
         'INDEPENDENT',
         'INDEPENDENT',
         'INDEPENDENT',
         'INDEPENDENT'
]

votes_count = Counter(votes)
print(votes_count)

#%%
# We can see how many times an element appears
votes_count["DEMOCRAT"]

#%%
# If an element doesn't exist it returns 0
votes_count["GREEN PARTY"]

#%%
# We can add elements to a counter
print(votes_count["DEMOCRAT"])
votes_count.update(["DEMOCRAT"])
print(votes_count["DEMOCRAT"])

#%%
# We can also update the total counts by using a dictionary
votes_count.update({"GREEN PARTY": 1,"DEMOCRAT": 10})
print(votes_count)

#%%
# We can also assign the values directly like with any dictionary
votes_count["GREEN PARTY"] = 3
print(votes_count)

#%%
"""
*******************************************************************************
DefaultDict
*******************************************************************************

DefaultDict allows us to create dictionaries that return a default value in case 
we are selecting a key that doesn't exist

We create a defaultdict by passing it a function that provides the default value
"""
from collections import defaultdict

# this is going to fail, "vanilla" is not a function!
icecream_flavors = defaultdict("vanilla")

#%%
icecream_flavors = defaultdict(lambda: "vanilla")
print(icecream_flavors)

#%%
icecream_flavors["Manuel"] = "chocolate"
print(icecream_flavors["Manuel"])

#%%
# When the key doesnt exist we get the default value
print(icecream_flavors["Mary"])

#%%
# We can also create a defaultdict from a regular dictionary

icecream_flavors_dict = {"Manuel": "chocolate", "Mary": "fresa"}
icecream_flavors = defaultdict(lambda: "vanilla", icecream_flavors_dict)
print(icecream_flavors)

#%%
"""
A very common usecase for defaultdicts is when we have a group of elements where
each element has multiple features and we want to make a dictionary for quick lookup
"""

pokemon_trainers_list = [
        ['Ash', 'Nidorian'],
         ['Ash', 'Charmander'],
         ['Ash', 'Jigglypuff'],
         ['Ash', 'Rattata'],
         ['Ash', 'Pikachu'],
         ['Ash', 'Pidgey'],
         ['Misty', 'Pikachu'],
         ['Misty', 'Squirtle'],
         ['Misty', 'Jigglypuff'],
         ['Misty', 'Rattata'],
         ['Brock', 'Nidorian'],
         ['Brock', 'Charmander'],
         ['Brock', 'Jigglypuff']
]

pokemons_by_trainer = defaultdict(list)

for trainer, pokemon in pokemon_trainers_list:
    pokemons_by_trainer[trainer].append(pokemon)
pokemons_by_trainer

#%%
"""
*******************************************************************************

EXERCISES

*******************************************************************************
"""
#%%
"""
 Convert the list pokemon_trainers to a list of dictionaries with the keys "trainer"
 and "pokemon"

[
{"trainer": "Ash", "pokemon": "Pikachu"},
{"trainer":"Ash", "pokemon": "Nidorian"},
...
]
"""


#%%
"""
Create a function that takes a frase and returns the most common 5 letters
"""

#%%
"""
Create a function that, given two lists of elements, returns their jaccard index.
 The Jaccard coefficent is a similarity measure between two groups and its defined
 as the number of elements in common in both groups divided by the total number of
 elements in both groups


So for example if we have the following friend groups:

friends_group1 = ["Manuel", "Nicole", "Michale", "Tom"]
friends_group2 = ["Manuel", "Alex", "Tom", "Mary", "Jane"]

Their jaccard index would be 0.2857142857142857
jaccard(friends_group1, friends_group2)
"""
