#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)

print(df)


# In[2]:


# Adding a new column
df['Salary'] = [50000, 60000, 75000]
print(df)


# In[13]:


df


# In[14]:


df


# In[24]:


s1=df.rename({'Name':'Name_Again','Age':'Age_years'},axis=1,inplace=True)


# In[28]:


df


# In[32]:


df.Name_Again


# In[33]:


df.iloc[1,0]


# In[37]:


# Calculating basic statistics
mean_age = df['Age_years'].mean()
max_salary = df['Salary'].max()

print(mean_age)
print(max_salary)


# 01/01/2024 Monday

# In[3]:


import pandas as pd


# In[4]:


data=pd.read_csv('iris.csv')


# In[5]:


data.head()


# In[6]:


data.min()


# In[7]:


data.max()


# In[20]:


def half(s):
    return s*0.5


# In[21]:


data[['SepalLengthCm','SepalWidthCm']].apply(half) 


# In[16]:


half = 0.5


# In[17]:


half


# In[24]:


data['Species'].value_counts()


# In[25]:


data.sort_values(by='PetalWidthCm')


# In[ ]:




