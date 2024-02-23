#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[6]:


df=pd.read_csv("C:\\Users\\pawan\\OneDrive\\Desktop\\clear\\New folder\\All_States_GE.csv")


# In[8]:


df


# In[23]:


# Assuming df is your DataFrame containing the election data
# Replace 'df' with the actual name of your DataFrame

# Define the list of parties
parties = ['BJP','INC', 'DMK', 'AITC', 'YSRCP', 'SHS', 'JD(U)', 'BJD', 'BSP', 'TRS', 'NCP']

for party in parties:
    # Filter the data for the year 2019 and the current party
    df_party = df[(df['Year'] == 2019) & (df['Party'] == party)]

    # Count the total number of candidates for the current party
    total_candidates = df_party['Candidate'].nunique()

    # Count the number of candidates from the current party who secured the first position
    candidates_first_position = df_party[df_party['Position'] == 1]['Candidate'].nunique()

    print("Total number of", party, "candidates who participated in the 2019 election:", total_candidates)
    print("Number of", party, "candidates who secured the first position in the 2019 election:", candidates_first_position)
    print()


# In[24]:


# Assuming df is your DataFrame containing the election data
# Replace 'df' with the actual name of your DataFrame

# Define the list of parties
parties = ['BJP','INC', 'DMK', 'AITC', 'YSRCP', 'SHS', 'JD(U)', 'BJD', 'BSP', 'TRS', 'NCP']

for party in parties:
    # Filter the data for the year 2019 and the current party
    df_party = df[(df['Year'] == 2019) & (df['Party'] == party)]

    # Count the total number of candidates for the current party
    total_candidates = df_party['Candidate'].nunique()

    # Count the number of candidates from the current party who secured the first position
    candidates_first_position = df_party[df_party['Position'] == 1]['Candidate'].nunique()

    # Calculate the proportion of candidates from the current party who secured the first position
    proportion_first_position = (candidates_first_position / total_candidates) * 100

    print("Proportion of", party, "candidates who secured the first position in the 2019 election: {:.2f}%".format(proportion_first_position))


# In[29]:


# Assuming df is your DataFrame containing the election data
# Replace 'df' with the actual name of your DataFrame

# Define the list of parties
parties = ['BJP','INC', 'ADMK', 'AITC', 'YSRCP', 'SHS', 'CPM', 'BJD', 'TDP', 'TRS']

for party in parties:
    # Filter the data for the year 2014 and the current party
    df_party = df[(df['Year'] == 2014) & (df['Party'] == party)]

    # Count the total number of candidates for the current party
    total_candidates = df_party['Candidate'].nunique()

    # Count the number of candidates from the current party who secured the first position
    candidates_first_position = df_party[df_party['Position'] == 1]['Candidate'].nunique()

    print("Total number of", party, "candidates who participated in the 2014 election:", total_candidates)
    print("Number of", party, "candidates who secured the first position in the 2014 election:", candidates_first_position)
    print()


# In[25]:


# Assuming df is your DataFrame containing the election data
# Replace 'df' with the actual name of your DataFrame

# Define the list of parties
parties = ['BJP','INC', 'ADMK', 'AITC', 'YSRCP', 'SHS', 'CPM', 'BJD', 'TDP', 'TRS']

for party in parties:
    # Filter the data for the year 2014 and the current party
    df_party = df[(df['Year'] == 2014) & (df['Party'] == party)]

    # Count the total number of candidates for the current party
    total_candidates = df_party['Candidate'].nunique()

    # Count the number of candidates from the current party who secured the first position
    candidates_first_position = df_party[df_party['Position'] == 1]['Candidate'].nunique()

    # Calculate the proportion of candidates from the current party who secured the first position
    proportion_first_position = (candidates_first_position / total_candidates) * 100

    print("Proportion of", party, "candidates who secured the first position in the 2019 election: {:.2f}%".format(proportion_first_position))


# In[30]:


# Assuming df is your DataFrame containing the election data
# Replace 'df' with the actual name of your DataFrame

# Define the list of parties
parties = ['BJP','INC', 'DMK', 'AITC', 'SP', 'SHS', 'CPM', 'BJD', 'BSP', 'JD(U)']

for party in parties:
    # Filter the data for the year 2009 and the current party
    df_party = df[(df['Year'] == 2009) & (df['Party'] == party)]

    # Count the total number of candidates for the current party
    total_candidates = df_party['Candidate'].nunique()

    # Count the number of candidates from the current party who secured the first position
    candidates_first_position = df_party[df_party['Position'] == 1]['Candidate'].nunique()

    print("Total number of", party, "candidates who participated in the 2009 election:", total_candidates)
    print("Number of", party, "candidates who secured the first position in the 2009 election:", candidates_first_position)
    print()


# In[31]:


# Assuming df is your DataFrame containing the election data
# Replace 'df' with the actual name of your DataFrame

# Define the list of parties
parties = ['BJP','INC', 'DMK', 'AITC', 'SP', 'SHS', 'CPM', 'BJD', 'BSP', 'JD(U)']

for party in parties:
    # Filter the data for the year 2009 and the current party
    df_party = df[(df['Year'] == 2009) & (df['Party'] == party)]

    # Count the total number of candidates for the current party
    total_candidates = df_party['Candidate'].nunique()

    # Count the number of candidates from the current party who secured the first position
    candidates_first_position = df_party[df_party['Position'] == 1]['Candidate'].nunique()

    # Calculate the proportion of candidates from the current party who secured the first position
    proportion_first_position = (candidates_first_position / total_candidates) * 100

    print("Proportion of", party, "candidates who secured the first position in the 2009 election: {:.2f}%".format(proportion_first_position))


# In[32]:


# Assuming df is your DataFrame containing the election data
# Replace 'df' with the actual name of your DataFrame

# Define the list of parties
parties = ['BJP','INC', 'DMK', 'AITC', 'SP', 'SHS', 'CPM', 'BJD', 'BSP', 'JD(U)']

for party in parties:
    # Filter the data for the year 2004 and the current party
    df_party = df[(df['Year'] == 2004) & (df['Party'] == party)]

    # Count the total number of candidates for the current party
    total_candidates = df_party['Candidate'].nunique()

    # Count the number of candidates from the current party who secured the first position
    candidates_first_position = df_party[df_party['Position'] == 1]['Candidate'].nunique()

    print("Total number of", party, "candidates who participated in the 2004 election:", total_candidates)
    print("Number of", party, "candidates who secured the first position in the 2004 election:", candidates_first_position)
    print()


# In[33]:


# Assuming df is your DataFrame containing the election data
# Replace 'df' with the actual name of your DataFrame

# Define the list of parties
parties = ['BJP','INC', 'DMK', 'AITC', 'SP', 'SHS', 'CPM', 'BJD', 'BSP', 'JD(U)']

for party in parties:
    # Filter the data for the year 2004 and the current party
    df_party = df[(df['Year'] == 2004) & (df['Party'] == party)]

    # Count the total number of candidates for the current party
    total_candidates = df_party['Candidate'].nunique()

    # Count the number of candidates from the current party who secured the first position
    candidates_first_position = df_party[df_party['Position'] == 1]['Candidate'].nunique()

    # Calculate the proportion of candidates from the current party who secured the first position
    proportion_first_position = (candidates_first_position / total_candidates) * 100

    print("Proportion of", party, "candidates who secured the first position in the 2004 election: {:.2f}%".format(proportion_first_position))

