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


# In[ ]:




