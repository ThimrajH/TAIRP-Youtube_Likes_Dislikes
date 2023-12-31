#!/usr/bin/env python
# coding: utf-8

# ### YouTube likes And Dislikes
#             movie ratings dataset, such as the MovieLens dataset, to gain insights into movie ratings and user preferences. Perform calculations to find average ratings for movies, identify highly-rated movies, and determine the most active users. Visualize the data using histograms, scatter plots, or heatmaps to explore relationships between ratings, genres, and user demographics.

# ### Importing the required libraries and read the provided dataset (youtube_dislike_dataset.csv) and retrieve top5 and bottom 5 records.

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df= pd.read_csv(r"C:\Users\ASUS\Downloads\youtube_dislike.csv")


# In[3]:


df.head(5)


# In[4]:


df.tail(5)


# ###  Check the info of the dataframe and write your inferences on data types and shape of the dataset.
# 

# In[5]:


df.shape


# In[6]:


df.info()


#  The comments column has some missing values beacuse there are 37422 total entries but in comments having less than required entries.
# The Dataset have total 37422 rows and 12 columns

# ###  Check for the Percentage of the missing values and drop or impute them.

# In[7]:


df.isna().sum()  ## there are 158 blank values in comments


# In[8]:


pct = df.isna().sum() / len(df)
pct/=pct.sum()


# In[9]:


pct


# In[10]:


df["comments"].unique()


# In[11]:


df.dropna(inplace=True)


# In[12]:


df.isna().sum()


# ###  Checking the statistical summary of both numerical and categorical columns and write your inferences.
# 

# In[13]:


df.describe(include='all')


# The dataset includes video data with a wide range of view counts, from a minimum of 20,368 to a maximum of 1,322,797,000. The average view count for all videos in the dataset is 5,710,821. The number of likes for the videos in the dataset ranges from a minimum of 21 to a maximum of 31,837,680, while the number of dislikes ranges from a minimum of 1 to a maximum of 3. The number of comments per video also varies widely, from a minimum of 2,397,733 to a maximum of 16,071,030. This data provides insights into the relative popularity of different kinds of videos and the variety of engagement users have with those videos.

# ### Convert datatype of column published_at from object to pandas datetime.

# In[14]:


pd.DataFrame(pd.to_datetime(df["published_at"]))


# ###  Creating a new column as 'published_month' using the column published_at (display the months only)
# 

# In[15]:


df["published_month"]=df['published_at'].str[5:7]


# In[16]:


df["published_month"].head(5)


# ###  Replacing the numbers in the column published_month as names of the months i,e., 1 as 'Jan', 2 as 'Feb' and so on.....
# 

# In[17]:


month={'01':"Jan",'02':'Feb','03':'Mar','04':'Apr','05':'May','06':'June','07':'July','08':'Aug','09':'Sep','10':'Oct','11':'Nov','12':'Dec'}


# In[18]:


df["published_month"]=df["published_month"].map(month)


# In[19]:


df['published_month'].head(5)


# ###  Finding the number of videos published each month and arrange the months in a decreasing order based on the video count.
# 

# In[20]:


df.groupby('published_month')['video_id'].count().sort_values(ascending=False)


# ### Finding the count of unique video_id, channel_id and channel_title.

# In[21]:


count_video_id= df['video_id'].nunique()
print("Count Of Unique Video_id's:",count_video_id)


# In[22]:


count_Channel_id = df['channel_id'].nunique()
print("Count Of Unique Channel_id's:",count_Channel_id)


# In[23]:


count_Channel_title = df['channel_title'].nunique()
print("Count Of Unique Channel_titles:",count_Channel_title)


# ### Top10 channel names having the highest number of videos in the dataset and the bottom10 having lowest number of videos.
# 

# In[24]:


Highest_lowest_Video= df.groupby('channel_title')['video_id'].count().sort_values(ascending=False)


# In[25]:


Highest_lowest_Video.head(10) #top10 channel names having the highest number of videos in the dataset


# In[26]:


Highest_lowest_Video.tail(10)  #buttom10 channel names having the highest number of videos in the dataset


# ### Title of the video which has the maximum number of likes and the title of the video having minimum likes and write your inferences

# In[27]:


pd.DataFrame(df.groupby('title')['likes'].max().sort_values(ascending=False).head(1))


# In[28]:


max_likes = df.loc[df['likes'].idxmax()]
max_title = max_likes['title']



# In[29]:


max_likes['likes']


# In[30]:


min_likes = df.loc[df['likes'].idxmin()]
min_title = min_likes['title']


# In[31]:


print("Video with the minimum number of likes:", min_title)


# In[32]:


min_likes['likes']


# ### Title of the video which has the maximum number of dislikes and the title of the video having minimum dislikes and write your inferences.
# 

# In[35]:


pd.DataFrame(df.groupby('title')['dislikes'].max().sort_values(ascending=False).tail(1))


# The Title of Tims For Good: A Taste of The Familiar is minimum dislikes
# it means the title is attractive and impressive to the users, so they reacted positively towards it.

# In[36]:


pd.DataFrame(df.groupby('title')['dislikes'].max().sort_values(ascending=False).head(1))


# The Cuties offiial trailer released in netflix and the trailer received a large number of dislikes and negative comments across different social media platforms.

# ### Finding the number of views have any effect on how many people disliked the videos, with a metric and a plot.

# In[39]:


df['dislike_rate'] = df['dislikes']/df['view_count']*100


# In[40]:


df['dislike_rate']


# In[44]:


import matplotlib.pyplot as plt
plt.scatter(df['dislike_rate'],df['view_count'])
plt.xlabel('dislikes')
plt.ylabel('view_count')
plt.title('number of views effected on how people disliked video')
plt.show()


# In[47]:


import seaborn as sns
sns.heatmap(df.corr(), annot=True, cmap='spring')


# ### Display all the information about the videos that were published in January, and mention the count of videos that were published in January.

# In[48]:


df.columns


# In[51]:


df[df['published_month']=='Jan']


# In[53]:


df[df['published_month']=='Jan'].count()


# In[ ]:




