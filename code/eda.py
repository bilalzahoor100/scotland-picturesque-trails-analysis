import pandas as pd

# Load dataset
df = pd.read_csv("data/picturesque_routes.csv")

print("=" * 50)
print("Dataset Overview")
print("=" * 50)

print(df.info())

print("\n")

print("=" * 50)
print("Summary Statistics")
print("=" * 50)

print(df.describe())

print("\n")

print("=" * 50)
print("Difficulty Distribution")
print("=" * 50)

print(df["difficulty"].value_counts())

print("\n")

print("=" * 50)
print("Route Types")
print("=" * 50)

print(df["route_type"].value_counts())

print("\n")

print("=" * 50)
print("Top 10 Picturesque Routes")
print("=" * 50)

print(
    df[
        [
            "trail_name",
            "picturesque_score",
            "rating",
            "reviews",
            "difficulty",
            "length_km",
            "elevation_gain_m"
        ]
    ].head(10)
)