#!/usr/bin/env python
# coding: utf-8

# ### Red Wine and White Wine 

# In[1]:


import pandas as pd


# In[2]:


RW_df = pd.read_csv('winequality-red.csv', delimiter = ';')
WW_df = pd.read_csv('winequality-white.csv', delimiter = ';')


# In[3]:


RW_df.head()


# In[4]:


WW_df.head()


# In[5]:


WW_df['type'] = 'White Wine'
RW_df['type'] = 'Red Wine'


# In[6]:


WW_df.head()


# In[7]:


RW_df.head()


# In[8]:


df_wines = pd.concat([WW_df, RW_df])


# In[9]:


df_wines


# In[ ]:





# ### Wine Sales 

# In[10]:


import pandas as pd


# In[12]:


winesales_df = pd.read_csv('winesales.csv')


# In[13]:


winesales_df.head()


# In[14]:


winesales_df.reset_index(drop = True, inplace = True)


# In[15]:


winesales_df


# In[ ]:





# ### Examples of Plots and Graphs

# In[19]:


import seaborn as sns

sns.relplot(x = 'points', y = 'price', kind = 'line', data = winesales_df)


# In[20]:


sns.relplot(x = 'quality', y = 'alcohol', kind = 'line', data = df_wines)


# In[22]:


sns.relplot(x = 'quality', y = 'fixed acidity', kind = 'line', data = df_wines)


# In[24]:


sns.relplot(x = 'quality', y = 'volatile acidity', kind = 'line', data = df_wines)


# In[25]:


sns.relplot(x = 'quality', y = 'citric acid', kind = 'line', data = df_wines)


# In[26]:


sns.relplot(x = 'quality', y = 'sulphates', kind = 'line', data = df_wines)


# In[28]:


sns.relplot(x = 'quality', y =  'alcohol', hue = 'type', kind = 'line' ,data = df_wines )


# In[ ]:





# ### Quality Label 

# In[31]:


# 7, 8,9 : high
# 5,6: medium
# 3,4 : low


# In[32]:


def label(x):
    if (x == 8) or (x == 9) or (x == 7)  :
        return 'High'
    
    elif x in [5, 6]:
        return 'Medium'
    else:
        return 'Low'


# In[33]:


df_wines['quality_label'] = df_wines['quality'].apply(lambda x: label(x))


# In[34]:


df_wines['quality_label'].value_counts()


# In[35]:


df_wines['quality_label'] = df_wines['quality'].apply(lambda x: 'High' if (x >=8) else 'Medium' if (x >=5) else 'Low')


# In[36]:


df_wines.head()


# In[ ]:





# In[39]:


sns.relplot(x = 'fixed acidity', y =  'alcohol', col = 'quality_label', col_wrap = 2,hue='type' ,data = df_wines )


# In[42]:


sns.relplot(x = 'citric acid', y =  'alcohol', col = 'quality_label', col_wrap = 2,hue='type' ,data = df_wines )


# In[43]:


sns.catplot(x = 'type', y = 'alcohol', kind = 'box', data = df_wines )


# In[45]:


sns.histplot(data=df_wines, x="alcohol")


# In[46]:


sns.histplot(data=df_wines, x="alcohol", hue="type")


# In[48]:


sns.histplot(df_wines, x="alcohol", hue="type", element="step")


# In[49]:


sns.histplot(df_wines, x="citric acid", hue="type", element="step")


# In[56]:


sns.relplot(x="alcohol", y="fixed acidity", hue="type",
            dashes=False, markers=True, kind="line", data=df_wines);


# In[60]:


sns.relplot(x="alcohol", y="quality", hue="type",
            dashes=False, markers=True, kind="line", data=df_wines);


# In[62]:


sns.relplot(x="fixed acidity", y="quality", hue="type",
            dashes=False, markers=True, kind="line", data=df_wines);


# ### PLT - Wine Sales 

# In[69]:


import matplotlib.pyplot as plt


# In[70]:



ax=(winesales_df['country'].value_counts().head(15) / len(winesales_df)).plot.bar(figsize=(14,6))
ax.set_title("Percentage of Top 15 Countries", fontsize=20,color= "magenta")
plt.grid()


# In[72]:


ax=(winesales_df['country'].value_counts().head(15) / len(winesales_df)).plot.bar(figsize=(14,6))
ax.set_title("Percentage of Top 10 Countries", fontsize=20,color= "red")
plt.grid()


# In[73]:


ax=winesales_df['variety'].value_counts().head(30).plot.bar(figsize=(14,6))
ax.set_title("Top 30 Wine Varieties", fontsize=20,color="magenta")
plt.grid()


# In[74]:


winesales_df.country.dropna(inplace = True)
labels = winesales_df.country.value_counts().index
labels_1=(labels[0:12])
colors = ['grey','blue','red','yellow','green','brown',"lime","cyan","magenta","purple","yellow","pink"]
explode = [0,0,0,0,0,0,0,0,0,0,0,0]
sizes = winesales_df.country.value_counts().values
array_1=(sizes[0:12])

# visual
plt.figure(figsize = (10,10))
plt.pie(array_1, explode=explode, labels=labels_1, colors=colors, autopct='%1.1f%%')
plt.title('Percentage per Country',color = 'blue',fontsize = 15)
plt.savefig('graph.png')
plt.show()


# In[ ]:





# ### Examples

# In[78]:


sns.histplot(df_wines, x="total sulfur dioxide", hue="type", element="step")


# In[80]:


sns.relplot(x="total sulfur dioxide", y="quality", hue="type",
            dashes=False, markers=True, kind="line", data=df_wines);


# In[81]:


sns.relplot(x="free sulfur dioxide", y="quality", hue="type",
            dashes=False, markers=True, kind="line", data=df_wines);


# In[ ]:




