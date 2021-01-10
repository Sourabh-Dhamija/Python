#!/usr/bin/env python
# coding: utf-8

# In[3]:


def filter_long_words(l,n):
    new_l=[]
    for i in l:
        if len(i) > n:
            new_l.append(i)
        else:
            pass
    return new_l

li=['sourabh','dhamija','anuj','aditya','sapna']
filter_long_words(li,5)


# In[4]:


def length_of_words(l):
    return [len(i) for i in l]

length_of_words(li)


# In[15]:


def check_vowel(c):
    if len(c) == 1:
        if c.lower() in ('a','e','i','o','u'):
            return True
        else:
            return False
    else:
        print('Please enter single character only')
check_vowel('v')


# In[64]:


class Tringle_input:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def print(self):
        print("entered values are {0}, {1}, {2}".format(self.a,self.b,self.c))
    
class tringle_area(Tringle_input):
    def calc_area(self):
        self.s=(self.a+self.b+self.c)/2
        self.area=(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))**0.5
        return self.area
        
area=tringle_area(9,10,11)
area.calc_area()        


# In[ ]:




