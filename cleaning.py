import pandas as pd

# ===========================
# STEP 1: Load the Dataset
# ===========================

df = pd.read_csv("marketing_campaign.csv", sep="\t")

print("Dataset Loaded Successfully!\n")

# ===========================
# STEP 2: Display First 5 Rows
# ===========================

print("First 5 Rows:")
print(df.head())

# ===========================
# STEP 3: Display Dataset Information
# ===========================

print("\nDataset Information:")
print(df.info())

# ===========================
# STEP 4: Check Missing Values
# ===========================

print("\nMissing Values:")
print(df.isnull().sum())

# ===========================
# STEP 5: Remove Duplicate Rows
# ===========================

duplicates = df.duplicated().sum()
print(f"\nDuplicate Rows Before Removal: {duplicates}")

df = df.drop_duplicates()

duplicates_after = df.duplicated().sum()
print(f"Duplicate Rows After Removal: {duplicates_after}")

# ===========================
# STEP 6: Fill Missing Values
# ===========================

# Fill numeric columns with mean
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

# Fill text columns with "Unknown"
text_columns = df.select_dtypes(include=["object"]).columns

for column in text_columns:
    df[column] = df[column].fillna("Unknown")

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# ===========================
# STEP 7: Standardize Text Columns
# ===========================

for column in text_columns:
    df[column] = df[column].astype(str).str.strip().str.lower()

print("\nText Values Standardized.")

# ===========================
# STEP 8: Rename Column Names
# ===========================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nColumn Names Renamed.")

# ===========================
# STEP 9: Convert Date Column
# ===========================

if "dt_customer" in df.columns:
    df["dt_customer"] = pd.to_datetime(
        df["dt_customer"],
        errors="coerce"
    )

print("\nDate Column Converted.")

# ===========================
# STEP 10: Check Data Types
# ===========================

print("\nData Types:")
print(df.dtypes)

# ===========================
# STEP 11: Save Cleaned Dataset
# ===========================

df.to_csv("cleaned_marketing_campaign.csv", index=False)

print("\nCleaned dataset saved successfully!")

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nData Cleaning Completed Successfully!")