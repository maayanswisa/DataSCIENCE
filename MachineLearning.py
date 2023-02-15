#!/usr/bin/env python
# coding: utf-8

# In[169]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor 


# In[170]:


get_ipython().system('pip install xgboost')


# In[171]:


from xgboost import XGBRegressor


# In[172]:


df=pd.read_csv("clean.csv")
df


# In[173]:


df = df.drop('Property Name', axis=1)
df = df.drop(columns='Unnamed: 0')
df = df.drop('Staff Rating', axis=1)
#df = df.drop('Distance To Beach', axis=1)


# In[ ]:





# In[174]:


df


# In[175]:


train_data, test_data, train_target, test_target = train_test_split(df.drop("Rating", axis=1), df["Rating"], test_size=0.2)
#train_data, test_data, train_target, test_target = train_test_split(df.drop("Price", axis=1), df["Price"], test_size=0.2)


# In[176]:


#cities = np.unique(df["City"])
#cities_dfs = []
#for city in cities:
 #   city_df = df[df["City"] == city].reset_index(drop=True)
 #   city_prices = city_df["Price"].values
 #   city_df.loc[:, "Price"] = (city_prices - np.mean(city_prices)) / np.std(city_prices)
 #   cities_dfs.append(city_df)

#df = pd.concat(cities_dfs)
df



# In[177]:


#df = df.drop('City', axis=1)


# In[178]:


#pd.get_dummies(df)


# In[179]:


#df= pd.get_dummies(df, columns=["City"],drop_first=True)
#df= pd.get_dummies(df, columns=["Room Kind"],drop_first=True)


# In[180]:


#df.to_csv("clean1.csv")


# In[181]:


#model = LinearRegression()
#model = RandomForestRegressor()
model = XGBRegressor(max_depth=10)


# train the model using the training data
model.fit(train_data, train_target)


# In[182]:


#model.feature_importances_


# In[183]:


#pd.Series(model.feature_importances_, index=train_data.columns)


# In[184]:


test_prediction = model.predict(test_data)
train_prediction = model.predict(train_data)
# calculate the mean absolute error
mae = mean_absolute_error(test_target, test_prediction)
print("Mean Absolute Error:", mae)


# In[185]:


r2  = r2_score(test_target, test_prediction)
r2


# In[186]:


r2train  = r2_score(train_target, train_prediction)
r2train


# In[ ]:





# In[187]:


plt.figure()
plt.scatter(train_target, train_prediction)
plt.xlabel("true")
plt.ylabel("predictions")
plt.show()


# In[188]:


plt.figure()
plt.scatter(test_target, test_prediction)
plt.xlabel("true")
plt.ylabel("predictions")
plt.show()


# In[ ]:





# In[ ]:





# In[22]:


#pd.Series(model.feature_importances_, index=train_data.columns)


# In[ ]:





# In[ ]:




