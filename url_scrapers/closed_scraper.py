import requests
import json
import os

from common.config import PAGES_NUM, FINISHED_URL


closed_houses = []
closed_apartments = []

for page in range(1, PAGES_NUM):
    resp = requests.get(f"{FINISHED_URL}{page}")
    data = json.loads(resp.content)
    for item in data["data"]:
        if item["listing_type"] == "sell":
            if item["category"]["name"] == "Kuće":
                closed_houses.append(item["id"])
            elif item["category"]["name"] == "Stanovi":
                closed_apartments.append(item["id"])
                
                
with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "houses.txt"), "w") as file:
    for house in closed_houses:
        file.write(f"{house}\n")
        
with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "apartments.txt"), "w") as file:
    for apartment in closed_apartments:
        file.write(f"{apartment}\n")