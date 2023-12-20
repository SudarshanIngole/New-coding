#!/usr/bin/env python
# coding: utf-8

# In[8]:


def add_numbers(x, y):
    
    result = x + y
    return result


num1 = int(input("Enter value"))
num2 = int(input("Enter Value"))
sum_result = add_numbers(num1, num2)
print(sum_result)


# In[11]:


# Arithmetic Operation

def num_1(n3):
    a=1
    while(a<=10):
        print(a)
        a+=1
    n3 += 1 
    return n3
    


# In[12]:


Res = num_1(100)
print(Res)


# In[14]:


my_string = "Hello, World!"
new_string = my_string.replace("Hello", "Hi")
print(new_string)


# In[19]:


import re

pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	


# In[20]:


import re

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)


# In[ ]:




