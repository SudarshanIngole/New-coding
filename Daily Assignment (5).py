#!/usr/bin/env python
# coding: utf-8

# In[82]:


import numpy  as np


# In[3]:


# create an array of 10 zeros
arr =np.zeros(10)
arr


# In[18]:


# create an array of 10 fives
arr=np.ones([10])
arr=arr*5
(arr)


# In[6]:


arr


# In[77]:


#### Create an array of the integers from 10 to 50

arr=np.array(range(10,51))
arr


# In[76]:


#### Create an array of all the even integers from 10 to 50
even_array = range(10,51,2)


arr=np.array(even_array)
arr


# In[73]:


#### Create a 3x3 matrix with values ranging from 0 to 8

matrix =([0,1,2],[3,4,5],[6,7,8])

arr=np.array(matrix)
arr


# In[78]:


#### Create a 3x3 identity matrix

matrix = np.eye(3)
matrix


# In[94]:


#### Use NumPy to generate a random number between 0 and 1

num=np.random.rand()
num


# In[100]:


#### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
num=np.random.randn(25)
num


# In[106]:


np.linspace(0.01,1,100).reshape(10,10)


# In[112]:


np.arange(0.01,1.01,0.01).reshape(10,10)


# In[115]:


#### Create an array of 20 linearly spaced points between 0 and 1:
np.linspace(0,1,20)


# In[117]:


## Numpy Indexing and Selection

## Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:
    
mat = np.arange(1,26).reshape(5,5)
mat


# In[118]:


mat[2:,1:]


# In[119]:


mat[3,4]


# In[120]:


mat[:3,1]


# In[121]:


mat[4,:]


# In[123]:


mat[3:,:]


# In[125]:


#### Get the sum of all the values in mat
np.sum(mat)


# In[126]:


#### Get the standard deviation of the values in mat

np.std(mat)


# In[131]:


np.sum(mat,axis=0)


# In[ ]:




