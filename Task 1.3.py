#!/usr/bin/env python
# coding: utf-8

# # Task 1.3 (Statistical Analysis using Python)

# ### 	Descriptive statistics for both numerical and categorical and draw few insights from them.

# In[1]:


import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import f_oneway
from scipy.stats import chi2_contingency
from scipy.stats import ttest_1samp
from statsmodels.stats.multicomp import pairwise_tukeyhsd
import statsmodels.api as sm
data1=pd.read_csv("user_demographics.csv")
data1


# In[2]:


data2=pd.read_csv("User_product_purchase_details_p2.csv")
data2


# In[3]:


data=pd.merge(data1,data2,on='User_ID',how='right')
data.head(20)


# In[4]:



df=pd.DataFrame(data)
df


# In[5]:


df.fillna(0)


# lets know what types of data is present in our dataset

# In[6]:


df.info()


# In[7]:


df.shape


# In[8]:


df.isnull().sum()


# summary of the numerical data

# In[9]:


df.describe().T


# In[10]:


df.skew()


# In[11]:


sns.distplot(df['Purchase'],kde=False)


# In[12]:


df['Stay_In_Current_City_Years'].value_counts().plot.bar()


# In[13]:


df.kurtosis()


# summary of categorical data

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


# In[19]:


df['Product_ID'].value_counts()


# In[20]:


df['City_Category'].value_counts()


# In[21]:


df['Stay_In_Current_City_Years'].value_counts()


# In[22]:


df['Gender'].value_counts()


# In[23]:


df['Age'].value_counts()


# In[24]:


var=np.var(df)


# In[25]:


var


# few insights from our data as mentioned below

# 1) Our data set consists of 7 numerical attributes and 5 categorical attributes .from Descriptive statistics of numerical attributes we will be extracting the information of the data for every attribute      such as:
# 
#    count(number of rows)	
#    
#    mean	(average)
#    
#    std	(standard deviation)
#    
#    min	(minimum value)  
#    
#    25%	(1st quartile)
#    
#    50%	(median)
#    
#    75%	(3rd quartile)
#    
#    max	(maximum value)
# 
# 2) Numerical - User_ID,	Occupation, Marital_Status,	Product_Category_1,	Product_Category_2,	Product_Category_3,	Purchase
# 
# 
# 3) kurtosis() - return unbiased kurtosis(0=normal distribution, +ve=heavier tails, -ve=lighter tails)
# 
# 4) skew() - return unbiased skew(0=symmetrically distributed, +ve=right-skewed, -ve=left-skewed)
# 
# 5) from Descriptive statistics of categorical attributes we will be extracting the information of the data for every attribute    such as:
# 
#    count    (number of rows)
#    
#    unique   (number of unique values)
#    
#    top      (the most common repeated value)
#    
#    freq     (frequency of top)
#    
#    Name     (name of the attribute)
#    
#    dtype    (type of data)
# 
# 6) categorical - Product_ID, City_Category, Stay_In_Current_City_Years, Gender, Age
# 
# 7) value_counts() - counts of unique value
# 
# 

# 
# 
# 
# 
# 
# #  Perform relevant hypothesis testing (t, chi-Square, Anova tests)

# ### t-test

# test  to compare the purchases of the two genders listed in the dataset using a two sample t-test. The result of the t-test will show a p-value indicating if the two groups are significantly different from each other.

# H0-there is no significant difference in the average purchase done by male and female
# 
# Ha-there is significant difference in the average purchase done by male and female

# In[26]:


df.Purchase.groupby(df.Gender).mean()


# In[27]:


female=df[df.Gender=='F']
male=df[df.Gender=='M']


# In[28]:


from scipy.stats import ttest_ind


# In[29]:


ttest_ind(female.Purchase,male.Purchase,equal_var=False)


# hence p-value is < 0.05 accepts H0 and reject Ha

# ### ANOVA TEST

# whether  there is a correlation between the age groups in terms of purchase in dollars or not. The hypothesis test we will be going to use is the ANOVA Test.

# H0- there is a corelation between age groups in terms of purchase
# 
# Ha- there is no corelation between age groups in terms of purchase

# In[30]:


df.Purchase.groupby(df.Age).mean()


# In[31]:


age1=df[df.Age=='0-17'].Purchase
age2=df[df.Age=='18-25'].Purchase
age3=df[df.Age=='26-35'].Purchase
age4=df[df.Age=='36-45'].Purchase
age5=df[df.Age=='46-50'].Purchase
age6=df[df.Age=='51-55'].Purchase
age7=df[df.Age=='55+'].Purchase


# In[32]:


ttest, pval = f_oneway(age1, age2, age3, age4, age5, age6, age7)
pval


# hence p-value is > 0.05 accepts Ha and reject H0

# ### chi-square testing

# test that the purchased item category is correlated with the city the person came from and occupation. The hypothesis we will be using here is Chi-Square Test. In order to use a chi square test function, the data must be arranged in a contingency table.

# #### a person from city vs Product_Category_1

# H0- there is a correlation btween city in terms of Product_Category_1
# 
# Ha- there is no correlation btween city in terms of Product_Category_1

# In[33]:


cont_table = pd.crosstab(df.Stay_In_Current_City_Years, df.Product_Category_1)
cont_table


# In[34]:


chi2, pval, dof, expected = chi2_contingency(cont_table)
pval


# hence p-value is > 0.05 accepts Ha and reject H0

# #### a person from city vs Product_Category_2

# H0- there is a correlation btween city in terms of Product_Category_2
# 
# Ha- there is no correlation btween city in terms of Product_Category_2

# In[35]:


cont_table2 = pd.crosstab(df.Stay_In_Current_City_Years, df.Product_Category_2)
cont_table2


# In[36]:


chi2, pval, dof, expected = chi2_contingency(cont_table2)
pval


# hence p-value is > 0.05 accepts Ha and reject H0

# #### a person from city vs Product_Category_3

# H0- there is a correlation btween city in terms of Product_Category_3
# 
# Ha- there is no correlation btween city in terms of Product_Category_3

# In[37]:


cont_table3 = pd.crosstab(df.Stay_In_Current_City_Years, df.Product_Category_3)
cont_table3


# In[38]:


chi2, pval, dof, expected = chi2_contingency(cont_table3)
pval


# hence p-value is < 0.05 accepts H0 and reject H1

# #### occupation vs Product_Category_1,Product_Category_2,Product_Category_3

# H0- there is a correlation btween occupation in terms of Product_Category_1,Product_Category_2,Product_Category_3
# 
# Ha- there is no correlation btween occupation in terms of Product_Category_1,Product_Category_2,Product_Category_3

# In[39]:


cont_occ1 = pd.crosstab(df.Occupation, df.Product_Category_1)
cont_occ1


# In[40]:


cont_occ2 = pd.crosstab(df.Occupation, df.Product_Category_2)
cont_occ2


# In[41]:


cont_occ3 = pd.crosstab(df.Occupation, df.Product_Category_3)
cont_occ3


# In[42]:


chi2, pval, dof, expected = chi2_contingency(cont_occ1)
pval


# hence p-value is < 0.05 accepts H0 and reject H1

# In[43]:


chi2, pval, dof, expected = chi2_contingency(cont_occ2)
pval


# hence p-value is < 0.05 accepts H0 and reject H1

# In[44]:


chi2, pval, dof, expected = chi2_contingency(cont_occ3)
pval


# hence p-value is > 0.05 accepts Ha and reject H0

# In[ ]:




