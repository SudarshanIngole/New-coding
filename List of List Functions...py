#!/usr/bin/env python
# coding: utf-8

# In[30]:


## List of List Functions ##

#  1) Append: add an element to the last in the list
list12 = [10,20,30,40,50,60,70,80,90,20,20]
list12.append(100)


# In[2]:


list12


# In[3]:


# 2) Insert : to add a element in specific index list12.insert(0,10)
list12.insert(5,55)


# In[4]:


list12


# In[5]:


# 3) Extend : any particular list is to be added in the list
list12.extend([110,120,130,])


# In[6]:


list12


# In[7]:


# 4) Pop : remove last element in the list with () only 
list12.pop()


# In[8]:


list12


# In[9]:


# if we want any specific elememt to be pop, then we can add index number of that value in ()
list12.pop(4)


# In[10]:


list12


# In[11]:


# 5) Remove : if we want any element to be remove then add that element in the ()
list12.remove(55)


# In[12]:


list12


# In[14]:


# 6) del : it is not a list function but it is a predefined word(keyword)
# It can be used to delete any value by giving that element index number
del list12[3]


# In[15]:


list12


# In[16]:


# 7) Reverse : it is used to reverse the elements of the list
list12.reverse()


# In[17]:


list12


# In[18]:


# 8) Sort : if is benificial for character values, if you have any list of fruits then it will give you the elements in the 
# alphabetical order.
list13 = ["guava", "apple","mango","banana","orange"]


# In[19]:


list13.sort()


# In[20]:


list13


# In[26]:


# 9) Index :  Returns the index of the first occurrence of an element in the list.
list12.index(110)


# In[32]:


# 10) Count : it gives the number of time an element occure in the list
list12.count(20)


# In[35]:


# 11) Copy : to copy all the elements in the list  
list12.copy()


# In[39]:


# 12) Minimum value and Maximum value in the list
min_value = min(list12)
print(min_value)
max_value = max(list12)
print(max_value)


# In[40]:


# 13) Sum : total sum of the elements 
total_sum = sum(list12)


# In[41]:


print(total_sum)


# In[45]:


# 14) Filter : it is used to filter some elements like the elements are only divisible by 2 or even number or odd number
def is_even(x):
    return x %2 == 0
even_num = list(filter(is_even,list12))
print(even_num)


# In[47]:


# 14) Map : to apply the function to all the elements in the list
def square(x):
    return x**2
numbers = [1,2,3,4,5,6]
square_number = list(map(square, numbers))
print(square_number)


# In[1]:


# 15) Zip : combine multiple list in one list
name = ["Darshan","Raj","Omkar",]
age = [22,21,33]
combine_name_age = list(zip(name,age))
print(combine_name_age)

# 16)
list123 = [10,20,30,50,44]
list123.copy()






# %%
