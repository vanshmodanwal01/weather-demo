# 🌦️ Live Weather Report using Python

A Python project that automatically detects the user's location using their IP address and fetches real-time weather data using the Open-Meteo API.

## 🚀 Features

- 📍 Detects live location using IP address
- 🌡️ Shows current temperature
- 💧 Displays relative humidity
- 💨 Shows wind speed
- ☁️ Displays cloud cover percentage
- ☀️ Shows solar irradiance data
- 🌐 Uses Open-Meteo API for live weather updates

## 🛠️ Technologies Used

- Python
- Requests Library
- Geocoder Library
- Open-Meteo API

## 📦 Installation

Install the required packages:

```bash
pip install requests geocoder
```

## ▶️ Run the Program

```bash
python weather.py
```

## 📋 Sample Output

```text
📍 Live Location Coordinates:
Latitude: 26.8467
Longitude: 80.9462

------ 🌤️ LIVE WEATHER REPORT ------

🌡️ Temperature     : 32°C
💧 Humidity        : 65%
💨 Wind Speed      : 14 km/h
☁️ Cloud Cover     : 20%
☀️ Solar Irradiance: 650 W/m²
```

## 📚 How It Works

1. The program detects the user's latitude and longitude using IP geolocation.
2. Coordinates are sent to the Open-Meteo API.
3. The API returns live weather information.
4. The program extracts and displays the data in a readable format.

## ⚠️ Requirements

- Internet Connection
- Python 3.x

## 🔮 Future Improvements

- 7-Day Weather Forecast
- Weather Alerts
- GUI using Tkinter
- Save Weather History
- City Search Feature

## 👨‍💻 Author

Vansh Modanwal

Learning Python through real-world projects.
