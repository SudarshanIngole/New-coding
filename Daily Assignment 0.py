#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data= pd.read_csv('train.csv')


# In[3]:


data.head()


# In[4]:


## IS NULL # Missing Values


# In[5]:


data.isnull().sum()


# In[6]:


data.Age.isnull().sum()


# In[7]:


## handling the missing values

data.Age.mean()


# In[8]:


np.mean(data['Age'])


# In[14]:


data.loc[data["Age"].isnull()==True, "Age"]=55


# In[15]:


data.Age.mean()


# In[16]:


data.Age.isnull().sum()


# In[17]:


data


# In[ ]:




