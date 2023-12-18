#!/usr/bin/env python
# coding: utf-8

# In[1]:


# OOPs 
# Class 
# Inheritance


# In[5]:


# Sigle Inheritance
class engineer:
    def __init__(self):
        self.x="civil engineer"
        self.y="comp engineer"
    def display(self):
        print("X is a :",  self.x)
        print("Y is a :" , self.y)


# In[6]:


run=engineer()
run.display()


# In[24]:


class Engineer:
    def name(self):
        self.x=int(input("cgpa of civil   "))
        self.y=int(input("cgpa of comp   "))
    def disp_name(self):
        print(self.x)
        print(self.y)


# In[25]:


class cgpa(Engineer):
    def total(self):
        self.cgpa=self.x+self.y
    def disp_cgpa(self):
        print(self.cgpa)
        


# In[26]:


run=cgpa()
run.name()
run.total()
run.disp_cgpa()


# In[3]:


class Laptop:
    def name(self):
        self.a="Lenovo"
        self.b="Mac"
        self.c="Dell"
        self.d="hp"
    def disp_name(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)


# In[4]:


class Cost(Laptop):
    def cost_lp(self):
        self.lp_names=self.a+self.b+self.c+self.d
    def cost_lp(self):
        self.lenovo_cost=int(input("Enter cost  "))
        self.mac_cost=int(input("Enter cost  "))
        self.dell_cost=int(input("Enter cost  "))
        self.hp_cost=int(input("Enter cost  "))
    def disp_cost(self):
        print("Cost of Lenovo: ",self.lenovo_cost)
        print("Cost of Mac: ",self.mac_cost)
        print("Cost of Dell: ",self.dell_cost)
        print("Cost of HP: ",self.hp_cost)


# In[5]:


run=Cost()
run.name()
run.cost_lp()
run.disp_name()
run.disp_cost()


# In[ ]:


# Bike cost price      tax

# 100000               15%
# 50000<=100000        10%
# <=50000              5%


# In[25]:


price = int(input("Enter cost of bike"))
if price >= 100000:
    tax = (15/100)*price
elif price <=100000 and price>=50000:
    tax = (10/100)*price
else :

    tax = (5/100)*price
print(tax)


# In[1]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# In[3]:


factorial(5)


# In[14]:


def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]


# In[25]:


s= 'madam'


# In[26]:


print(is_palindrome(s))


# In[27]:


def list_sum(numbers):
    return sum(numbers)


# In[28]:


numbers = 1,2,5,6,97,4


# In[29]:


list_sum(numbers)


# In[30]:


def fibonacci(n):
   fib_sequence = [0, 1]
   while len(fib_sequence) < n:
       fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
   return fib_sequence


# In[32]:


fibonacci(15)


# In[ ]:




