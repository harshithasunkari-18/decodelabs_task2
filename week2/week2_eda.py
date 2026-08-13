import pandas as pd

# ==========================
# LOAD DATASET
# ==========================
df = pd.read_excel("cleaned_dataset(1).xlsx")   # Change the filename if needed

# ==========================
# DATASET OVERVIEW
# ==========================
print("=" * 70)
print("          WEEK 2 EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 70)

print("\nDATASET OVERVIEW")
print("-" * 70)
print(f"Total Rows    : {df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")

# Display column names
print("\nColumns:")
print(df.columns.tolist())

# ==========================
# BASIC STATISTICS
# ==========================
print("\nBASIC STATISTICS")
print("-" * 70)
print(df.describe(include="all"))

# ==========================
# MISSING VALUE ANALYSIS
# ==========================
print("\nMISSING VALUE ANALYSIS")
print("-" * 70)

missing_values = df.isnull().sum()

if missing_values.sum() == 0:
    print("No missing values found.")
else:
    print(missing_values)

# ==========================
# DUPLICATE RECORDS ANALYSIS
# ==========================
print("\nDUPLICATE RECORDS ANALYSIS")
print("-" * 70)

duplicate_rows = df.duplicated().sum()

if duplicate_rows == 0:
    print("No duplicate records found.")
else:
    print(f"Duplicate Rows: {duplicate_rows}")

# ==========================
# PRODUCT ANALYSIS
# ==========================
print("\nPRODUCT ANALYSIS")
print("-" * 70)
print(df["Product"].value_counts())

# ==========================
# PAYMENT METHOD ANALYSIS
# ==========================
print("\nPAYMENT METHOD ANALYSIS")
print("-" * 70)
print(df["PaymentMethod"].value_counts())

# ==========================
# ORDER STATUS ANALYSIS
# ==========================
print("\nORDER STATUS ANALYSIS")
print("-" * 70)
print(df["OrderStatus"].value_counts())

# ==========================
# REVENUE ANALYSIS
# ==========================
print("\nREVENUE ANALYSIS")
print("-" * 70)

total_revenue = df["TotalPrice"].sum()
average_order_value = df["TotalPrice"].mean()
highest_order = df["TotalPrice"].max()
lowest_order = df["TotalPrice"].min()

print(f"Total Revenue         : ${total_revenue:,.2f}")
print(f"Average Order Value   : ${average_order_value:,.2f}")
print(f"Highest Order Value   : ${highest_order:,.2f}")
print(f"Lowest Order Value    : ${lowest_order:,.2f}")

# ==========================
# OUTLIER ANALYSIS
# ==========================
print("\nOUTLIER ANALYSIS")
print("-" * 70)

Q1 = df["TotalPrice"].quantile(0.25)
Q3 = df["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

outliers = df[
    (df["TotalPrice"] < lower_bound) |
    (df["TotalPrice"] > upper_bound)
]

print(f"Number of Outliers : {len(outliers)}")

if len(outliers) > 0:
    print("\nOutlier Records:")
    print(outliers[["CustomerID", "Product", "TotalPrice"]])

# ==========================
# KEY OBSERVATIONS
# ==========================
print("\nKEY OBSERVATIONS")
print("-" * 70)

print(f"1. Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")
print(f"2. Missing Values: {missing_values.sum()}")
print(f"3. Duplicate Records: {duplicate_rows}")
print(f"4. Most Sold Product: {df['Product'].value_counts().idxmax()}")
print(f"5. Most Preferred Payment Method: {df['PaymentMethod'].value_counts().idxmax()}")
print(f"6. Most Common Order Status: {df['OrderStatus'].value_counts().idxmax()}")
print(f"7. Total Revenue Generated: ${total_revenue:,.2f}")
print(f"8. Average Order Value: ${average_order_value:,.2f}")
print(f"9. Highest Order Value: ${highest_order:,.2f}")
print(f"10. Lowest Order Value: ${lowest_order:,.2f}")
print(f"11. Number of Outliers: {len(outliers)}")

print("\n" + "=" * 70)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 70)