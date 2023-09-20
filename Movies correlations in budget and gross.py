#!/usr/bin/env python
# coding: utf-8

# In[4]:


# First let's import the packages we will use in this project
# You can do this all now or as you need them
import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib
plt.style.use('ggplot')
from matplotlib.pyplot import figure

get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12,8)

pd.options.mode.chained_assignment = None


# In[12]:


df = pd.read_csv(r'C:\Users\FAM\Downloads\archive\movies.csv')


# In[10]:


df.head(6)


# In[16]:


for c in df.columns:
    missing = np.mean(df[c].isnull())
    print('{} - {}%'.format(c, round(missing*100)))


# In[17]:


df.dtypes


# In[30]:


df['Correct year'] = df['released'].astype(str).str[:13]
df.head()


# In[31]:


df.sort_values(by=['gross'], inplace = False, ascending = True)
df.head()


# In[ ]:


del df['cy']
df.head()


# In[28]:


df.sort_values(by=['gross'], inplace = False, ascending = False)
df.head()


# In[31]:


df_descending = df.sort_values(by=['gross'], ascending=False)

# Sort in ascending order (lowest to highest gross)
df_ascending = df.sort_values(by=['gross'], ascending=True)

# Print the sorted DataFrames if you want to see the results
print("Descending Order:")
print(df_descending)

print("\nAscending Order:")
print(df_ascending)


# In[29]:


sns.regplot(x="gross", y="budget", data=df)


# In[15]:


sns.regplot(x="gross", y="budget", data=df)


# In[14]:


df.dtypes


# In[13]:


df.dtypes


# In[18]:


sns.regplot(x="gross", y="budget", data=df, scatter_kws = {"color": "red"}, line_kws = {"color": "blue"})
df.corr()


# In[22]:


c_matrix = df.corr()
sns.heatmap(c_matrix, annot = True)
plt.title("correlation of budget and gross")
plt.xlabel("gross")
plt.ylabel("budget")


# In[25]:


df_numerized = df
for c in df_numerized.columns:
    if(df_numerized[c].dtype=='object'):
        df_numerized[c] = df_numerized[c].astype('category')
        df_numerized[c] = df_numerized[c].cat.codes
df_numerized


# In[26]:


c_matrix = df.corr()
sns.heatmap(c_matrix, annot = True)
plt.title("correlation of budget and gross")
plt.xlabel("gross")
plt.ylabel("budget")


# In[ ]:




