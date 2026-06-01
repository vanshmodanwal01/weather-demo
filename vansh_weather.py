import requests
import geocoder

# Get live location using IP
g = geocoder.ip('me')
latitude, longitude = g.latlng

print(f"\n📍 Live Location Coordinates:")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")

# Open-Meteo API URL
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={latitude}&longitude={longitude}"
    f"&current=temperature_2m,relative_humidity_2m,windspeed_10m,cloud_cover"
    f"&hourly=shortwave_radiation"
)

try:
    response = requests.get(url)
    data = response.json()

    print("\n----- 🌦 LIVE WEATHER REPORT -----\n")

    current = data["current"]

    print(f"🌡 Temperature     : {current['temperature_2m']} °C")
    print(f"💧 Humidity        : {current['relative_humidity_2m']} %")
    print(f"💨 Wind Speed      : {current['windspeed_10m']} km/h")
    print(f"☁ Cloud Cover     : {current['cloud_cover']} %")

    radiation = data["hourly"]["shortwave_radiation"][0]
    print(f"☀ Solar Irradiance : {radiation} W/m²")

except Exception as e:
    print("❌ Error fetching data:", e)

