
# coding: utf-8

# In[2]:


from IPython.display import Image
import numpy as np
import pandas as pd 
import sys
import matplotlib.pyplot as plt


# In[3]:


import scipy.stats as stats
apartments = pd.read_csv("../data/airbnb.csv")


# In[4]:


print(apartments.describe())
print(apartments.isnull().sum())


# In[5]:


argument1 = sys.argv[1]
region = sys.argv[2]


# In[11]:


region = apartments[apartments.neighborhood == region]


# In[22]:


available = region.count(region.room_id)


# In[7]:


listings = region.groupby("room_type").count()


# In[10]:


price = region.price.mean()


# In[20]:


quartile25 = region.price.quantile(.25)
quartile50 = region.price.quantile(.50)
quartile75 = region.price.quantile(.75)


# In[21]:


print("The total number of available listings in" + region + "are" + available + ".")
print("The number of rooms broken down per listing type are" + listings)
print("The average room price is" + price + ".")
print("The price quartiles are" + quartile25 + "," + quartile50 + "," + quartile75 + ".")


# In[14]:


def search (region):
    pass


# In[13]:


def parse_arguments():
    pass


# In[15]:


def main(argument1):
    pass


# In[18]:


if__name__=="__main__":
    if argument1 == 'information':
        information (region)
    else:
        search()
main(argument1)

