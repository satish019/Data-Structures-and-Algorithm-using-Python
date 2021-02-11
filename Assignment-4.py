#!/usr/bin/env python
# coding: utf-8

# # Assignment - 4

# # Question 1

# # Write a program to print the following pattern

# # 1
# 22
# 333
# 4444
# 55555
# 

# # Solution:

# In[1]:


num = 5
for i in range(1,num+1):
    for j in range(1,i+1):
        print(i,end = "")
    print()


# # Question 2

# # Write a Python program to add two numbers using class and object. (Take both numbers as input from the user)

# # Solution:

# In[2]:


class Addition:
    
    def add(self, num1, num2):
        return num1 + num2
    
num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
Add = Addition()
res = Add.add(num1, num2)
print("Addition is:",res)


# # Question 3

# # Define a function swap that should swap two values and print the swapped variables outside the swap function.

# # Solution:¶

# In[3]:


def swap(num1, num2):
    num1 = num1 + num2
    num2 = num1 - num2
    num1 = num1 - num2
    return num1,num2

swap(3,4)


# In[ ]:




