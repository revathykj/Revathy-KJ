#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
# Read the Excel file
df = pd.read_excel(r"C:\Users\Revathy\Desktop\Data 3_Assignment.xlsx")

# 1. Find out how many males and females participated in the test.
gender_count = df['gender'].value_counts()
print(gender_count)

# 2. What do you think about the students' parental level of education?
parental_education_count = df['parental level of education'].value_counts()
print(parental_education_count)

# 3. Who scores the most on average for math, reading and writing based on Gender and Test preparation course
average_scores_gender = df.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
print(average_scores_gender)

average_scores_prep_course = df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean()
print(average_scores_prep_course)

# 4. What do you think about the scoring variation for math, reading and writing based on Gender and Test preparation course
std_scores_gender = df.groupby('gender')[['math score', 'reading score', 'writing score']].std()
print(std_scores_gender)

std_scores_prep_course = df.groupby('test preparation course')[['math score', 'reading score', 'writing score']].std()
print(std_scores_prep_course)

# 5. The management needs your help to give bonus points to the top 25% of students based on their math score
top_25_percentile = df[df['math score'] > df['math score'].quantile(0.75)]
print(top_25_percentile)


# In[ ]:




