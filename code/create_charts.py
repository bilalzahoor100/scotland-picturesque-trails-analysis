import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/picturesque_routes.csv")


# 1. Rating distribution

plt.figure(figsize=(8,5))

df["rating"].value_counts().sort_index().plot(kind="bar")

plt.title("Distribution of Trail Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Trails")

plt.tight_layout()

plt.savefig("charts/rating_distribution.png")

plt.close()



# 2. Difficulty distribution

plt.figure(figsize=(8,5))

df["difficulty"].value_counts().plot(kind="bar")

plt.title("Trail Difficulty Distribution")
plt.xlabel("Difficulty")
plt.ylabel("Number of Trails")

plt.tight_layout()

plt.savefig("charts/difficulty_distribution.png")

plt.close()



# 3. Route type distribution

plt.figure(figsize=(8,5))

df["route_type"].value_counts().plot(kind="bar")

plt.title("Route Type Distribution")
plt.xlabel("Route Type")
plt.ylabel("Number of Trails")

plt.tight_layout()

plt.savefig("charts/route_type_distribution.png")

plt.close()



# 4. Elevation distribution

plt.figure(figsize=(8,5))

plt.hist(df["elevation_gain_m"], bins=15)

plt.title("Elevation Gain Distribution")
plt.xlabel("Elevation Gain (m)")
plt.ylabel("Number of Trails")

plt.tight_layout()

plt.savefig("charts/elevation_distribution.png")

plt.close()



# 5. Top 10 picturesque routes

top10 = df.head(10).sort_values(
    "picturesque_score"
)


plt.figure(figsize=(10,6))

plt.barh(
    top10["trail_name"],
    top10["picturesque_score"]
)

plt.title("Top 10 Most Picturesque Running Routes in Scotland")

plt.xlabel("Picturesque Score")

plt.tight_layout()

plt.savefig("charts/top10_picturesque_routes.png")

plt.close()


print("Charts created successfully!")