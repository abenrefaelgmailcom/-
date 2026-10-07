import pandas as pd
import numpy as np


# =========================================================
# Exercise 1 - Sorting
# =========================================================

orders_df = pd.DataFrame({
    'Order ID': [101, 102, 103, 104, 105],
    'Customer': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Amount': [250, 450, 300, 150, 500],
    'Payment Method': ['Card', 'Cash', 'Card', 'Cash', 'Card']
})

orders_df = orders_df.set_index("Order ID")

# 1. Sort Amount ascending
print("\n--- Exercise 1.1 ---")
print(
    orders_df.sort_values(
        by='Amount',
        ascending=True
    )
)

# 2. Sort Payment Method and Amount descending
print("\n--- Exercise 1.2 ---")
print(
    orders_df.sort_values(
        by=['Payment Method', 'Amount'],
        ascending=[False, False]
    )
)


# =========================================================
# Exercise 2 - Value Counts
# =========================================================

students_df = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie', 'David',
                'Eva', 'Frank', 'Grace', 'Helen'],
    'Gender': ['Female', 'Male', 'Male', 'Male',
               'Female', 'Male', 'Female', 'Female'],
    'Club': ['Science', 'Drama', 'Science', 'Sports',
             'Drama', 'Science', 'Sports', 'Drama'],
    'Scholarship': ['Yes', 'No', 'Yes', 'No',
                    'Yes', 'Yes', 'No', 'Yes']
})

# 1. Count students by Gender
print("\n--- Exercise 2.1 ---")
print(students_df['Gender'].value_counts())

# 2. Scholarship students grouped by Club and Gender
print("\n--- Exercise 2.2 ---")
print(
    students_df[
        students_df['Scholarship'] == 'Yes'
    ][['Club', 'Gender']].value_counts()
)


# =========================================================
# Exercise 3 - GroupBy
# =========================================================

employees_df = pd.DataFrame([
    {'EmpID': 1, 'Name': 'Alice', 'Department': 'HR',
     'Gender': 'Female', 'Sales': 1200, 'Bonus': 150},

    {'EmpID': 2, 'Name': 'Bob', 'Department': 'Finance',
     'Gender': 'Male', 'Sales': 1800, 'Bonus': 200},

    {'EmpID': 3, 'Name': 'Charlie', 'Department': 'Finance',
     'Gender': 'Male', 'Sales': 1700, 'Bonus': 180},

    {'EmpID': 4, 'Name': 'Diana', 'Department': 'HR',
     'Gender': 'Female', 'Sales': 1600, 'Bonus': 175},

    {'EmpID': 5, 'Name': 'Evan', 'Department': 'IT',
     'Gender': 'Male', 'Sales': 2200, 'Bonus': 250},

    {'EmpID': 6, 'Name': 'Fiona', 'Department': 'IT',
     'Gender': 'Female', 'Sales': 2100, 'Bonus': 240},

    {'EmpID': 7, 'Name': 'George', 'Department': 'Finance',
     'Gender': 'Male', 'Sales': 1950, 'Bonus': 210},

    {'EmpID': 8, 'Name': 'Hannah', 'Department': 'HR',
     'Gender': 'Female', 'Sales': 1550, 'Bonus': 160},

    {'EmpID': 9, 'Name': 'Ian', 'Department': 'IT',
     'Gender': 'Male', 'Sales': 2300, 'Bonus': 270},

    {'EmpID': 10, 'Name': 'Julia', 'Department': 'Finance',
     'Gender': 'Female', 'Sales': 1850, 'Bonus': 220},
])

employees_df = employees_df.set_index('EmpID')

# 1. Count employees by Gender
print("\n--- Exercise 3.1 ---")
print(
    employees_df.groupby('Gender').size()
)

# 2. Mean numeric columns by Gender
print("\n--- Exercise 3.2 ---")
print(
    employees_df
    .groupby('Gender')
    .mean(numeric_only=True)
)

# 3. Mean numeric columns by Department
print("\n--- Exercise 3.3 ---")
print(
    employees_df
    .groupby('Department')
    .mean(numeric_only=True)
)

# 4. Bonus max, min and std by Department and Gender
print("\n--- Exercise 3.4 ---")
print(
    employees_df
    .groupby(['Department', 'Gender'])['Bonus']
    .agg(['max', 'min', 'std'])
)

# 5. Unique Departments
print("\n--- Exercise 3.5 ---")
print(
    list(employees_df['Department'].unique())
)


# =========================================================
# Exercise 4 - Duplicates
# =========================================================

movies_df = pd.DataFrame([
    {'movie_id': 1, 'title': 'Inception', 'rating': 9.0},
    {'movie_id': 2, 'title': 'Titanic', 'rating': 8.7},
    {'movie_id': 2, 'title': 'Titanic', 'rating': 8.7},
    {'movie_id': 3, 'title': 'Interstellar', 'rating': 8.9},
    {'movie_id': 4, 'title': 'Avatar', 'rating': 8.1},
    {'movie_id': 4, 'title': 'Avatar', 'rating': 8.1},
    {'movie_id': 4, 'title': 'Avatar', 'rating': 8.3},
    {'movie_id': 5, 'title': 'The Dark Knight', 'rating': 9.2}
])

# 1. Fully duplicated rows
print("\n--- Exercise 4.1 ---")
print(
    movies_df[movies_df.duplicated()]
)

# 2. Duplicates by movie_id
print("\n--- Exercise 4.2 ---")
print(
    movies_df[
        movies_df.duplicated(subset=['movie_id'])
    ]
)


# =========================================================
# Exercise 5 - Drop Duplicates
# =========================================================

print("\n--- Exercise 5 ---")

print(
    movies_df.drop_duplicates(
        subset=['movie_id'],
        keep='first'
    )
)


# =========================================================
# Exercise 6 - Missing Values
# =========================================================

products_df = pd.DataFrame({
    "product": ["Laptop", np.nan, "Phone", "Tablet", "Camera"],
    "brand": ["Dell", "Apple", "Samsung", np.nan, "Canon"],
    "price": [1200, 1500, np.nan, 300, 700],
    "stock": [10, np.nan, 25, 15, 8],
    "rating": [4.5, 4.8, np.nan, 4.2, 4.6]
})

# 1. Display missing cells
print("\n--- Exercise 6.1 ---")
print(products_df.isna())

# 2. Count NaN values per row
print("\n--- Exercise 6.2 ---")

products_df['number_of_missing'] = (
    products_df.isna().sum(axis=1)
)

print(products_df)

# 3. Missing values in price
print("\n--- Exercise 6.3 ---")

print(
    products_df['price'].isna().sum()
)


# =========================================================
# Exercise 7 - Missing Value Condition
# =========================================================

training_df = pd.DataFrame({
    "first_name": ["Alice", np.nan, "Bob", "Diana", "Evan"],
    "last_name": ["Smith", np.nan, "Brown", "Lopez", "Kim"],
    "age": [28, np.nan, 35, 40, 30],
    "department": ["HR", "IT", "Finance", "IT", "HR"],
    "pre_training_score": [7, np.nan, np.nan, 6, 8],
    "post_training_score": [9, np.nan, np.nan, 7, 9]
})

print("\n--- Exercise 7 ---")

result = training_df[
    (training_df['pre_training_score'].isna())
    &
    (training_df['first_name'].notna())
]

print(result)


# =========================================================
# Exercise 8 - Drop NaN
# =========================================================

drop_df = pd.DataFrame({
    "product": ["Laptop", "Phone", "Tablet", "Camera", "Monitor"],
    "brand": ["Dell", np.nan, "Apple", "Canon", np.nan],
    "price": [1200, 800, np.nan, 500, 300],
    "stock": [10, 25, 15, np.nan, np.nan],
    "rating": [4.5, np.nan, 4.8, 4.3, np.nan]
})

drop_df["number_of_missing"] = (
    drop_df.isna().sum(axis=1)
)

# 1. Drop rows with at least one NaN
print("\n--- Exercise 8.1 ---")
print(
    drop_df.dropna()
)

# 2. Drop only rows where all values are NaN
print("\n--- Exercise 8.2 ---")
print(
    drop_df.dropna(how='all')
)

# 3. Keep rows with at least 2 non-null values
print("\n--- Exercise 8.3 ---")
print(
    drop_df.dropna(thresh=2)
)