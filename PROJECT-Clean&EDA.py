#!/usr/bin/env python
# coding: utf-8

# In[74]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import numpy as np


# In[75]:


df=pd.read_csv("AllCitysCSV/combined_csv.csv")
df


# In[76]:


df = df.drop(columns='Unnamed: 0', axis=1)
df = df.drop('Property Type', axis=1)
df = df.drop('Distance To Beach', axis=1)
df


# In[ ]:






# In[77]:


###REPLACE ALL VALUES:   1 = yes, 2 = no, -1 = not exist

df.replace('NAN', 0, inplace=True)#NAN that we made for thing there are not appeard.
df['Free Cancle'].replace('Free Cancle', 1, inplace=True)
df['Pool'].replace('Swimming pool', 1, inplace=True)
df['Parking'].replace('Parking', 1, inplace=True)
df['Restaurant'].replace('Restaurant', 1, inplace=True)
df['GYM'].replace('Fitness centre', 1, inplace=True)
df['Air Condition'].replace('Air conditioning', 1, inplace=True)
df['Disabled Access'].replace('Facilities for disabled guests', 1, inplace=True)
df['WiFi'].replace('Free WiFi', 1, inplace=True)
df['SPA'].replace('Spa and wellness centre', 1, inplace=True)
df['Balcony'].replace('Balcony', 1, inplace=True)
df['View'].replace('View', 1, inplace=True)
df['Rating'].fillna(-1, inplace=True)
#df = df[df['Rating'] != -1]
#df['Distance To Beach'].fillna(-1, inplace=True)
df['Review Number'].replace('nan', 0, inplace=True)

#The lambda function uses a regular expression to extract any sequences of digits
df['Review Number'] = df['Review Number'].astype(str)
df['Review Number'] = df['Review Number'].apply(lambda x: int(re.findall("\d+,?\d+", x)[0].replace(',', '')) if re.findall("\d+,?\d+", x) else 0)

df['Price'] = df['Price'].astype(str)
df['Price'] = df['Price'].apply(lambda x: int(re.findall("\d+,?\d+", x)[0].replace(',', '')) if re.findall("\d+,?\d+", x) else 0)


# In[78]:


df


# In[79]:


#### delete the km and meter in distance
def extract_distance(value):
    if type(value) == str:
        if "km" in value:
            value = float(value.split()[0])
            value *= 1000
        elif "m" in value:
            value = float(value.split()[0])
    return value

df['Distance To Center'] = df['Distance To Center'].apply(extract_distance)
#df['Distance To Beach'] = df['Distance To Beach'].apply(extract_distance)


# In[80]:


df


# In[81]:


df = df[df['Rating'] != -1]
df


# In[ ]:





# In[82]:


sns.scatterplot(x='Rating', y='Price', data=df)
plt.show()


# In[83]:


#clean the price outliers
Q1 = df.Price.quantile(0.25)
Q3 = df.Price.quantile(0.75)
IQR = Q3 - Q1

df = df[~((df.Price < (Q1 - 1.5 * IQR)) | (df.Price > (Q3 + 1.5 * IQR)))]
sns.scatterplot(x='Rating', y='Price', data=df)
plt.show()


# In[ ]:





# In[84]:


sns.scatterplot(x='Price', y='City', data=df)
plt.show()


# In[85]:


###### COMBINE THE CITYS
df['City'] = np.where(df['City'].str.contains("Atlanta"), 'Atlanta', df['City'])
df['City'] = np.where(df['City'].str.contains("New York"), 'New York', df['City'])
df['City'] = np.where(df['City'].str.contains("Houston"), 'Houston', df['City'])
df['City'] = np.where(df['City'].str.contains("Los Angeles"), 'Los Angeles', df['City'])
df['City'] = np.where(df['City'].str.contains("Orlando"), 'Orlando', df['City'])

df['City'] = np.where(df['City'].str.contains("San Antonio"), 'San Antonio', df['City'])
df['City'] = np.where(df['City'].str.contains("New Orleans"), 'New Orleans', df['City'])
df['City'] = np.where(df['City'].str.contains("San Diego"), 'San Diego', df['City'])
df['City'] = np.where(df['City'].str.contains("Austin"), 'Austin', df['City'])
df['City'] = np.where(df['City'].str.contains("Chicago"), 'Chicago', df['City'])

df['City'] = np.where(df['City'].str.contains("Las Vegas"), 'Las Vegas', df['City'])
df['City'] = np.where(df['City'].str.contains("Miami"), 'Miami', df['City'])


sns.scatterplot(x='Price', y='City', data=df)
plt.show()


# In[87]:


sns.scatterplot(x='Price', y='Review Number', data=df)
plt.show()


# In[88]:


#clean the Review Number outliers
Q1 = df['Review Number'].quantile(0.25)
Q3 = df['Review Number'].quantile(0.75)
IQR = Q3 - Q1

df = df[~((df['Review Number'] < (Q1 - 1.5 * IQR)) | (df['Review Number'] > (Q3 + 1.5 * IQR)))]
sns.scatterplot(x='Price', y='Review Number', data=df)

plt.show()


# In[ ]:





# In[89]:


sns.barplot(x='Restaurant', y='Price', data=df, label="No Restaurant")
plt.legend()
plt.show()


# In[90]:


df


# In[ ]:





# In[91]:


sns.scatterplot(x='Price', y='Room Kind', data=df)
plt.show()


# In[96]:


df['Room Kind'] = np.where(df['Room Kind'].str.contains("Suite"), 'Suite', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("SUITE"), 'Suite', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("King"), 'King', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("KING"), 'King', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Deluxe"), 'Deluxe', df['Room Kind'])

df['Room Kind'] = np.where(df['Room Kind'].str.contains("Queen"), 'Queen ', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Standard"), 'Standard ', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Loft"), 'Studio', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Studio"), 'Studio ', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Room"), 'Standard', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Standard"), 'Standard', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Guest"), 'Standard', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Apartment"), 'Apartment', df['Room Kind'])

df['Room Kind'] = np.where(df['Room Kind'].str.contains("Bed","BED"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Classic"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Twin"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Pad"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Pied"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Company"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Full"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("House"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Double"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("House"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Mama"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Cozy"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("View"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("offer"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Snug"), 'Other', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("other"), 'Other', df['Room Kind'])
sns.barplot(x='Room Kind', y='Price', data=df)
plt.show()


# In[97]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[99]:


df['City'] = np.where(df['City'].str.contains("Atlanta"), '1', df['City'])
df['City'] = np.where(df['City'].str.contains("New York"), '2', df['City'])
df['City'] = np.where(df['City'].str.contains("Houston"), '3', df['City'])
df['City'] = np.where(df['City'].str.contains("Los Angeles"), '4', df['City'])
df['City'] = np.where(df['City'].str.contains("Orlando"), '5', df['City'])
df['City'] = np.where(df['City'].str.contains("San Antonio"), '6', df['City'])
df['City'] = np.where(df['City'].str.contains("New Orleans"), '7', df['City'])
df['City'] = np.where(df['City'].str.contains("Miami"), '8', df['City'])
df['City'] = np.where(df['City'].str.contains("Austin"), '9', df['City'])
df['City'] = np.where(df['City'].str.contains("Chicago"), '10', df['City'])
df['City'] = np.where(df['City'].str.contains("Las Vegas"), '11', df['City'])
df['City'] = np.where(df['City'].str.contains("San Diego"), '12', df['City'])


# In[100]:


df


# In[101]:


df['Room Kind'] = np.where(df['Room Kind'].str.contains("Suite"), '1', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("King"), '2', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Deluxe"), '3', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Queen"), '4 ', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Standard"), '5 ', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Studio"), '6 ', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Apartment"), '7', df['Room Kind'])
df['Room Kind'] = np.where(df['Room Kind'].str.contains("Other"), '8', df['Room Kind'])


# In[102]:


sns.displot(df, x="Price", col="City")


# In[103]:


df


# In[ ]:





# In[ ]:





# In[104]:


df.to_csv("clean.csv")


# In[ ]:





# In[ ]:




