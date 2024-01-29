#!/usr/bin/env python
# coding: utf-8

# In[3]:


fruits =('Apple', 'Banana', 'orange' )
for fruit in fruits:
    print(fruit)
    print(fruit + ' amy')
print(fruits)


# In[5]:


# Input a Python list of student heights
student_heights = input('Give the students height ( with space only )').split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Your code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(f"average height = {average_height}")


# In[7]:


# Input a list of student scores
student_scores = input('Give the student score (with space only)').split()
for n in range(0, len(student_scores)):
    
    
    student_scores[n] = int(student_scores[n])

# Your code below this row 👇
highest_score = 0
for score in student_scores:
    
    
    if score > highest_score:
        
        highest_score = score
    # print(highest_score)

print(f"The highest score in the class is: {highest_score}")


# In[ ]:




