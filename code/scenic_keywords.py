import pandas as pd

df = pd.read_csv("data/trails_clean.csv")

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
    "coastal",
    "sea",
    "beach",
    "castle",
    "glen",
    "valley",
    "nature",
    "wildlife",
    "hill"
]

print("Keyword frequencies\n")

for word in keywords:

    count = df["description"].str.lower().str.contains(word).sum()

    print(f"{word:12} {count}")