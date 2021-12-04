#!/usr/bin/env python
# coding: utf-8

# # Data Manipulation 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


path1="user_demographics.csv"


# In[3]:


path2="User_product_purchase_details_p2.csv"


# In[4]:


data1=pd.read_csv(path2)
data1


# In[5]:


data2=pd.read_csv(path1)
data2


# In[6]:


df1=pd.DataFrame(data1)
df1


# In[7]:


df2=pd.DataFrame(data2)
df2


# ### Summary of datasets

# In[8]:


df1.info()


# In[9]:


df2.info()


# Merge the above two datasets to one dataset

# In[10]:


data=pd.merge(data1,data2,on='User_ID',how='right')
data.head(20)


# In[11]:


data.info()


# ### Describing the numerical and categorical data

# 
# describing the numerical data gives you statistical details like percentile,mean,std etc

# In[12]:


df=pd.DataFrame(data)


# In[13]:


df.describe()


# describing the categorical data gives you details like top,frequency,count etc

# In[14]:


df['Product_ID'].describe()


# In[15]:


df['City_Category'].describe()


# In[16]:


df['Stay_In_Current_City_Years'].describe()


# In[17]:


df['Gender'].describe()


# In[18]:


df['Age'].describe()


# lets know about the unique values present in every column

# In[19]:


data['Product_ID'].unique()


# In[20]:


data['City_Category'].unique()


# In[21]:


data['Stay_In_Current_City_Years'].unique()


# In[22]:


data.groupby('Stay_In_Current_City_Years')['Stay_In_Current_City_Years'].count()


# In[23]:


data['Marital_Status'].unique()


# In[24]:


data.groupby('Marital_Status')['Marital_Status'].count()


# In[25]:


objectcat1=data['Product_Category_1'].unique()
objectcat1


# In[26]:


data.groupby('Product_Category_1')['Product_Category_1'].count()


# In[27]:


data['Product_Category_2'].unique()


# In[28]:


data.groupby('Product_Category_2')['Product_Category_2'].count()


# In[29]:


data['Product_Category_3'].unique()


# In[30]:


data.groupby('Product_Category_3')['Product_Category_3'].count()


# In[31]:


data['Gender'].unique()


# In[32]:


data.groupby('Gender')['Gender'].count()


# In[33]:


data['Age'].unique()


# In[34]:


data.groupby('Age')['Age'].count()


# In[35]:


data['Occupation'].unique()


# In[36]:


data.groupby('Occupation')['Occupation'].count()


# # Task1-Maximum, spend in different categories of products

# product_category_1

# In[37]:


data.groupby('Product_Category_1').sum()['Purchase']


# product_category_1

# In[38]:


data.groupby('Product_Category_2').sum()['Purchase']


# In[39]:


data.groupby('Product_Category_3').sum()['Purchase']


# # Based on above data which set of customers can be offered personalised discount vouchers

# 
# Based on age analyze the purchase rate

# In[40]:


data.groupby("Age").sum()['Purchase']


# Based on city analyze the purchase rate

# In[41]:


data.groupby("City_Category").sum()['Purchase']


# Based on gender analyze the purchase rate

# In[42]:


data.groupby("Gender").sum()['Purchase']


# Based on occupation analyze the purchase rate

# In[43]:


data.groupby("Occupation").sum()['Purchase']


# Based on Marital_Status analyze the purchase rate
# 

# In[44]:


data.groupby("Marital_Status").sum()['Purchase']


# In[45]:


data1 = df.groupby('Age')['Product_ID'].apply(lambda x: x.value_counts().index[0]).reset_index()
data1


# In[46]:


df["Product_ID"].value_counts(sort=True)[:10]


# # Based on above data which set of customers can be offered personalised discount vouchers

# the personalised discount vouchers are provide to those customers whose age lies in between 26-35 irrespective of their gender and occupation

# 
# 
# 
# # And in which category the voucher should be offered

# the voucher is apllicable on the prodcut category where the product_id is P00265242 

# # Or it should be on the total amount

# yes, we can provide the discount on total amount for the top 10 active users.
# 

# In[ ]:





# In[ ]:





# In[ ]:




