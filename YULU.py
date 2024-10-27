#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from scipy.stats import ttest_ind,norm,f_oneway,chi2_contingency,shapiro,levene
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("yulu")
df


# # OBSERVATIONS

# In[3]:


df.shape


# In[4]:


df.info()


# From the above data set we can see that there is no missing values present in the data

# In[5]:


df.describe(include="all")


# # Checking Outliers

# In[6]:


plt.figure(figsize=(5,5))
sns.boxplot(y=df["count"],x=df["workingday"])
plt.title("Workingday_wise_count")
plt.show()


# In[7]:


plt.figure(figsize=(5,5))
sns.boxplot(y=df["count"],x=df["season"])
plt.title("season_wise_count")
plt.show()


# In[8]:


plt.figure(figsize=(5,5))
sns.boxplot(y=df["count"],x=df["holiday"])
plt.title("Holiday_wise_count")
plt.show()


# In[9]:


plt.figure(figsize=(5,5))
sns.boxplot(y=df["count"],x=df["weather"])
plt.title("Weather_wise_count")
plt.show()


# In[ ]:





# # BIVARIATE ANALYSIS

# In[ ]:





# # ttest to check "Working Day has effect on number of electric cycles rented"

H0:Mean of working day and mean of non working day  are equal.
Ha:Mean of working day and mean of non working day  are  not same.
alpha value=0.5
# In[10]:


alpha_value=0.5


# In[11]:


df_notworkingday=df[df["workingday"]==0]["count"]
df_notworkingday


# In[12]:


df_workingday=df[df["workingday"]==1]["count"]
df_workingday


# In[13]:


tstatistic,P_value=ttest_ind(df_notworkingday,df_workingday)


# In[14]:


P_value


# In[ ]:





# In[15]:


if P_value < alpha_value:
    print("reject the null hypothesis")
else:
    print("Don't reject the null hypothesis")

Hence no of casual users and registered user are more compare to non working day
# Visual Analysis "Working Day has effect on number of electric cycles rented"

# In[16]:


df_notworkingday.mean()


# In[17]:


df_workingday.mean()

df_notworkingday.mean() < df_workingday.mean()
# Normality test for working and non working day 
H0:working and non working day will come under normality 
Ha:working and non working will not come under normality
# In[21]:


statistic_value,p_value=shapiro(df_workingday)


# In[22]:


p_value


# In[23]:


statistic_value,p_value=shapiro(df_notworkingday)


# In[24]:


p_value


# In[25]:


if p_value < alpha_value:
    print("working and non working will not come under normality")
else:
    print("working and non working day will come under normality ")


# In[26]:


sns.histplot(df_workingday)
plt.title("Count_of_workingday")
plt.show()


# In[27]:


sns.histplot(df_notworkingday)
plt.title("Count_of_notworkingday")
plt.show()


# Variance Test for Working and non working day 
H0:Both Working and non working variance are equal
Ha:Both Working and non working variance not are equal
# In[29]:


statistic_value,p_value=levene(df_workingday,df_notworkingday)


# In[30]:


p_value


# In[31]:


if P_value < alpha_value:
    print('Both Working and non working variance not are equal')
else:
    print("Both Working and non working variance are equal")


# In[ ]:





# In[ ]:





# # No. of cycles rented similar or different in different seasons

# In[ ]:




H0:the null hypothesis is that there is no difference among group means(mu1=mu2=mu3=mu=4)
Ha:The alternative hypothesis is that at least one group differs significantly from the overall mean of the dependent variable
    
# In[32]:


season1=df[df["season"]==1]["count"]
season2=df[df["season"]==2]["count"]
season3=df[df["season"]==3]['count']
season4=df[df["season"]==4]["count"]


# In[33]:


fstatistic,p_value=f_oneway(season1,season2,season3,season4)


# In[34]:


p_value


# In[ ]:





# In[35]:


if p_value > alpha_value:
    print("the null hypothesis is that there is no difference among group means")
else:
    print("The alternative hypothesis is that at least one group differs significantly from the overall mean of the dependent variable")


# Visual Analysis " No. of cycles rented similar or different in different seasons"

# season1.mean()

# In[36]:


season2.mean()


# In[37]:


season3.mean()


# In[38]:


season4.mean()


# In[39]:


season1.mean()

From the above means we can conclude that  at least one group differs significantly from the overall mean of the dependent variable
# Normality test for working and non working day
H0:season1,season2,season3,season4 will are normally distributed
Ha:season1,season2,season3,season4 will are not normally distributed
# In[40]:


shapiro(season1)


# In[41]:


shapiro(season2)


# In[42]:


shapiro(season3)


# In[43]:


shapiro(season4)

P_values are less than 0.5(alpha_value)
So we are rejecting the null hypothesis
# In[ ]:





# Graphical analysis for "season vs count"

# In[ ]:





# In[44]:


sns.histplot(x=season1)
plt.title("season1")
plt.show()


# In[45]:


sns.histplot(x=season2)
plt.title("season2")
plt.show()


# In[46]:


sns.histplot(x=season3)
plt.title("season3")
plt.show()


# In[47]:


sns.histplot(x=season4)
plt.title("season4")
plt.show()


# Variance Test for "season vs count"
H0:season1,season2,season3,season4 are having equal variance.
Ha:season1,season2,season3,season4 are not having equal variance.
# In[48]:


statistic_value,p_value=levene(season1,season2,season3,season4)


# In[49]:


p_value


# In[50]:


if p_value < alpha_value:
    print("reject null hypothesis")
else:
    print("we don't reject null hypothesis")


# In[ ]:





# In[ ]:





# In[ ]:





# # "No. of cycles rented similar or different in different weather"
H0:No of cycles is similar in different weather or mu1=mu2=mu3
Ha:No of cycles is different in different weather 
# In[ ]:





# In[59]:


df_weather1=df[df["weather"]==1]["count"]


# In[60]:


df_weather2=df[df["weather"]==2]["count"]


# In[61]:


df_weather3=df[df["weather"]==3]["count"]


# In[62]:


df_weather4=df[df["weather"]==4]["count"]


# In[63]:


statistic,P_value=f_oneway(df_weather1,df_weather2,df_weather3,df_weather4)


# In[ ]:





# In[64]:


P_value


# In[65]:


if P_value < alpha_value:
    print("Reject null hypothesis and We conclude that No of cycles is different in different weather ")
else:
    print("we don't reject the null hypothesis and we conclude that No of cycles is similar in different weather ")


# Visual analysis for "No. of cycles rented similar or different in different weather"

# In[66]:


df_weather1.mean()


# In[67]:


df_weather2.mean()


# In[68]:


df_weather3.mean()


# In[69]:


df_weather4.mean()

From the above analysis we conclude that "No of cycles rented similar or different in different weather"
# In[ ]:





# Normality Test for Weather vs count
H0:df_weather1,df_weather2,df_weather3,df_weather4  are  normally distributed.
Ha:df_weather1,df_weather2,df_weather3,df_weather4  are not  normally distributed.
# In[72]:


statistic_value,P_value=shapiro(df_weather1)


# In[73]:


p_value


# In[74]:


statistic_value,P_value=shapiro(df_weather2)


# In[75]:


p_value


# In[76]:


statistic_value,P_value=shapiro(df_weather3)


# In[77]:


P_value

We cannot able to find the shapiro test for df_weather4 as there is only one value so all the p_values are less than we reject null hypothesis and conclude that df_weather1,df_weather2,df_weather3,df_weather4  are not  normally distributed.
# Grahical analysis

# In[78]:


sns.histplot(x=df_weather1)
plt.title("Weather1")
plt.show()


# In[79]:


sns.histplot(x=df_weather2)
plt.title("Weather2")
plt.show()


# In[80]:


sns.histplot(x=df_weather3)
plt.title("Weather3")
plt.show()


# Variance test for Weather vs count
H0:Variance for all the weather are equal
Ha:Variance for all the weather are not equal
# In[81]:


levene(df_weather1,df_weather2,df_weather3,df_weather4)

P_value is less than alpha value so we reject null hypothesis and  we conclude that "Variance for all the weather are not equal".
# In[ ]:





# # Weather is dependent on season 
Null hypothesis (H0): Weather is not dependent on season.
Alternative hypothesis (Ha): Weather is dependent on season.
# In[82]:


df["weather"]


# In[83]:


df["season"]


# In[84]:


pd.crosstab(df["weather"],df["season"])


# In[85]:


statistic_value,P_value,Dof,exp_value=chi2_contingency(pd.crosstab(df["weather"],df["season"]))


# In[86]:


P_value


# In[87]:


if p_value < alpha_value:
    print("We reject null hypothesis and we can conclude Weather is dependent on season.")
else:
    print("Weather is not dependent on season.")


# In[88]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




