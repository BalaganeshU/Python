#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
import numpy as np


# In[2]:


os.getcwd()


# In[46]:


cars=pd.read_csv('cars.csv')


# In[47]:


cars


# In[48]:


#1- How many Rows are in the cars dataset?
cars.shape[0]


# In[49]:


#2- How many Columns are in the car's data set?
cars.shape[1]


# In[50]:


#3- How many unique numbers of cylinders we have in the cars dataset?
cars.cylenders.value_counts()


# In[51]:


cars.cylenders.unique()


# In[52]:


#4- what is the average horsepower of cars? 
cars.horsepower.describe()


# In[53]:


#5- what is the maximum horsepower?
Answer = 500


# In[54]:


#6- what is the most expensive car?
cars[cars.Price==max(cars.Price)]


# In[60]:


#7- change the name of the column "name" to "car name"
cars=cars.rename(columns={'name':'car_name'})


# In[58]:


cars


# In[94]:


#8- make a subset of the data that has the car name, the price and name the new sub-setted data frame  car pricing.
car_pricing=cars.loc[:,['car_name','Price']]
car_pricing


# In[ ]:


#9- create a function called pricing category that returns "Budget Car " if the cars are less than 20,000 USD,
#" Suitable Car " is the car is more than 20,000 and less than 35 000 and finally 
#an expensive car for cars more than 35000. 
def pricing_category(car):
    if car<=20000:
        return 'Budget'
    elif ((car>20000) & (car<35000)):
        return 'Suitable Car'
    else: return 'Expensive Car'


# In[141]:


#10- create a column named category on the subset using a for loop and pricing category function.
for i in range(car_pricing.shape[0]):
    car_pricing.loc[i,'category']=pricing_category(car_pricing.Price[i])


# In[142]:


car_pricing


# In[144]:


#11- How many Budget cars, suitable cars, and expensive cars we have?
car_pricing.category.value_counts()


# In[ ]:




