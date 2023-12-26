#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Using While loop


# In[2]:


counter = 1
while counter <= 5:
    print(counter)
    counter += 1


# In[6]:


limit = 10
sum_result = 0
current_number = 1

while current_number <= limit:
    sum_result += current_number
    current_number += 1

print("Sum of numbers from 1 to 10 ", "is:", sum_result)


# In[27]:


import random

ran_num = random.randint(1,88)

print(ran_num)


# In[28]:


import secrets

secure_random = secrets.randbelow(100)
print(secure_random)


# In[29]:


num=int(input("Enter any  Number"))
a = 1
while(a<=10):
    print(a*num)
    a=a+1


# In[ ]:




