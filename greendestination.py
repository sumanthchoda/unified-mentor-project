# -*- coding: utf-8 -*-
"""GreenDestination.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cUhtvO606dOzxxu_aqU5ft1F03M31sqP

**Green Destination Analytics of Unified Mentor**

Load the Data
"""

import pandas as pd

df = pd.read_csv('/content/greendestination.csv')

print(df.head())

df.shape

df.columns

df.info()

print(df.describe())

"""**Observations**

There are total of 1470 rows and 35 columns in the data. Each row contains the data of the employee working in the company along with his history and work related information.

We have the information regarding their age, years at the company and the salary of each individual along with the attrition, these helps us to find the attrition rate and also to check in the trends regarding attrition.

***Attrition Rate***
"""

a=df['Attrition'].value_counts()
print(a)

"""We can observe that only 237 people have given YES to attrition and majority of the people gave NO that is 1233 people given NO to attrition."""

attrition_rate = (df['Attrition'].value_counts()['Yes'] / len(df)) * 100
print(f"Attrition Rate: {attrition_rate:.2f}%")

"""From the above cell we foud that the attrition rate of the people who left the company is around **16.12%**"""

import matplotlib.pyplot as plt
import seaborn as sns

# Visualizing age, years at the company, and income against attrition
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
sns.scatterplot(x='Age', y='YearsAtCompany', hue='Attrition', data=df, color='blue')
plt.title('Age vs Years at Company')


plt.subplot(1, 2, 2)
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df, color='cyan')
plt.title('Income vs Attrition')

plt.show()

plt.figure(figsize=(10,5))
sns.scatterplot(data=df,x='Age',y='MonthlyIncome',color='blue',edgecolor='linen',alpha=1)
plt.title("Income vs Age")
plt.xlabel("Age")
plt.ylabel("MontlyIncome")
plt.show()

c=df['Age'].value_counts()
print(c)

m=df['MonthlyIncome'].sum()
m/len(df)

"""The Average Montly Income of the Employees working in the company is 65203 appx.."""

plt.figure(figsize=(10,5))
plt.bar(c.index,c.values,color='skyblue',edgecolor='blue')
plt.title('Count of Ages')
plt.xticks(range(18, max(c.index)+1,2))
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

"""So, we can observe that the comapny is having more number of employees under age 35. We can also observe that the people between the age 25 to 35 are working more in the company.

**Final Observations**

1. We observe that there are total of 1470 rows of data in the given file, this means that there are 1470 Employees working in the commpany.
2. The Attrition rate is about 16.2% as of now.
3. Total of 237 people are leaving the company, as they gave YES for attrition and the age group of 26-32 are more likely to leave.
4. We can observe that the average monthly income of the employees is 6503.
"""