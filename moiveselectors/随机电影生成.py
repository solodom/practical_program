
# coding: utf-8

# In[15]:


import numpy as np
import pandas as pd


# In[39]:


movie_file=open('10.txt')
movie_list={}
i=0
for lines in movie_file.readlines():
    lines=lines[:-2]
    movie_list[i]=lines
    i=i+1


# In[40]:


movie_list


# In[44]:


index_list=np.random.randint(0,250)
print('Today\'s movie is:',movie_list[index_list])


# In[46]:


movie_list

