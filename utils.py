import requests

API = "https://api.hypixel.net/v2/resources/skyblock"

ITEMS = requests.get(API + "/items").json()

def fetch_weapons():
    response = requests.get(API + "/items").json()
    weapons = [r for r in response["items"] if r.get("category") == "SWORD" and r.get("tier") != "UNOBTAINABLE" and "origin" not in r]

    return weapons