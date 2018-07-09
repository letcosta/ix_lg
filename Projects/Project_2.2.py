
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib as mpl
mpl.rcParams["figure.figsize"] = (12,12)


# In[3]:


chetty = pd.io.stata.read_stata("/Users/letcosta/Desktop/Econ 41:42/files42 Winter 2018/data/Chetty_opportunity.dta")
chetty.to_csv("Chetty_opportunity.csv")


# In[4]:


chetty.shape
chetty


# In[5]:


chetty.head()
chetty


# In[6]:


chetty.dtypes


# In[20]:


import cartopy.crs as crs
from cartopy.io import img_tiles


# In[21]:


chetty.e_rank_b.plot.hist();


# In[22]:


chetty.shape


# In[23]:


low_100 = chetty.sort_values(by="e_rank_b").head(100)
high_100 = chetty.sort_values(by="e_rank_b", ascending=False).head(100)


# In[25]:


imagery = img_tiles.GoogleTiles()

ax = mpl.axes(projection=imagery.crs)

#x0, x1, y0, y1
maps_limits = (-71.38 ,-70.77,42.03 , 42.47)
ax.set_extent(maps_limits)

ax.add_image(imagery, 10)

mpl.plot(low_100.LON, low_100.LAT, transform=ccrs.Geodetic(), 
         marker='.', markersize=10, color="red",  linewidth=0, alpha=0.5)

mpl.plot(high_100.LON, high_100.LAT, transform=ccrs.Geodetic(),
         marker='.', markersize=10, color="green",  linewidth=0, alpha=0.5)

mpl.show();


# In[26]:


print("e_rank_b")


# In[27]:


class StamenToner(img_tiles.GoogleTiles):
    def _image_url(self, tile):
        x, y, z = tile
        url = 'http://tile.stamen.com/toner/%s/%s/%s.png' % (
            z, x, y)
        return url
    
imagery = StamenToner()

ax = mpl.axes(projection=imagery.crs)

#x0, x1, y0, y1
maps_limits = (-71.38 ,-70.77,42.03 , 42.47)
ax.set_extent(maps_limits)

ax.add_image(imagery, 10)

mpl.plot(cheap_100.LON, cheap_100.LAT, transform=ccrs.Geodetic(), 
         marker='.', markersize=10, color="red",  linewidth=0, alpha=0.5)

mpl.plot(expensive_100.LON, expensive_100.LAT, transform=ccrs.Geodetic(),
         marker='.', markersize=10, color="green",  linewidth=0, alpha=0.5)

mpl.show();

