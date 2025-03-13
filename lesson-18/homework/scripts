
#HOMEWORK 2

import pandas as pd
df = pd.read_csv('tackoverflow_qa.csv')
df.head()

#Find all questions that were created before 2014
df[df['creationdate'] < '2014-01-01']

#Find all questions with a score more than 50
df[df['score']>50]

#Find all questions with a score between 50 and 100
df[(df['score']>=50) & (df['score']<100)]

#Find all questions answered by Scott Boston
df[df['ans_name']=='Scott Boston']

#Find all questions answered by the following 5 users
df[df['ans_name'].isin(['Scott Boston', 'Jon Clements', 'unutbu', 'BrenBarn', 'DSM'])]

#Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
filtered_df = df[df['creationdate'].between('2014-03-01', '2014-10-01')]

#Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
df[(df['score'].between(5,10)) | (df['viewcount']>10000)]

#Find all questions that are not answered by Scott Boston
df[df['ans_name']!='Scott Boston']

#HOMEWORK 3

import pandas as pd
df = pd.read_csv('titanic.csv')
df.head()

#Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30
# Agar ustun nomlari aynan shunday bo‘lsa:
filtered_df = df[
    (df['Sex'] == 'female') & 
    (df['Pclass'] == 1) & 
    (df['Age'].between(20, 30))
]

#Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.
filtered_df=df[df['Fare']>100]

#Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
filtered_df = df[
    (df['Survived'] == 1) & 
    (df['SibSp'] == 0) & 
    (df['Parch'] == 0)
]

#Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
filtered_df=df[df['Embarked']=='C' & df['Fare']>50]

#Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.
filtered_df=df[(df['SibSp'] > 0) & (df['Parch']>0)]

#Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.
filtered_df = df[(df['Age'] <= 15) & (df['Survived'] == 0)]

#Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.
filtered_df = df[(df['Cabin'].notnull()) & (df['Fare'] > 200)]

#Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.
filtered_df = df[df['PassengerId'] % 2 != 0]

#Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.
filtered_df = df.drop_duplicates(subset='Ticket', keep=False)

#Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.
filtered_df
df[(df['Name'].str.contains('Miss')) & (df['Pclass'] == 1)]
