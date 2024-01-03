#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Creating two DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 22]})

# Performing an inner join on the 'ID' column
result_inner = pd.merge(df1, df2, on='ID', how='inner')

print(result_inner)


# In[2]:


import pandas as pd

# Creating two DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 22]})

# Performing a left join on the 'ID' column
result_left = pd.merge(df1, df2, on='ID', how='left')

print(result_left)


# In[3]:


import pandas as pd

# Creating two DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 22]})

# Performing a right join on the 'ID' column
result_right = pd.merge(df1, df2, on='ID', how='right')

print(result_right)


# In[4]:


import pandas as pd

# Creating two DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie'], 'Dept': ['HR', 'IT', 'Finance']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Age': [25, 30, 22], 'Dept': ['IT', 'Finance', 'Marketing']})

# Performing an inner join on multiple columns ('ID' and 'Dept')
result_multi = pd.merge(df1, df2, on=['ID', 'Dept'], how='inner')

print(result_multi)


# In[5]:


df1= pd.DataFrame({'A':[1,2,3,4,5,6],'B':[11,12,13,14,15,16], 'C':[21,22,23,24,25,26],'D':[31,32,33,34,35,36]})

df2= pd.DataFrame({'A':[7,8,9,10,11,12],'B':[17,18,19,20,21,22], 'C':[27,28,29,30,31,32],'D':[37,38,39,40,41,42]})


# In[8]:


df1


# In[9]:


df3  = pd.concat([df1, df2], axis=0)


# In[10]:


df3


# In[ ]:




