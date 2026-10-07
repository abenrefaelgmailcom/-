import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# PART 1 - MATPLOTLIB / MPG
# =========================================================

df = pd.read_csv("mpg (1).csv")


# ---------------------------------------------------------
# 1. Scatter Plot - Horsepower vs MPG
# Color by origin
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["horsepower"],
    df["mpg"],
    c=df["origin"]
)

plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.title("Horsepower vs MPG")

plt.show()


# ---------------------------------------------------------
# 2. Average MPG - 4 vs 8 Cylinders
# ---------------------------------------------------------

df_4_8 = df[
    df["cylinders"].isin([4, 8])
]

avg_mpg = (
    df_4_8
    .groupby("cylinders")["mpg"]
    .mean()
)

print("Average MPG:")
print(avg_mpg)

plt.figure(figsize=(7, 5))

plt.bar(
    avg_mpg.index.astype(str),
    avg_mpg.values
)

plt.xlabel("Cylinders")
plt.ylabel("Average MPG")
plt.title("Average MPG: 4 vs 8 Cylinders")

plt.show()


# ---------------------------------------------------------
# 3. Count Cars by Origin
# ---------------------------------------------------------

origin_counts = df["origin"].value_counts()

print("Cars by origin:")
print(origin_counts)

plt.figure(figsize=(7, 5))

plt.bar(
    origin_counts.index.astype(str),
    origin_counts.values
)

plt.xlabel("Origin")
plt.ylabel("Number of Cars")
plt.title("Number of Cars by Origin")

plt.show()


# ---------------------------------------------------------
# 4. Histogram - Weight
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["weight"],
    bins=20
)

plt.xlabel("Weight")
plt.ylabel("Frequency")
plt.title("Distribution of Car Weight")

plt.show()


# ---------------------------------------------------------
# 5. Box Plot - MPG by Cylinders
# ---------------------------------------------------------

cylinder_types = sorted(
    df["cylinders"].unique()
)

mpg_groups = [
    df[df["cylinders"] == c]["mpg"]
    for c in cylinder_types
]

plt.figure(figsize=(8, 5))

plt.boxplot(
    mpg_groups,
    tick_labels=cylinder_types
)

plt.xlabel("Cylinders")
plt.ylabel("MPG")
plt.title("MPG by Number of Cylinders")

plt.show()


# =========================================================
# PART 2 - PANDAS / BOOKS DATA CLEANING
# =========================================================

books = pd.read_csv("books.csv")
sales = pd.read_csv("books_sales.csv")


# ---------------------------------------------------------
# 1. Find duplicate catalog numbers
# ---------------------------------------------------------

duplicates = books[
    books.duplicated(
        subset="catalog_number",
        keep=False
    )
].copy()

print("\nDuplicate books:")
print(duplicates)


# ---------------------------------------------------------
# 2. Count non-NaN values in each duplicate row
# ---------------------------------------------------------

duplicates["non_nan_count"] = (
    duplicates.notna().sum(axis=1)
)

print("\nDuplicates with non-NaN count:")
print(duplicates)


# ---------------------------------------------------------
# 3. Find the best row for each catalog number
# ---------------------------------------------------------

keep_indices = (
    duplicates
    .groupby("catalog_number")["non_nan_count"]
    .idxmax()
)

kept = duplicates.loc[
    keep_indices,
    ["catalog_number", "book_id"]
].copy()

kept = kept.rename(
    columns={
        "book_id": "book_id_kept"
    }
)


# ---------------------------------------------------------
# 4. Merge duplicates with the kept IDs
# ---------------------------------------------------------

mapping = duplicates.merge(
    kept,
    on="catalog_number",
    how="inner"
)


# Keep only books that should be removed
mapping = mapping[
    mapping["book_id"] != mapping["book_id_kept"]
].copy()

mapping = mapping.rename(
    columns={
        "book_id": "book_id_removed"
    }
)

print("\nID replacement mapping:")
print(
    mapping[
        [
            "catalog_number",
            "book_id_removed",
            "book_id_kept"
        ]
    ]
)


# ---------------------------------------------------------
# 5. Remove duplicate books
# ---------------------------------------------------------

books_clean = books[
    ~books["book_id"].isin(
        mapping["book_id_removed"]
    )
].copy()


# ---------------------------------------------------------
# 6. Create old ID -> new ID dictionary
# ---------------------------------------------------------

replacement_dict = dict(
    zip(
        mapping["book_id_removed"],
        mapping["book_id_kept"]
    )
)

print("\nReplacement dictionary:")
print(replacement_dict)


# ---------------------------------------------------------
# 7. Update book IDs in sales table
# ---------------------------------------------------------

sales["book_id"] = (
    sales["book_id"]
    .replace(replacement_dict)
)


# ---------------------------------------------------------
# 8. Save clean files
# ---------------------------------------------------------

books_clean.to_csv(
    "books_clean.csv",
    index=False
)

sales.to_csv(
    "books_sales_clean.csv",
    index=False
)


print("\nBooks cleaned successfully.")
print("Sales IDs updated successfully.")