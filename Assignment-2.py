#!/usr/bin/env python
# coding: utf-8

# # Assignment - 2

# # Question 1

# # What is the time, space complexity of following code:

# int a = 0, b = 0;
# for (i = 0; i < N; i++) {
# a = a + 1;
# }
# for (j = 0; j < M; j++) {
# b = b + j;
# }

# # Answer:

# O(N + M) time complexity,
# O(1) space complexity

# # Explanation:

# The first loop is O(N) and the second loop is O(M). Since we don’t know which is bigger, we say this is O(N + M). This can also be written as O(max(N, M)).
# Since there is no additional space being utilized, the space complexity is constant O(1)

# # Question 2

# # What does it mean when we say that an algorithm X is asymptotically more efficient than Y?¶

# a)X will be a better choice for all inputs
# b)X will be a better choice for all inputs except possibly small inputs
# c)X will be a better choice for all inputs except possibly large inputs
# d)Y will be a better choice for small inputs

# # Answer

# (b) X will be a better choice for all inputs except possibly small inputs

# # Explanation:

# In asymptotic analysis we consider growth of algorithm in terms of input size. An algorithm X is said to be asymptotically better than Y if X takes smaller time than y for all input sizes n larger than a value n0 where n0 > 0.

# # Question 3

# # Write a Python program to print even numbers in a list.¶

# Sample:
# Input: list1 = [12, 3, 55, 6, 144]
# Output: [12, 6, 144]
# Input: list2 = [2, 10, 9, 37]
# Output: [2, 10]

# # Solution

# In[3]:


size = int(input("Enter the size of list:"))
my_list = []
for i in range(0,size):
    num = int(input("Enter any number:"))
    if num%2 == 0:
        my_list.append(num)
print(my_list)


# In[ ]:




