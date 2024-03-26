#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from scipy.stats import ttest_ind


# In[3]:


df=pd.read_csv('website_ab_test.csv')


# In[4]:


df.head()


# In[6]:


# Dataset Summary
summary = {
    'Number of Records': df.shape[0],
    'Number of Columns': df.shape[1],
    'Missing Values': df.isnull().sum(),
    'Numberical Columns Summary': df.describe()
}
summary


# In[7]:


df.info()


# In[8]:


# grouping data by theme and calculating mean values
theme_performance = df.groupby('Theme').mean()
theme_performance


# In[9]:


# Sorting the data by conversion rate for a better comparison
theme_performance_sorted = theme_performance.sort_values(by='Conversion Rate', ascending=False)
theme_performance_sorted


# # Hypothesis Testing
# We’ll use a significance level (alpha) of 0.05 for our hypothesis testing

# ## 1. Hypothesis testing based on the Conversion Rate between the Light Theme and Dark Theme.

# ### Null Hypothesis (H0): 
# There is no difference in conversion rates between the Light theme and Dark theme
# ### Alternative Hypothesis (H1): 
# There is a difference in conversion rates between the Light theme and Dark theme

# In[10]:


# Extracting conversion rates for both themes
conversion_rate_light = df[df['Theme']=='Light Theme']['Conversion Rate']
conversion_rate_dark = df[df['Theme']=='Dark Theme']['Conversion Rate']


# In[11]:


# performing a two-sample t-test
t_stat, p_value = ttest_ind(conversion_rate_light, conversion_rate_dark, equal_var=False)
print('t-stat value:',t_stat)
print('p value:', p_value)


# ### Conclusion:
# Since p value is smuch greater than significance level, we donot have enough evidence to reject the null hypothesis.

# ## 2. Hypothesis testing based on the Click Through Rate (CTR) between the Light Theme and Dark Theme.

# ### Null Hypothesis (H0): 
# There is no difference in Click Through Rates between the Light theme and Dark theme
# ### Alternative Hypothesis (H1): 
# There is a difference in Click Through Rates between the Light theme and Dark theme

# In[13]:


# Extracting click through rate  for both themes
click_through_rate_light=df[df['Theme']=='Light Theme']['Click Through Rate']
click_through_rate_dark =df[df['Theme']=='Dark Theme']['Click Through Rate']


# In[14]:


# performing a two sample test
t_test_ctr, p_value_ctr = ttest_ind(click_through_rate_light, click_through_rate_dark, equal_var=False)
print('t-test for CTR:', t_test_ctr)
print('p value for CTR:', p_value_ctr)


# ### Conclusion:
# P value is slightly below our significance level indicating there is a statistically significant difference in CLick Through Rate between the Light theme and Dark theme, with the Dark theme likely having a higher CTR.

# ## 3. Hypothesis testing based on the Bounce Rate between the Light Theme and Dark Theme.

# ### Null Hypothesis (H0): 
# There is no difference in Bounce Rate between the Light theme and Dark theme
# ### Alternative Hypothesis (H1): 
# There is a difference in Bounce Rate between the Light theme and Dark theme

# In[15]:


# Extracting Bounce rate for both themes
bounce_rate_light = df[df['Theme']=='Light Theme']['Bounce Rate']
bounce_rate_dark = df[df['Theme']=='Dark Theme']['Bounce Rate']


# In[16]:


# performing a two sample test
t_test_bounce, p_value_bounce = ttest_ind(bounce_rate_light, bounce_rate_dark, equal_var=False)
print('t-test value for bounce rate:', t_test_bounce)
print('p value for bounce rate:', p_value_bounce)


# ### Conclusion:
# Since p value is greater than significance level, we do not have enough evidence to reject the null hypothesis.

# ## 4. Hypothesis testing based on the Scroll Depth between the Light Theme and Dark Theme.

# ### Null Hypothesis (H0): 
# There is no difference in Scroll Depth between the Light theme and Dark theme
# ### Alternative Hypothesis (H1): 
# There is a difference in Scroll Depth between the Light theme and Dark theme

# In[19]:


# Extracting Bounce rate for both themes
scroll_depth_light = df[df['Theme']=='Light Theme']['Scroll_Depth']
scroll_depth_dark = df[df['Theme']=='Dark Theme']['Scroll_Depth']


# In[21]:


# performing a two-sample t-test for scroll depth
t_test_scroll, p_value_scroll = ttest_ind(scroll_depth_light, scroll_depth_dark, equal_var=False)
print('t-test value for scroll depth:', t_test_scroll)
print('p value for scroll depth:', p_value_scroll)


# ### Conclusion:
# Since p value is greater than significance level, we do not have enough evidence to reject the null hypothesis.

# In[24]:


# Creatinga table for comparison
comparison_table= pd.DataFrame({
    'Metric': ['Click Through Rate','Conversion Rate','Bounce Rate', 'Scroll Depth'],
    'T-Statistic': [t_test_ctr,t_stat, t_test_bounce, t_test_scroll],
    'p value':[p_value_ctr, p_value, p_value_bounce, p_value_scroll]
})
comparison_table


# ### Click Through Rate:
# The test reveals a statistically significant difference, with the Dark theme likely performing better
# ### Conversion Rate:
# No statistically significant difference was found.
# ### Bounce Rate:
# No statistically significant difference found in Bounce rates.
# ### Scroll Depth:
# No statistically significant difference observed in Scroll Depth.

# ## Summary:
# While two themes perform similarly across most metrics, the Dark theme has slight edge in terms of engaging users to click through. For other key performance indicators like Conversion rate, Bounce Rate, Scroll Depth, the choice between a Light Theme and Dark Theme doesnot significantly affect user behaviour according to the data provided.

# In[ ]:




