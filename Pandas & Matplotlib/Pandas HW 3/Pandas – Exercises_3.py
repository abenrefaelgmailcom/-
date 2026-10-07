import pandas as pd


# =========================================================
# Load the DataFrame
# =========================================================

df = pd.read_csv("mpg.csv")

print("First 5 rows:")
print(df.head())


# =========================================================
# 1. Sorting
# =========================================================

# Q1.1 - Sort by mpg in ascending order
print("\nQ1.1 - MPG ascending:")

sorted_by_mpg = df.sort_values(
    by='mpg',
    ascending=True
)

print(sorted_by_mpg)


# Q1.2 - Sort by weight in descending order
print("\nQ1.2 - Weight descending:")

sorted_by_weight = df.sort_values(
    by='weight',
    ascending=False
)

print(sorted_by_weight)


# Q1.3 - Sort by model_year first, then mpg
print("\nQ1.3 - Sort by model_year and mpg:")

sorted_by_year_mpg = df.sort_values(
    by=['model_year', 'mpg']
)

print(sorted_by_year_mpg)


# =========================================================
# 2. Value Counts
# =========================================================

# Q2.1 - Count cars for each cylinders type
print("\nQ2.1 - Cylinders counts:")

cylinder_counts = df['cylinders'].value_counts()

print(cylinder_counts)


# Q2.2 - Count each origin
print("\nQ2.2 - Origin counts:")

origin_counts = df['origin'].value_counts()

print(origin_counts)


# Q2.3 - Find model year with most cars
print("\nQ2.3 - Model year with most cars:")

year_counts = df['model_year'].value_counts()

most_common_year = year_counts.idxmax()
number_of_cars = year_counts.max()

print("Model year:", most_common_year)
print("Number of cars:", number_of_cars)


# =========================================================
# 3. GroupBy & Aggregations
# =========================================================

# Q3.1 - Average mpg for each cylinders group
print("\nQ3.1 - Average MPG by cylinders:")

average_mpg = df.groupby('cylinders')['mpg'].mean()

print(average_mpg)


# Q3.2 - Maximum horsepower for each origin
print("\nQ3.2 - Maximum horsepower by origin:")

# Convert horsepower to numeric.
# Invalid values such as "?" become NaN.
df['horsepower'] = pd.to_numeric(
    df['horsepower'],
    errors='coerce'
)

max_horsepower = df.groupby('origin')['horsepower'].max()

print(max_horsepower)


# Q3.3 - Mean and median weight for each model year
print("\nQ3.3 - Weight statistics by model year:")

weight_stats = df.groupby('model_year')['weight'].agg(
    ['mean', 'median']
)

print(weight_stats)


# =========================================================
# 4. Unique & nunique
# =========================================================

# Q4.1 - Number of unique car names
print("\nQ4.1 - Number of unique car names:")

unique_names = df['name'].nunique()

print(unique_names)


# Q4.2 - All unique cylinders values
print("\nQ4.2 - Unique cylinders:")

unique_cylinders = df['cylinders'].unique()

print(unique_cylinders)


# Q4.3 - Number of unique model years
print("\nQ4.3 - Number of unique model years:")

unique_years = df['model_year'].nunique()

print(unique_years)