import requests

WIDTH = 1920
HEIGHT = 1080

API = "https://api.hypixel.net/v2/resources/skyblock"
FONTS = {
    "big": ("Segoe UI", 18, "bold"),
    "small": ("Segoe UI", 13, "bold")
}

def fetch_weapons():
    response = requests.get(API + "/items").json()
    weapons = [r for r in response["items"] if r.get("category") == "SWORD" and r.get("tier") != "UNOBTAINABLE" and "origin" not in r]

    return weapons