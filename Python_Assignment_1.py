#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assignment 1, Question 1
for i in range(2000,3201):
    if i%7==0 and i%5 != 0:
        print(i,end=',')


# In[2]:


fn=input("Enter First Name ")
ln=input("Enter Last Name")
print("Last name is {} and First name is {}".format(ln,fn))
print("First Name and Last name in reverse are {} {}".format(ln[::-1],fn[::-1]))


# In[3]:


#find volumne of sphere
d=int(input("Enter Diameter"))
v=(4/3)*3.14*((d/2)**3)
print("Volume of sphere is {0} for diameter {1}".format(v,d))


# In[ ]:




