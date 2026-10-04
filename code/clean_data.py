import pandas as pd

df = pd.read_csv("data/trails_raw.csv")

print("Rows before cleaning:", len(df))

# Remove duplicate trails
df = df.drop_duplicates(subset=["trail_name"])

# Remove rows with no rating
df = df.dropna(subset=["rating"])

# Remove rows with no description
df = df.dropna(subset=["description"])

# Convert reviews to numbers
df["reviews"] = (
    df["reviews"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

df["reviews"] = pd.to_numeric(df["reviews"], errors="coerce")

# Save cleaned dataset
df.to_csv("data/trails_clean.csv", index=False)

print("Rows after cleaning:", len(df))
print("\nMissing values:")
print(df.isnull().sum())