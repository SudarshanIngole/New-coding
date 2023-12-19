#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## using Lambda Function 


# In[6]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
   ## Extracting the even numbers from the given set


# In[2]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)


# In[11]:


tuples_list = [(1, 5), (2, 3), (4, 1), (3, 9)]
sorted_tuples = sorted(tuples_list, key=lambda x: x[1])



# In[12]:


print(sorted_tuples)


# In[4]:


list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
sum_lists = list(map(lambda x, y: x + y, list1, list2))
print(sum_lists)


# In[ ]:





# In[7]:


numbers = [8, 3, 2, 10, 5, 7]
max_number = max(numbers, key=lambda x: x)



# In[9]:


print(max_number)


# In[16]:


is_even = lambda x: x % 2 == 0

# Example usage
number = int(input("Enter Number"))

if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# In[ ]:




