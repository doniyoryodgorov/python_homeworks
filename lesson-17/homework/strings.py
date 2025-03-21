Homework 1
import pandas as pd

# Step 1: Create the DataFrame
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Step 2: Rename column names using function
df = df.rename(columns={'First Name': 'first_name', 'Age': 'age'})

# Step 3: Print the first 3 rows of the DataFrame
print("First 3 Rows of the DataFrame:")
print(df.head(3))

# Step 4: Find the mean age of the individuals
mean_age = df['age'].mean()
print("\nMean Age of Individuals:", mean_age)

# Step 5: Select and print only the 'first_name' and 'City' columns
print("\nSelected Columns (first_name and City):")
print(df[['first_name', 'City']])

#Step 6 
import numpy as np

np.random.seed(42)  # For reproducibility
df['Salary'] = np.random.randint(50000, 100000, size=len(df))

#Step 7

print(df.describe())

Homework 2:
#1
Month=['Jan','Feb','Mar','Apr']
Sales=[5000,6000,7500,8000]
Expenses=[3000,3500,4000,4500]

sales_expenses=pd.DataFrame({'Month':Month,'Sales':Sales,'Expenses':Expenses})
sales_expenses
#2
#Calculate and display the maximum sales and expenses.
max_sales=sales_expenses['Sales'].max()
max_expenses=sales_expenses['Expenses'].max()
print(max_sales)
print(max_expenses)

#3
#Calculate and display the minimum sales and expenses.
min_sales=sales_expenses['Sales'].min()
min_expenses=sales_expenses['Expenses'].min()
print(min_sales)
print(min_expenses)
#4
#Calculate and display the average sales and expenses.
average_sales=sales_expenses['Sales'].mean()
average_expenses=sales_expenses['Expenses'].mean()
print(average_sales)
print(average_expenses)

Homework 3:

#1
import pandas as pd

Category=['Rent','Utilities','Groceries','Entertainment']
January=[1200,200,300,150]
February=[1300,220,320,160]
March=[1400,240,330,170]
April=[1500,250,350,180]

Expenses=pd.DataFrame({'Category':Category,'January':January,'February':February,'March':March,'April':April})
Expenses

expenses = Expenses.set_index('Category')

#2 Calculate and display the maximum expense for each category.
max_expenses=Expenses[['January','February','March','April']].max(axis=1)
Expenses['Max Expenses']=max_expenses    
print(max_expenses)

#3 calculate and display the minimum expense for each category.
min_expenses=Expenses[['January','February','March','April']].min(axis=1)
Expenses['Min Expenses']=min_expenses
print(min_expenses)   

#4 Calculate and display the average expense for each category.
average_expenses=Expenses[['January','February','March','April']].mean(axis=1)
Expenses['Average Expenses']=average_expenses
print(average_expenses)   





