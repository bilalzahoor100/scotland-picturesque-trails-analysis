import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/trails_clean.csv")

# Scenic keywords
keywords = [
    "mountain",
    "summit",
    "view",
    "views",
    "loch",
    "lake",
    "river",
    "waterfall",
    "forest",
    "woodland",
    "coast",
    "sea",
    "beach",
    "castle",
    "glen",
    "valley",
    "nature",
    "wildlife",
    "hill"
]

# Count scenic keywords
def keyword_score(text):
    text = str(text).lower()
    return sum(text.count(word) for word in keywords)

df["keyword_score"] = df["description"].apply(keyword_score)

# Normalise values (0 to 1)
df["rating_norm"] = df["rating"] / df["rating"].max()
df["reviews_norm"] = df["reviews"] / df["reviews"].max()
df["elevation_norm"] = df["elevation_gain_m"] / df["elevation_gain_m"].max()
df["keyword_norm"] = df["keyword_score"] / df["keyword_score"].max()

# Picturesque Score
df["picturesque_score"] = (
    df["rating_norm"] * 0.40 +
    df["reviews_norm"] * 0.20 +
    df["elevation_norm"] * 0.20 +
    df["keyword_norm"] * 0.20
)

# Sort highest first
df = df.sort_values(
    "picturesque_score",
    ascending=False
)

# Save
df.to_csv(
    "data/picturesque_routes.csv",
    index=False
)

print(df[
    [
        "trail_name",
        "picturesque_score",
        "rating",
        "reviews",
        "keyword_score",
        "elevation_gain_m"
    ]
].head(10).to_string(index=False))