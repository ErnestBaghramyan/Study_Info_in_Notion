#!/usr/bin/env python
# coding: utf-8

# ## Data Cleaning

# In[1]:


import pandas as pd


# In[53]:


df = pd.read_excel("/Users/ernestbaghramyan/Downloads/Customer Call List.xlsx")
df


# In[54]:


df = df.drop_duplicates()
df


# In[55]:


df = df.drop(columns = "Not_Useful_Column")
df


# In[56]:


# We can remove one by one using strip/lstrip/rstrip
# df["Last_Name"] = df["Last_Name"].str.lstrip("...") # Strip from the left side "..." and remove it
# df["Last_Name"] = df["Last_Name"].str.lstrip("/")
# df["Last_Name"] = df["Last_Name"].str.rstrip("_") # Strip from the right side "_" and remove it

# We can remove multiple simbols also using strip function - strpi("./_*")
df["Last_Name"] = df["Last_Name"].str.strip("./_")

df


# In[58]:


# Step 1 - replaceing with "" everything that we don't need
# df["Phone_Number"] = df["Phone_Number"].str.replace("[^a-zA-Z0-9]","") # "[^a-zA-Z0-9]" means everything except
    # lowwer and upper case letters and numbers

# Just testing lambda function
# df["Phone_Number"].apply(lambda x: x[0:3] + "-" + x[3:6] + "-" + x[6:10])

# Step 2 - as we have both int and flout types, converting everything to str, as lambda works with it if we need some aggregation - Check the upper lambda function
# df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))

# Step 3 - as now er have str to work with, we are running lambda funstion to get the needed format "xxx-xxx-xxxx"
# df["Phone_Number"] =  df["Phone_Number"].apply(lambda x: x[0:3] + "-" + x[3:6] + "-" + x[6:10])

# Step 4 - replacing all that is not needed - in this case "nan--" & "Na--"
df["Phone_Number"] = df["Phone_Number"].str.replace("nan--","")
df["Phone_Number"] = df["Phone_Number"].str.replace("Na--","")

df


# In[64]:


df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(",",2, expand = True)
df


# In[67]:


df["Paying Customer"] = df["Paying Customer"].str.replace("Yes", "Y")
df["Paying Customer"] = df["Paying Customer"].str.replace("No", "N")
df


# In[68]:


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes", "Y")
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("No", "N")
df


# In[76]:


# df = df.replace("N/a","")
# df = df.replace("NaN","") # This won't work as "NaN" is kind of value and it shows that the cell is empty, null, none
df = df.fillna("") # for na values (NaN, None) we are filling ""
df


# In[77]:


for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == "Y":
        df.drop(x, inplace = True)

df


# In[78]:


for x in df.index:
    if df.loc[x, "Phone_Number"] == "":
        df.drop(x, inplace = True)


df

# Another way to drop null values
# df = df.dropna(subset = "Phone_Number", inplace = True)


# In[80]:


df = df.reset_index(drop = True)
df


# In[ ]:





# In[ ]:





# In[ ]:




