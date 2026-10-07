import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# Exercise 1 - Taxi Fare Linear Model
# =========================================================

x = np.arange(0, 11)
y = 8 + 5 * x

plt.figure(figsize=(8, 5))

plt.plot(
    x,
    y,
    label='Taxi Fare'
)

plt.title('Taxi Fare vs Distance')
plt.xlabel('Distance (km)')
plt.ylabel('Fare')

plt.xlim(0, 10)
plt.ylim(0, 60)

plt.legend()

plt.savefig('taxi_fare_line.jpg')
plt.show()


# =========================================================
# Exercise 2 - Load tips.csv
# =========================================================

df = pd.read_csv('tips.csv')

print(df.head())


# =========================================================
# Exercise 2.1 - Scatter Plot
# =========================================================

plt.figure(figsize=(8, 5))

plt.scatter(
    df['price_per_person'],
    df['tip']
)

plt.title('Price Per Person vs Tip')
plt.xlabel('Price Per Person')
plt.ylabel('Tip')

plt.show()

# Answer:
# There is a weak-to-moderate positive correlation.
# As price_per_person increases, tip tends to increase.


# =========================================================
# Exercise 2.2 - Bar Chart
# Maximum total_bill per day
# =========================================================

max_bill_per_day = (
    df.groupby('day')['total_bill'].max()
)

plt.figure(figsize=(8, 5))

plt.bar(
    max_bill_per_day.index,
    max_bill_per_day.values
)

plt.title('Maximum Total Bill Per Day')
plt.xlabel('Day')
plt.ylabel('Maximum Total Bill')

plt.show()


# =========================================================
# Exercise 2.3 - Histogram of Tips
# =========================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df['tip'],
    bins=10
)

plt.title('Distribution of Tips')
plt.xlabel('Tip')
plt.ylabel('Frequency')

plt.show()

# Answer:
# The most common tips are approximately $2-$3.


# =========================================================
# Exercise 2.4 - Histogram of Tip Percentage
# =========================================================

df['tip_perc'] = (
    100 * df['tip'] / df['total_bill']
)

plt.figure(figsize=(8, 5))

plt.hist(
    df['tip_perc'],
    bins=10
)

plt.title('Distribution of Tip Percentage')
plt.xlabel('Tip Percentage (%)')
plt.ylabel('Frequency')

plt.show()

# Answer:
# The most common tip percentage is approximately 10%-17%.


# =========================================================
# Exercise 2.5 - 2x2 Subplots
# =========================================================

fig, axes = plt.subplots(
    2,
    2,
    figsize=(10, 7)
)


# -------------------------
# Top Left - Scatter
# -------------------------

axes[0, 0].scatter(
    df['price_per_person'],
    df['tip']
)

axes[0, 0].set_title(
    'Price Per Person vs Tip'
)

axes[0, 0].set_xlabel(
    'Price Per Person'
)

axes[0, 0].set_ylabel(
    'Tip'
)


# -------------------------
# Top Right - Bar
# -------------------------

axes[0, 1].bar(
    max_bill_per_day.index,
    max_bill_per_day.values
)

axes[0, 1].set_title(
    'Maximum Total Bill Per Day'
)

axes[0, 1].set_xlabel(
    'Day'
)

axes[0, 1].set_ylabel(
    'Maximum Total Bill'
)


# -------------------------
# Bottom Left - Tip Histogram
# -------------------------

axes[1, 0].hist(
    df['tip'],
    bins=10
)

axes[1, 0].set_title(
    'Distribution of Tips'
)

axes[1, 0].set_xlabel(
    'Tip'
)

axes[1, 0].set_ylabel(
    'Frequency'
)


# -------------------------
# Bottom Right - Tip Percentage
# -------------------------

axes[1, 1].hist(
    df['tip_perc'],
    bins=10
)

axes[1, 1].set_title(
    'Distribution of Tip Percentage'
)

axes[1, 1].set_xlabel(
    'Tip Percentage (%)'
)

axes[1, 1].set_ylabel(
    'Frequency'
)


# Adjust spacing
plt.tight_layout()

# Save figure
plt.savefig('tips_overview.png')

# Show figure
plt.show()