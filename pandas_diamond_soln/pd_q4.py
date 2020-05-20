#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv('diamonds.csv')


# In[3]:


print('No. of rows',len(data.axes[0]))


# In[4]:


print('No. of columns',len(data.axes[1]))


# In[5]:


data.dropna()


# In[6]:


print(data[data.duplicated()])






