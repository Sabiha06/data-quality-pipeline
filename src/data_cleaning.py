import pandas as pd

# Load data
df = pd.read_csv("data/raw_data.csv")
print(df.columns)

print("Initial Shape:", df.shape)

# ---------------------------
#DATA QUALITY CHECKS 
#---------------------------

missing = df.isnull().sum()
duplicates = df.duplicated().sum()

# ---------------------------
# DATA CLEANING
# ---------------------------

# Remove exact duplicates
df = df.drop_duplicates()

# Standardize column names
df.columns = df.columns.str.lower().str.strip()

# ---------------------------
# VALIDATION RULES
# ---------------------------

# Convert age to numeric
df['age'] = pd.to_numeric(df['age'], errors='coerce')

# Remove invalid ages
df = df[(df['age'] > 0) & (df['age'] < 120)]

# Remove invalid emails
df = df[df['email'].str.contains('@', na=False)]

# Remove rows missing critical fields
df = df.dropna(subset=['patient_id', 'name'])

# ---------------------------
# SAVE CLEAN DATA
# ---------------------------

df.to_csv("output/cleaned_data.csv", index=False)

# ---------------------------
# QUALITY REPORT
# ---------------------------

with open("output/quality_report.txt", "w") as f:
    f.write("=== DATA QUALITY REPORT ===\n\n")
    f.write(f"Initial rows: {df.shape[0]}\n\n")
    
    f.write("Missing Values (Before Cleaning):\n")
    f.write(f"{missing}\n\n")
    
    f.write(f"Duplicate rows detected: {duplicates}\n")

print("Data cleaning complete. Check output folder.")