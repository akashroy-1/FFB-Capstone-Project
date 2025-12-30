import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.environ['API_KEY']

import requests
from datetime import date

# Your API key
#API_KEY = "your-api-key"
BASE_URL = "https://api.balldontlie.io"

# Set up headers with authentication
headers = {"Authorization": API_KEY}

# Get today's date
today = date.today().isoformat()

# Fetch today's NFL games
response = requests.get(
    f"{BASE_URL}/nba/v1/games",
    headers=headers,
    params={"dates[]": today}
)

# Print the results
data = response.json()
print(f"Found {len(data['data'])} games for {today}:\n")

for game in data["data"]:
    home = game["home_team"]
    away = game["visitor_team"]
    score = f"{game['visitor_team_score']}-{game['home_team_score']}"
    print(f"{away['abbreviation']} @ {home['abbreviation']}: {score} ({game['status']})")
