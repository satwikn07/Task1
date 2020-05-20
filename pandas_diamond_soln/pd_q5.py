#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv('diamonds.csv')


# In[3]:


data1 = data[:int(len(data)*0.75)+1]
print(data1)


# In[4]:


df2 = data[int(0.75*len(data))+1:]
print(df2)


# In[5]:


print(id(df2),type(df2))
print(id(data1),type(df2))


# In[ ]:




