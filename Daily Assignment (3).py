#!/usr/bin/env python
# coding: utf-8

# # work on Pandas Library

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv('iris.csv')


# In[3]:


data.head()


# In[5]:


data.tail()


# In[6]:


data.info()


# In[7]:


data.describe()


# In[9]:


data.Id


# In[11]:


data.SepalLengthCm


# In[12]:


data.iloc[:,2]


# In[13]:


data.columns


# In[16]:


data['SepalLengthCm'].mean()


# In[17]:


data['SepalLengthCm'].max()


# In[19]:


data['Result']="True False"


# In[20]:


data


# In[24]:


dff1=data.drop([2,3],axis=0)


# In[23]:


data


# In[25]:


dff1


# In[26]:


data.drop(['Result'],axis=1)


# In[27]:


dff1


# In[28]:


data


# In[31]:


data.loc[data['PetalLengthCm']==1.4]


# In[ ]:




