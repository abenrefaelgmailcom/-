import pandas as pd
import numpy as np


# =========================================================
# Setup
# =========================================================

books = pd.DataFrame({
    "title": ["1984", "Dune", "Dune", "Hamlet", "Hamlet", "Hamlet", "Emma"],
    "author": ["Orwell", "Herbert", "Herbert",
               "Shakespeare", "Shakespeare", "Shakespeare", "Austen"],
    "year": [1949, 1965, 1965, 1603, 1603, 1609, 1815]
})

students = pd.DataFrame({
    "first_name": ["Liam", np.nan, "Noah", "Emma", "Olivia"],
    "last_name": ["Smith", np.nan, "Johnson", "Brown", "Wilson"],
    "age": [20, np.nan, 22, 19, 21],
    "major": ["Math", np.nan, "CS", "History", "Biology"],
    "gpa": [3.5, np.nan, np.nan, 3.7, 3.9],
    "credits": [30, np.nan, np.nan, 25, 40]
})

customers = pd.DataFrame({
    "cust_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Clara", "David"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "cust_id": [1, 2, 2, 5],
    "amount": [250, 400, 150, 500]
})


# =========================================================
# 1. Duplicates
# =========================================================

# Q1.1 - Find duplicate rows
print("\nQ1.1 - Duplicate rows:")
print(books[books.duplicated()])


# Q1.2 - Show non-duplicated rows
print("\nQ1.2 - Non-duplicated rows:")
print(books[~books.duplicated()])


# Q1.3 - Keep last occurrence of each title
print("\nQ1.3 - Keep last occurrence of each title:")
print(
    books.drop_duplicates(
        subset='title',
        keep='last'
    )
)


# Q1.4 - Count duplicates in author
print("\nQ1.4 - Number of duplicate authors:")
print(books['author'].duplicated().sum())


# =========================================================
# 2. Missing Data
# =========================================================

# Q2.1 - Count missing values per column
print("\nQ2.1 - Missing values per column:")
print(students.isna().sum())


# Q2.2 - Missing values per row
print("\nQ2.2 - Missing count per row:")

students['missing_count'] = students.isna().sum(axis=1)

print(students)


# Q2.3 - GPA is NaN but first_name exists
print("\nQ2.3 - Missing GPA with existing first name:")

result = students[
    students['gpa'].isna()
    &
    students['first_name'].notna()
]

print(result)


# Q2.4 - Column with most missing values
print("\nQ2.4 - Column with most missing values:")

missing = students.isna().sum()

print("Column:", missing.idxmax())
print("Missing values:", missing.max())


# =========================================================
# 3. Filling NaN
# =========================================================

# Use a copy so the original students DataFrame stays unchanged
students_filled = students.copy()


# Q3.1 - Fill age with mean
students_filled['age'] = students_filled['age'].fillna(
    students_filled['age'].mean()
)


# Q3.2 - Fill GPA with minimum
students_filled['gpa'] = students_filled['gpa'].fillna(
    students_filled['gpa'].min()
)


# Q3.3 - Fill credits with maximum
students_filled['credits'] = students_filled['credits'].fillna(
    students_filled['credits'].max()
)


print("\nQ3 - Students after filling values:")
print(students_filled)


# Q3.4
print("\nQ3.4:")
print("Mean is generally the most reasonable basic strategy here for age.")


# =========================================================
# 4. Dropping NaN
# =========================================================

# Q4.1 - Drop rows containing any NaN
print("\nQ4.1 - Drop rows with any NaN:")
print(students.dropna())


# Q4.2 - Drop rows only if all values are NaN
print("\nQ4.2 - Drop rows where all values are NaN:")
print(students.dropna(how='all'))


# Q4.3 - Keep rows with at least 3 non-missing values
print("\nQ4.3 - At least 3 non-missing values:")
print(students.dropna(thresh=3))


# Q4.4 - Drop columns with more than 50% missing values
print("\nQ4.4 - Remove columns with more than 50% missing:")

result = students.loc[
    :,
    students.isna().mean() <= 0.5
]

print(result)


# =========================================================
# 5. Merging Tables
# =========================================================

# Q5.1 - Inner Join
print("\nQ5.1 - INNER JOIN:")

inner_join = pd.merge(
    customers,
    orders,
    on='cust_id',
    how='inner'
)

print(inner_join)


# Q5.2 - Left Join
print("\nQ5.2 - LEFT JOIN:")

left_join = pd.merge(
    customers,
    orders,
    on='cust_id',
    how='left'
)

print(left_join)


# Q5.3 - Right Join
print("\nQ5.3 - RIGHT JOIN:")

right_join = pd.merge(
    customers,
    orders,
    on='cust_id',
    how='right'
)

print(right_join)


# Q5.4 - Outer Join with indicator
print("\nQ5.4 - OUTER JOIN:")

outer_join = pd.merge(
    customers,
    orders,
    on='cust_id',
    how='outer',
    indicator=True
)

print(outer_join)


# Q5.5 - Cross Join
print("\nQ5.5 - CROSS JOIN:")

colors = pd.DataFrame({
    'color': ['Red', 'Blue']
})

sizes = pd.DataFrame({
    'size': ['S', 'M', 'L']
})

cross_join = pd.merge(
    colors,
    sizes,
    how='cross'
)

print(cross_join)