import pandas as pd
import plotly.express as px


df = pd.read_csv(
    "data/picturesque_routes.csv"
)


# Top 10 trails

top10 = df.head(10).sort_values(
    "picturesque_score"
)


fig1 = px.bar(
    top10,
    x="picturesque_score",
    y="trail_name",
    orientation="h",
    title="Top 10 Most Picturesque Running Routes in Scotland",
    hover_data=[
        "rating",
        "reviews",
        "elevation_gain_m",
        "difficulty"
    ]
)


fig1.write_html(
    "dashboard/top10_routes.html"
)



# Elevation vs Picturesque Score

fig2 = px.scatter(
    df,
    x="elevation_gain_m",
    y="picturesque_score",
    size="reviews",
    hover_name="trail_name",
    color="difficulty",
    title="Relationship Between Elevation and Picturesque Score"
)


fig2.write_html(
    "dashboard/elevation_vs_score.html"
)


print("Interactive dashboards created!")