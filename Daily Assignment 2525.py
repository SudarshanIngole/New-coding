#!/usr/bin/env python
# coding: utf-8

# In[1]:


for number in range(1,101):
    if number % 3 == 0 and number % 5 ==0 :
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number %5 == 0:
        print('Buzz')
    else:
        print(number)
        


# In[3]:


# Program 1
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


# In[4]:


# Program 2
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")


# In[5]:


# Program 3
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles triangle")
else:
    print("Scalene triangle")


# In[ ]:




