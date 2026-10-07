import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# Exercise 1 - Conditions
# =========================================================

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [22, 35, 19, 40],
    'city': ['Paris', 'London', 'Berlin', 'Paris']
})

# 1. Age greater than 30
print(df[df['age'] > 30])

# 2. City is Paris or London
print(df[df['city'].isin(['Paris', 'London'])])

# 3. Age between 20 and 25
print(df[df['age'].between(20, 25)])


# =========================================================
# Exercise 2 - Apply on Column
# =========================================================

df = pd.DataFrame({
    'salary': [2500, 4000, 6000, 7500]
})

# 10% tax
df['salary_tax'] = df['salary'] * 0.10

# Annual salary
df['annual_salary'] = df['salary'] * 12

print(df)


# =========================================================
# Exercise 3 - Apply on Rows
# =========================================================

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'math': [80, 55, 90],
    'english': [70, 65, 85],
    'science': [60, 75, 95]
})

# Calculate total score for every student
df['total_score'] = df.apply(
    lambda row: row['math'] + row['english'] + row['science'],
    axis=1
)

# Pass if average is above 60
df['result'] = df.apply(
    lambda row: 'Pass'
    if (row['math'] + row['english'] + row['science']) / 3 > 60
    else 'Fail',
    axis=1
)

print(df)


# =========================================================
# Exercise 4 - loc / iloc
# =========================================================

df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30]
})

# Add Charlie
df.loc[2] = ['Charlie', 28]

# Replace Bob
df.iloc[1] = ['Bobby', 32]

print(df)


# =========================================================
# Exercise 5 - at / iat
# =========================================================

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [22, 35, 28]
})

# Change Alice to Alicia
df.at[0, 'name'] = 'Alicia'

# Change Bob's age
df.iat[1, 1] = 36

print(df)


# =========================================================
# Exercise 6 - Concatenation
# =========================================================

df1 = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

df2 = pd.DataFrame({
    'A': [7, 8, 9],
    'B': [10, 11, 12]
})

# Concatenate by rows
result_rows = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(result_rows)

# Concatenate by columns
result_columns = pd.concat(
    [df1, df2],
    axis=1
)

print(result_columns)


# =========================================================
# Exercise 7 - More Conditions
# =========================================================

df = pd.DataFrame({
    'name': ['Book', 'Pen', 'Laptop', 'Phone'],
    'price': [50, 10, 120, 80],
    'quantity': [5, 2, 10, 7]
})

# Price greater than 100
print(df[df['price'] > 100])

# Quantity is 5 or 10
print(df[df['quantity'].isin([5, 10])])

# Price between 50 and 80
print(df[df['price'].between(50, 80)])


# =========================================================
# Exercise 8 - Drop Row / Column
# =========================================================

df = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'department': ['HR', 'IT', 'Finance']
})

# Drop first row
df_without_first_row = df.drop(index=0)
print(df_without_first_row)

# Drop department column
df_without_department = df.drop(columns=['department'])
print(df_without_department)