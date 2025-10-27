import os, requests

WEATHER_BASE = os.getenv("WEATHER_BASE", "http://weather-service:8789")
DEF_CITY = os.getenv("WEATHER_DEFAULT_CITY", "")
DEF_STATE = os.getenv("WEATHER_DEFAULT_STATE", "")

def weather_today(city: str | None = None, state: str | None = None) -> str:
    params = {}
    if city:  params["city"] = city
    if state: params["state"] = state
    if not city and DEF_CITY:     params["city"] = DEF_CITY
    if not state and DEF_STATE:   params["state"] = DEF_STATE

    r = requests.get(f"{WEATHER_BASE}/today", params=params, timeout=12)
    r.raise_for_status()
    data = r.json()
    if "message" in data:
        return data["message"]
    return f"Weather lookup failed: {data}"
