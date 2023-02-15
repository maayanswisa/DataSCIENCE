#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import glob

# get all the csv files in the current directory
all_filenames = glob.glob("*.csv")

# combine all the csv files into one dataframe
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

# save the combined csv file
combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')##'utf-8-sig' - help prevent issues with reading or writing files


# In[5]:


df_hotel=pd.read_csv("combined_csv.csv")


# In[6]:


df_hotel


# In[ ]:




