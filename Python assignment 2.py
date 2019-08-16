
# coding: utf-8

# In[1]:


#1 Import the customer data into python
import pandas as pd

df = pd.read_csv (r'C:\Users\XSVontarvi\OneDrive - NESTLE\Vineela\Customers.csv')
print (df)


# In[3]:


#2 Understand the data using different functions 
#and attributes like shape, index, columns, dtypes.ndim, info(), get_dtype_counts etc

df.index
#It shows the informations about how the index is arranged 


# In[4]:


#To display the top five rows
df.head()


# In[5]:


# To get the names of all columns in the DataFrame
df.columns


# In[7]:


# To get the names of all columns in the DataFrame in the form of list
df.columns.tolist()


# In[8]:


# To know the datatype of all columns in the DataFrame
df.dtypes


# In[9]:


# Dimention of DataFrame
df.ndim


# In[11]:


# To get the file level information about the dataset
df.info()


# In[12]:


# To know the sattistical summary of dataset
# It gives the information about total number of observation, mean, max, median, standard deviation, percentiles
# Note : it gives the result of only numerical variable columns
df.describe()


# In[14]:


# It gives the information about number of columns of which datatype
df.get_dtype_counts()


# In[15]:


# To show the number of observations are presents in particular Attributes/variables/columns
# Indirectly we can observe the missing values
df.count()


# In[16]:


# To get the number of observation and number of columns
df.shape


# In[17]:


# To display the number of rows only
df.shape[0]


# In[18]:


# To show the number of columns/ no. of attributes
df.shape[1]


# In[19]:


#3 What is percentage of missing values for customer Value variable? 


# In[20]:


# first find out the number of rows mussing in 'Customer_value'
# a= df['Customer_Value'].isnull().sum()
df['Customer_Value'].isnull().sum()


# In[21]:


# find the total length of observation
# b= df.shape[0]
df.shape[0]


# In[22]:


#divide the missing length of 'Customer_Value' by 'Total length of observation'
# a/b
df['Customer_Value'].isnull().sum()/df.shape[0]


# In[23]:


# to display in terms of percentage multiply by 100
#a/b*100
df['Customer_Value'].isnull().sum()/df.shape[0]*100


# In[25]:


round(((df['Customer_Value'].isnull().sum()/df.shape[0])*100),3)


# In[ ]:


#4 Create two subsets with unique and duplicate values.


# In[26]:


# To find the how many duplicate observation in the dataframe
df.Customer_ID.duplicated().sum()


# In[29]:


# create a subset of duplicate value
duplicate= df[df.Customer_ID.duplicated()]
duplicate.head()


# In[30]:


# to get the number of rows and columns of duplicate subset
duplicate.shape


# In[31]:


# create a subset of unique values value
unique_values= df[df.Customer_ID.duplicated()== False]
unique_values.head()


# In[32]:


# to get the number of rows and columns of unique subset
unique_values.shape


# In[ ]:


#5. Create data set with list of customers whose customer value greater than 10000


# In[33]:


df_10000=df[df['Customer_Value']> 10000]
df_10000.shape[0]


# In[34]:


# Reset the index values and drops the original index number
df_10000=df[df['Customer_Value']> 10000].reset_index(drop= True)
df_10000.head()


# In[35]:


#6. In customer table, create a new variable called “customer value segment” using customer value as follows. -¶
#High Segment - > 25000
#Medium Segment – Between 10000 and 25000
#Low Segment – less than or equal to 10000

from numpy import where as IF
#customer_value = CV
CV= df.Customer_Value
df['Customer_value_segment']=IF(CV > 25000,'High Segment',IF((CV > 10000) & (CV < 25000),'Medium Segment','Low Segment'))
df.head()


# In[36]:


#7. Create variables “average revenue per trip” and “balance points” in the customer data set
df = df.assign(average_revenue_per_trip= df.Customer_Value/df.Buy_Times,
              Balance_Points=df.Points_Earned - df.Points_Redeemed)
df.head()


# In[43]:


#8. How many days between last purchase date and today?
import datetime as dt
today = pd.to_datetime(dt.datetime.now().date())
day_difference = today - pd.to_datetime(df.Recent_Date,format= '%Y%m%d')
day_difference


# In[44]:


#9. Calculate percentage of sales by each last city, state and region.
# Select only 'last_region', 'last_state', 'last_city' and 'Customer_Value' columns
demography = df[['Last_region','Last_state','Last_city','Customer_Value']]
demography.head()


# In[45]:


demography.groupby(['Last_region'])['Customer_Value'].sum()/demography.Customer_Value.sum()


# In[46]:


demography.groupby(['Last_region', 'Last_state'])['Customer_Value'].sum()/demography.Customer_Value.sum()


# In[47]:


demography.groupby(['Last_region', 'Last_state', 'Last_city'])['Customer_Value'].sum()/demography.Customer_Value.sum()


# In[50]:


#10. What is the count of customers, 
#average number of purchases and average purchase transaction value by last state and city.
df.groupby(['Last_state', 'Last_city'])['Customer_ID'].count()


# In[51]:


df.groupby(['Last_state','Last_city'])['Buy_Times'].count()


# In[53]:


df.groupby(['Last_state', 'Last_city'])['average_revenue_per_trip'].mean()

