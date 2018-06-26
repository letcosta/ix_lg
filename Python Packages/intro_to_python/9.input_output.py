# -*- coding: utf-8 -*-
"""
Here we talk about reading and writing to files

@author: manugarri
"""

#%%

"""
******************************************************************************
Folder creation
******************************************************************************
"""

# we can create folders with os.makedirs()
import os
os.makedirs("./data/names/", exist_ok=True)
#%%
"""
******************************************************************************
LISTING FILES
******************************************************************************
"""
files_in_current_folder = os.listdir(".")
print(files_in_current_folder)


#%%
"""
*******************************************************************************
WRITING TO FILES
*******************************************************************************
"""
#%%
# We can use `open` to open files. If the file does not exist it will throw an error
nonexisten_file = open("./data/names/users.txt")

#%%
# If we want to write to a file (create it) we must specify we want to open the file in write mode
writing_file = open("./data/names/users.txt", "w")
writing_file.write("James")
writing_file.write("Mary")
#%%
# Nothing is actually written until we close the file
writing_file.close()
#%%
# If we open a file in "w" mode again, it will delete the existing content and create a blank file
writing_file = open("./data/names/users.txt", "w")
writing_file.write("Michael")
writing_file.write("Adam")
writing_file.close()

#%%
# We can open a file in append mode with "a". This way we wont erase existing 
# content and will add to the end of the file
append_file = open("./data/names/users.txt", "a")
append_file.write("James")
append_file.write("Mary")
append_file.close()


#%%
"""
Usually we don't want to use the open method like we did, because if any error
happens between opening and closing the file we can lose the file

The recommended way of reading and writing to files is via a context manager
"""
users = ["Manuel", "Anthony", "John", "Mary"]
#we open a context with the keyword `with`
with open("./data/names/users.txt", "w") as file_name:
    for user in users:
        file_name.write(users)
#%%
# So far we have been writing all the names one next to each other, if we want to 
# put each one in one line, we need to write a newline symbol "\n" after each one

users = ["Manuel", "Anthony", "John", "Mary"]

with open("./data/names/users.txt", "w") as file_name:
    for user in users:
        file_name.write(users)
        file_name.write("\n")
#%%

"""
*******************************************************************************
READING FROM FILES
*******************************************************************************
"""

with open("./data/names/users.txt") as fname:
    data = fname.read()
print(data)

type(data)
#%%

# the method `read()` read the whole file as text (one giant string).
# If we want to separate the lines into different strings we can use the method
# readlines()
read_users = []

with open("./data/names/users.txt") as fname:
    lines = fname.readlines()
    print(lines)
    for line in lines:
        read_users.append(line.strip("\n"))
print(read_users)

type(read_users)
#%%
"""
*******************************************************************************
USING PATHLIB
*******************************************************************************

In windows folder structure is defined with \ while in linux/mac we use /
This can lead to problems

One way to avoid these kinds of issues is use pathlib, a cross-platform library
for dealing with files
"""

from pathlib import Path

folder = Path("./data/names/")

users_file = folder / "users.txt"
print(type(users_file)) #PosixPath o WindowsPath
# we dont need a context manager with pathlib
users_file.read_text()
#%%
# we can easily write to a file using pathlib
folder = Path("./data/names/")

file2 = folder / "users_2.txt"

file2.write_text("hola!")
#%%
print(file2.read_text())

# Pathlib does not support append mode yet!
"""

Exercises

"""
#%%
"""
Create a function that, given a filename, reads it and returns the longest line

"""

#%% 
"""
Create a function that takes a filename and an integer as arguments, reads the file
and returns the last n lines
"""


#%%
"""
Create a function that takes a dictionary and a filename as arguments, and writes 
the dictionary as a csv file with the specified filename.

CSV files (Comma-Separated-Values) are a data format to store data, where each element
is a row, and each field is separated by a comma

For example, given the dictionary
{
"name": ["Antonio", "Miguel", "Julian", "Andrew"],
"age": [45, 40, 22, 34],
"city": ["Murcia", "Lisbon", "Barcelona", "Madrid"]
}

and a filename , `people.csv`,

This function would save such dictionary as a file named `people.csv` with this format:

    name,age,city
    Antonio,45,Murcia
    Miguel,40,Lisbon,
    Julian,22,Barcelona
    Andrew,34,Madrid
"""
