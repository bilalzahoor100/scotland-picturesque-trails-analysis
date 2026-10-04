from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
import os


# Chrome debug connection
options = Options()
options.debugger_address = "127.0.0.1:9222"

driver = webdriver.Chrome(options=options)


# Read URLs
urls = pd.read_csv("data/trail_urls.csv")


output_file = "data/trails_raw_2.csv"


# Resume if file already exists
if os.path.exists(output_file):
    results = pd.read_csv(output_file).to_dict("records")
    completed = set(results[i]["url"] for i in range(len(results)))
else:
    results = []
    completed = set()


for index, row in urls.iterrows():

    url = row["url"]

    if url in completed:
        continue

    print(f"\nProcessing {index+1}/{len(urls)}")
    print(url)


    try:

        driver.get(url)

        time.sleep(4)


        soup = BeautifulSoup(
            driver.page_source,
            "lxml"
        )


        text = soup.get_text(
            "\n",
            strip=True
        )


        # Title
        title = driver.title.split(",")[0]


        # Rating
        rating = None
        rating_match = re.search(
            r"\n(\d\.\d)\n\(\n([\d,]+) reviews",
            text
        )

        if rating_match:
            rating = rating_match.group(1)
            reviews = rating_match.group(2)


        else:
            reviews = None


        # Length
        length = None
        length_match = re.search(
            r"(\d+\.?\d*)\nkm\nLength",
            text
        )

        if length_match:
            length = length_match.group(1)


        # Elevation
        elevation = None
        elevation_match = re.search(
            r"(\d+)\nm\nElevation gain",
            text
        )

        if elevation_match:
            elevation = elevation_match.group(1)


        # Time
        duration = None
        duration_match = re.search(
            r"([\d–\-\.]+hr)\nEstimated time",
            text
        )

        if duration_match:
            duration = duration_match.group(1)


        # Difficulty
        difficulty = None

        difficulties = [
            "Easy",
            "Moderate",
            "Hard",
            "Very hard"
        ]

        for d in difficulties:
            if f"·\n{d}\n·" in text:
                difficulty = d


        # Route type
        route_type = None

        for r in ["Loop", "Out & back", "Point to point"]:
            if r in text:
                route_type = r
                break


        # Photos
        photos = None
        photo_match = re.search(
            r"([\d,]+)\nphotos",
            text
        )

        if photo_match:
            photos = photo_match.group(1)


        # Description
        description = None

        if "Estimated time" in text:
            parts = text.split("Estimated time")

            if len(parts) > 1:
                description = parts[1][:600]


        results.append({

            "trail_name": title,
            "rating": rating,
            "reviews": reviews,
            "difficulty": difficulty,
            "length_km": length,
            "elevation_gain_m": elevation,
            "estimated_time": duration,
            "route_type": route_type,
            "photos_count": photos,
            "description": description,
            "url": url

        })


        # Save after every trail
        pd.DataFrame(results).to_csv(
            output_file,
            index=False
        )


        print("Saved")


        time.sleep(3)


    except Exception as e:

        print("ERROR:", e)


driver.quit()


print("\nFinished!")