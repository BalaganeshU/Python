#!/usr/bin/env python
# coding: utf-8

# In[304]:


import os
import pandas as pd
import numpy as np


# In[305]:


os.getcwd()


# In[306]:


file=pd.read_csv('online_retail2.csv')


# In[307]:


file


# In[308]:


file.head()


# In[309]:


file.tail()


# In[310]:


file.shape


# In[311]:


file.Quantity.describe()


# In[312]:


file.info()


# In[313]:


first_five=file.iloc[0:5,0:5]


# In[314]:


first_five


# In[315]:


two_columns=file.loc[:,['Invoice','Quantity']]


# In[316]:


two_columns


# In[317]:


second_subset=file.iloc[[1,3,5],[1,2,4]]


# In[318]:


second_subset


# In[319]:


file.columns


# In[320]:


#creating new column
file['price_USD']=file.Price*1.28


# In[321]:


file


# In[322]:


bala=30
ganesh=25
aadi=20
vivek=15


# In[323]:


def status(person):
    if (person>=25):
        return('adult')
    elif (person>=20):
        return('teenager')
    else:
        return('child')


# In[324]:


class_list=[bala,ganesh,aadi,vivek]


# In[325]:


map_object=map(status,class_list)


# In[326]:


list(map_object)


# In[327]:


for age in class_list:
    print(age)


# In[328]:


for age in class_list:
    print(status(age))


# In[329]:


status_list=[]
for age in class_list:
    status_list.append(status(age))
status_list


# In[330]:


def ukornot(country):
    if (country=='United Kingdom'):
        return True
    else:return False


# In[331]:


ukornot('United kingdom')


# In[332]:


ukornot('France')


# In[333]:


file['uk']=file['Country'].map(ukornot)


# In[334]:


file['uk'].value_counts()


# In[339]:


first_10=file.iloc[0:10,:]


# In[340]:


first_10


# In[341]:


first_10['uk1']=np.nan


# In[342]:


first_10


# In[345]:


first_10.shape[0]


# In[347]:


for i in range(0,first_10.shape[0]):
    first_10.loc[i,'uk1']=ukornot(first_10.Country[i])


# In[348]:


first_10


# In[ ]:




