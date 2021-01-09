#!/usr/bin/env python
# coding: utf-8

# In[51]:


#Assignment 2

for i in range(1,6):
    print('')
    for j in range(0,i):
        print('*',end='')
for i in range(5,1,-1):
    print('')
    for j in range(1,i):
        print('*',end='')


# In[53]:


w=input("Enter word")
print("Actual Word = {0}, Reversed Word {1}".format(w,w[::-1]))


# In[ ]:




