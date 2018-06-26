#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 18:15:21 2018

@author: letcosta
"""
#%%
""""
FIZZBUZZ
"""""
# What's the difference between using the def fuction versus the for function?
for num in range (1,101):
    if num%3 == 0: 
        print("Fizz")
    elif num%5 == 0:
        print("Buzz")
    elif num%3 == 0 and num%5==0:
        print("FizzBuzz")
    else:
        print(num)
#%%
 """"
Roman Numerals
"""""       
def romanlist (number):
    list=((1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(50,'L'),(45,'XLV'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I'))
    roman=""
    for x,y in list: 
        while number >= x:
            roman=roman+y
            number=number-x
    return roman
print(romanlist(55))
#%%
""""
ROT13
"""""
# Letter to number to number + 13 to new letter
import string

text = 'Pastel'
alphabet = string.ascii_lowercase

for letter in text:
    ognumber = alphabet.find(letter)
    ciphernum = ((ognumber + 13) % 25) 
    cipherletter = alphabet[ciphernum]
    print(cipherletter)
        