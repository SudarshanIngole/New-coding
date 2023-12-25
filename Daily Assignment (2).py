#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime


# In[2]:


x = datetime.datetime.now()


# In[3]:


print(x)


# In[10]:


x= datetime.datetime(2001, 4,5)


# In[12]:


print(x.year)
print(x.strftime('%a'))   ## For knowing day and year


# In[16]:


x= datetime.datetime(2001, 4,5)

print(x.year)    ## For knowing year and month
print(x.strftime('%b'))




# In[23]:


import camelcase


# In[28]:


c  = camelcase.CamelCase()


# In[29]:


txt = 'my name is Sudarshan Ingole'


# In[30]:


print(c.hump(txt))


# In[32]:


import re


# In[40]:


txt = "India is a country all indians are my brothers and brothers"
x = re.findall("the", txt)
print(x)


# In[42]:


txt = "India is a country all indians are my brothers and brothers"
x =  re.split('\s', txt)
print(x)


# In[52]:


txt = "India is a country all indians are my brothers and brothers"
x =  re.search('ias', txt)
print(x)


# In[ ]:




