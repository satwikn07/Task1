#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv('diamonds.csv')


# In[3]:


series = data['carat']


# In[4]:


print(series)

