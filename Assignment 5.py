#!/usr/bin/env python
# coding: utf-8

# In[18]:


#Assignment 5
subject=['American','Indian']
object1=['play','watch']
verb=['Football','Basketball']
[[k+' '+j+' '+v] for k in subject for j in object1 for v in verb]


# In[22]:


n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))

try:
    k=n1/n2
    print(k)
except ZeroDivisionError as ne:
    print('Please enter second no. greater than 0')


# In[ ]:




