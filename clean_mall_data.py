import pandas as pd

# Load the dataset (make sure the file is in the same folder as this script)
df = pd.read_csv('Mall_Customers.csv')

# ----- Step 1: View the first few rows -----
print("Initial Data Preview:")
print(df.head())

# ----- Step 2: Check for missing values -----
print("\nMissing Values:")
print(df.isnull().sum())

# Example: Fill missing 'Age' values with the mean (if any)
if df['Age'].isnull().sum() > 0:
    df['Age'] = df['Age'].fillna(df['Age'].mean())

# Drop any rows with other missing values
df.dropna(inplace=True)

# ----- Step 3: Remove duplicate rows -----
duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows Found: {duplicates}")
df.drop_duplicates(inplace=True)

# ----- Step 4: Standardize text (e.g., Gender column) -----
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.strip().str.capitalize()

# ----- Step 5: Clean column names -----
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# ----- Step 6: Check and fix data types -----
print("\nData Types Before Fixing:")
print(df.dtypes)

# Ensure Age is int
if df['age'].dtype != 'int':
    df['age'] = df['age'].astype(int)

# ----- Step 7: Save cleaned data -----
df.to_csv('Mall_Customers_Cleaned.csv', index=False)
print("\n✅ Data cleaning complete. File saved as 'Mall_Customers_Cleaned.csv'.")

# ----- Optional: Summary of actions -----
print("\nSummary:")
print("- Missing values handled")
print("- Duplicates removed")
print("- Gender values standardized")
print("- Column names cleaned")
print("- Data types corrected")
