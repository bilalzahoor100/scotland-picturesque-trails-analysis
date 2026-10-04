# Scotland Picturesque Trails Analysis

A Python-based data analysis project exploring Scottish running and hiking trails using publicly available trail information from AllTrails.

The project combines trail characteristics, user ratings, popularity and scenic language to identify routes with a higher **Picturesque Score**.

## Project Overview

The analysis focuses on understanding what characteristics are associated with picturesque trails across Scotland.

The project covers the complete data analytics workflow:

- Data collection
- Data cleaning and preparation
- Feature engineering
- Scenic keyword analysis
- Custom scoring methodology
- Exploratory data analysis
- Data visualisation
- Interactive dashboard development

## Key Results

The final analysis contains **98 cleaned Scottish trails**.

The highest-ranked routes based on the custom Picturesque Score include:

| Rank | Trail | Picturesque Score |
|---:|---|---:|
| 1 | Ben Lomond Mountain Path | 0.821 |
| 2 | Ben Nevis Mountain Trail: Halfway Lochan View | 0.766 |
| 3 | Meall a' Bhuachaille | 0.764 |
| 4 | Goat Fell Out and Back | 0.748 |
| 5 | Meikle Pap | 0.747 |

Other observations include:

- Average trail rating of approximately **4.66/5**
- Mountain and elevated routes were strongly represented among the highest-ranked trails
- Scenic terms such as **view, loch, mountain, hill and glen** appeared frequently in trail descriptions

## Picturesque Score

A custom scoring model was developed to rank trails based on four components:

| Factor | Weight |
|---|---:|
| User rating | 40% |
| Review popularity | 20% |
| Elevation gain | 20% |
| Scenic keywords | 20% |

Each component was normalised before being combined into the final score.

The scenic keyword analysis searches trail descriptions for landscape-related terms such as:

- Mountain
- Summit
- View
- Loch
- Lake
- River
- Waterfall
- Forest
- Glen
- Castle
- Wildlife

The resulting score is intended as an **analytical ranking metric**, rather than an official measure of scenic quality.

## Data Pipeline

The project uses a multi-stage workflow:

```text
Trail Data
    ↓
Data Collection
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
Scenic Keyword Analysis
    ↓
Picturesque Score
    ↓
Exploratory Data Analysis
    ↓
Visualisations
    ↓
Interactive Dashboards
```

## Technologies

### Data Collection
- Python
- Selenium
- BeautifulSoup

### Data Analysis
- Pandas
- NumPy

### Visualisation
- Matplotlib
- Plotly

### Development
- Python
- HTML
- CSV

## Visualisations

The project includes visualisations covering:

- Top picturesque routes
- Rating distribution
- Elevation distribution
- Difficulty distribution
- Route type distribution
- Elevation versus Picturesque Score

The interactive Plotly dashboards are available in the `dashboard/` directory.

## Project Structure

```text
scotland-picturesque-trails-analysis/
│
├── charts/
│   ├── difficulty_distribution.png
│   ├── elevation_distribution.png
│   ├── rating_distribution.png
│   ├── route_type_distribution.png
│   └── top10_picturesque_routes.png
│
├── code/
│   ├── clean_data.py
│   ├── create_charts.py
│   ├── create_dashboard.py
│   ├── eda.py
│   ├── picturesque_score.py
│   ├── scenic_keywords.py
│   ├── scrape_trails.py
│   └── ...
│
├── dashboard/
│   ├── elevation_vs_score.html
│   └── top10_routes.html
│
├── data/
│   ├── picturesque_routes.csv
│   └── trails_clean.csv
│
├── requirements.txt
└── README.md
```

## Running the Project

Clone the repository and install the required Python packages:

```bash
git clone <repository-url>
cd scotland-picturesque-trails-analysis

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

The analysis scripts can then be run as required:

```bash
python code/clean_data.py
python code/picturesque_score.py
python code/eda.py
python code/create_charts.py
python code/create_dashboard.py
```

## Limitations

The analysis has several limitations:

- The dataset represents a limited selection of Scottish trails rather than the entire trail network.
- Scenic quality is partly inferred from text descriptions and therefore cannot capture every visual characteristic.
- Popularity can influence rankings because highly reviewed trails receive stronger popularity signals.
- Weather, seasonality and trail accessibility are not included.
- The Picturesque Score is a custom analytical metric and should not be interpreted as an objective measure of scenic quality.

Potential future improvements include:

- Natural language processing of user reviews
- Image-based scenic analysis
- Geographic and spatial analysis
- Weather and seasonal data
- Additional trail characteristics
- Sentiment analysis

## Disclaimer

Trail information used in this analysis was sourced from publicly available online trail information. The project is intended for **educational and portfolio purposes** and does not represent an official rating or recommendation from the original data source.

## Author

**Bilal Zahoor**

Data & BI Engineer | Data Analyst

---

*This project demonstrates an end-to-end approach to collecting, transforming, analysing and visualising real-world data to generate actionable insights.*