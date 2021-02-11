#!/usr/bin/env python
# coding: utf-8

# # Assignment - 5

# # Question 1

# # Perform Bubble sort using function in python.

# # Solution:

# In[1]:


def bubble_sort(l):
    n= len(l)
    for i in range(0,n):
        swapped = 0
        for j in range(0,n-1-i):
            if l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
                swapped = 1
        if swapped == 0:
            break
    return l

li = [12, 34, 5, 23, 10, 15]
res = bubble_sort(li)
print(res)


# # Question 2

# # Perform Selection sort using function in python.

# # Solution:

# In[2]:


def select_sort(l):
    n = len(l)
    for i in range(0, n-1):
        pos = i
        for j in range(i+1, n):
            if l[pos] > l[j]:
                pos = j
        l[pos],l[i] = l[i],l[pos]
    return l

li = [33, 54, 21, 43, 30, 15]

res = select_sort(li)
print(res)


# # Question 3

# # Perform Insertion sort using function in python.

# # Solution:

# In[3]:


def insert_sort(l):
    n = len(l)
    for j in range(1,n):
        key = l[j]
        i = j-1
        while(i >=0 and l[i] > key):
            l[i+1] = l[i]
            i = i-1
        l[i+1] = key
    return l

li = [21, 24, 10, 0, 7, 15, 4]

res = insert_sort(li)
print(res)


# In[ ]:




