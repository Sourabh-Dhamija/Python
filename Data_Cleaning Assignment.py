#!/usr/bin/env python
# coding: utf-8

# In[160]:


import pandas as pd
import numpy as np

df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN','londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
                    'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
                    'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
                    'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )','12. Air France', '"Swiss Air"']})
df1=df.copy()


# In[161]:


#while loop added to handle consecutive missing values
while(df1['FlightNumber'].isna().any()):
    df1['FlightNumber'].fillna(df1['FlightNumber'].shift(1)+10,inplace=True)
df1['FlightNumber']=df1['FlightNumber'].astype(int)
df1


# In[162]:


df1['From']=df1['From_To'].str.split('_',n=1,expand=True)[0]
df1['To']=df1['From_To'].str.split('_',n=1,expand=True)[1]
df1['From']=df1['From'].str.capitalize()
df1['To']=df1['To'].str.capitalize()
df1.drop(columns='From_To',inplace=True)


# In[163]:


df1


# In[140]:


# df3=pd.DataFrame()
# df3=pd.DataFrame(df1['RecentDelays'].tolist(),dtype=np.int)
# df3.add_prefix('Delay_')


# In[164]:


df2=pd.DataFrame([pd.Series(x).astype(int) for x in df1['RecentDelays']])
df2.columns=['Delay_{}'.format(x+1) for x in df2.columns]


# In[171]:


df1=df1.join(df2)


# In[186]:


df1


# In[ ]:




