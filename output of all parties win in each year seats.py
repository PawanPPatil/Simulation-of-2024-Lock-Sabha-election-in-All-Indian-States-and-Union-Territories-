#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np


# In[2]:


data=pd.read_csv("C:\\Users\\pawan\\OneDrive\\Desktop\\project data\\TCPD_GE_All_States_2023-12-23.csv\\All_States_GE.csv")
data.head()


# In[3]:


df=pd.DataFrame(data)
df


# In[8]:


# Group by Party and count the number of seats won by each party across all years
party_seat_counts_all_years = df[df['Position'] == 1].groupby(['Year', 'Party', 'State_Name'])['Position'].count().sort_values(ascending=False)

print("Number of seats won by each party across all years:")
print(party_seat_counts_all_years)


# In[9]:


df1 = pd.DataFrame(party_seat_counts_all_years)
df1


# In[12]:


output_data = party_seat_counts_all_years.reset_index()

# Extracting 'Year', 'Party', and 'Position' (Wining Seats)
year = output_data['Year']
party_name = output_data['Party']
wining_seats = output_data['Position']

# Creating a dictionary to store the data
data_dict = {
    'Year': year,
    'Party Name': party_name,
    'Wining Seats': wining_seats
}

# Creating a DataFrame from the dictionary
output_df = pd.DataFrame(data_dict)
output_df


# In[14]:


import pandas as pd
output_df.to_csv('C:\\Users\\pawan\\OneDrive\\Desktop.csv', index=False)


# In[ ]:




