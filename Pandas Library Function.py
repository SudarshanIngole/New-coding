#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Creating a DataFrame with a categorical column
df_categorical = pd.DataFrame({'Category': ['A', 'B', 'A', 'B', 'A', 'B']})

# Converting the column to a categorical type
df_categorical['Category'] = df_categorical['Category'].astype('category')
print(df_categorical)


# In[4]:


# Resampling time series data to a different frequency
df_dates = pd.DataFrame({'Date': pd.date_range('2022-01-01', periods=5), 'Value': [10, 20, 30, 40, 50]})
df_resampled = df_dates.set_index('Date').resample('M').sum()
print(df_resampled)


# In[6]:


data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Los Angeles']}

df = pd.DataFrame(data)
print(df)


# In[7]:


df.plot(x='Name', y='Age', kind='bar', title='Age Distribution')


# In[8]:


s1 = pd.Series([1,2,3,4,5])


# In[14]:


s2=pd.Series([1,2,3,4,5],index=[ 'a','b','c','d','e'])


# In[15]:


s2


# In[18]:


# Dictionary in Pandas
s2 = pd.Series({'k1':10,'k2':20,'k3':30,'Sudarshan':22})


# In[19]:


s2


# In[ ]:




