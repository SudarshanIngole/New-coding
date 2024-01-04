#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


# In[2]:


sns.get_dataset_names()


# In[5]:


df  = sns.load_dataset('iris')


# In[6]:


df


# In[7]:


df.head()


# In[8]:


df.tail()


# In[9]:


df.species.unique()


# In[10]:


df.species.value_counts()


# In[11]:


df.info()


# In[12]:


df.describe()


# In[17]:


sns.lineplot(x='sepal_length', y='sepal_width', data=df, errorbar=None)
plt.show()


# In[19]:


sns.scatterplot( data=df)


# In[23]:


sns.pairplot(data=df)  # without coloring


# In[27]:


sns.boxplot(x='sepal_width', y='sepal_length', data=df)
plt.show()


# In[29]:


sns.lineplot(x='sepal_length', y='sepal_width', data=df,hue='species', errorbar=None)
plt.show()


# In[32]:


sns.barplot(x='species',y='sepal_length', data=df)
plt.show()


# In[33]:


sns.countplot(x='species', data=df)
plt.show()


# In[34]:


sns.violinplot(x='species', y='sepal_width', data=df)
plt.show()


# In[35]:


sns.stripplot(x='species', y='petal_width', data=df)
plt.show()


# In[36]:


sns.histplot(x='petal_width', data=df)
plt.show()


# In[37]:


sns.histplot(x='petal_width', data=df,hue='species', kde=True) # kernel density estimation 
plt.show()
#kde is approximation of histogram to density curve.


# In[42]:


sns.distplot(df['petal_width'],color="g", kde=True) # ,hist=False, kde=False
plt.show()


# In[43]:


sns.pairplot(data=df, hue='species')


# In[ ]:




