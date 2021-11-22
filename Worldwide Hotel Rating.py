#!/usr/bin/env python
# coding: utf-8

# # Worldwide Hotel Rating

# ## Introduction

# This dataset is about Worldwide hotels, We will perform Exploratory Data Analysis EDA to get insight from the data.

# ### Our goal is to answer the following questions:

# - Which are the most expensive countries to book a hotel in? 

# - Which are the cheapest countries to book a hotel in?

# - What are the Top Rated Hotels?

# In[1]:



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg'")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Importing Data

df = pd.read_csv('TripAdvisor.csv')
df


# ## Data Structure

# In[3]:


df.head()


# ## Data Cleaning

# In[4]:


#Clean The symbols on the country_name and city_name columns 

spec_chars=["�"]

for char in spec_chars:
    df['country_name']=df['country_name'].str.replace(char,' ')
    df['city_name']=df['city_name'].str.replace(char,' ')
df


# In[5]:


#Rename the colnmns 

df.rename(columns={
'continent_name': 'Continent_name', 
'city_name': 'City_name',
'country_name': 'Country_name',
'reviews count': 'Reviews count',
'info.1': 'Wifi', 
'info.2': 'Hotel_facilities',
'info.3': 'Offers',
'info.4': 'Hotel_website',
'info.5': 'Free_cancellation', 
'info.6': 'Reservation',
'info.7': 'Pay'
}, inplace=True)
df


# In[6]:


df.info()


# In[7]:


df.dtypes 


# In[8]:


#Checking for Null values by showing the total null values for each column

df.isnull().sum()


# In[9]:


df.count()


# In[10]:


df.fillna(0)


# In[11]:


#We see that the price is an important feature to our analysis, so we will drop the NaN value to achive a perfect result

df.dropna(subset = ['Price'])


# ## Data Analysis

# In[12]:



continent_reviews = df.groupby('Continent_name').agg({'Reviews count': 'sum'})
C = ['#d1d0cb', '#adaaaa', '#ff8282', '#8a8484']
plt.pie(continent_reviews['Reviews count'], labels = continent_reviews.index, startangle = 20, colors = C, autopct='%1.1f%%')
plt.title('Reviews count for each continent', fontsize = 15);
my_circle = plt.Circle( (0,0), 0.7, color='white')
p=plt.gcf()
p.gca().add_artist(my_circle)

plt.show()


# ### Which are the most expensive countries to book a hotel in? And which are the cheapest ones?

# In[13]:




high = df.groupby('Country_name').agg({'Price': 'mean',
                                            'Reviews count': 'sum',
                                            'Rating': 'mean'}).sort_values(by = 'Price', ascending = False).head(10)

sns.barplot( y = high.index, x = 'Price', data = high, orient = 'h', 
            palette = 'Blues', edgecolor='black')


plt.title('Top 10 Countries With The Most Expensive Hotels', fontsize = 14)

plt.savefig("Expensive.png", dpi=250);


# The country with the most expensive hotels is Seychelles, with an average price of 330.55$ 
# per night.
# 

# In[14]:


low = df.groupby('Country_name').agg({'Price': 'mean',
                                           'Reviews count': 'sum',
                                           'Rating': 'mean'}).sort_values(by = 'Price', ascending = True).head(10)



sns.barplot( y = low.index, x = 'Price', data = low, orient = 'h', 
            palette = 'Blues', edgecolor='black')

plt.title('Top 10 Countries With The Cheapest Hotels', fontsize = 14)

plt.savefig("Cheapest.png", dpi=250);


# The country with the cheapest hotels is Crimea, with an average price of 25.5$ per night.

# In[15]:



#Top rated Hotels by Continent 

sns.catplot(y="Rating", hue="Continent_name", kind="count",
            palette="pastel", edgecolor=".6",
            data=df)

plt.title('World wide Hotel Rating by Continent', fontsize = 13)
plt.savefig("Rating.png", dpi=250);


# We can see that Europa has the highest Rating on Hotels, Also has the highest number of hotels. After that we see Asia
# comes behind Europa in Rating and number of hotels. In the end we see Africa and South Pacific almost in the same range. 
#  

# ### Top 5 hotels in Europe

# In[16]:




top_R = df[(df['Rating'] == 5) & (df['Continent_name'] == 'Europe')] 

top_H = top_R.sort_values(by = 'Reviews count', ascending = False)

top_H[['Hotel name', 'Price', 'Country_name']].head(5)


# In[17]:


#Hotel prices by continent

df= df.groupby('Continent_name').agg ({'Price': 'mean'})
    

sns.barplot(x = df.index, y = 'Price', edgecolor='black',data = df, 
            palette = "Accent")

sns.despine(left=True, bottom=False, right=True, top=True)

plt.title('Hotel prices by continent', fontsize = 15)
plt.xlabel('')
plt.ylabel('Price')

plt.savefig("Price.png", dpi=250);


# We can see that Africa has the highest average price per night for Hotels. Where Europa which have highest Rating on Hotels,
# it comes with a little bit cheaper price per nigh same as South Pacific.
# 
# This shows that there is no positive coorelation between how rich a continent is, and the Hotel prices.

# ## Conclusion

# ##### After doing EDA on this Dataset, We become more familiar with how to plan our trip in Perfect way !

# ##### Europe has received the highest number of international visitors by 745  million visitors much larger than all other continents.

# ##### It seems that Europe is the favorite destination for tourists possibly due to quality services, safety and reasonable prices.
