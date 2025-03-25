import requests
import json

# Ganti dengan API key OpenWeather milikmu
API_KEY = "OpenWeatherAPIKey"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric" 
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        
        print(f"\n🌍 Kota: {city_name}")
        print(f"🌡️ Suhu: {temp}°C")
        print(f"🌥️ Cuaca: {weather_desc.capitalize()}")
    else:
        print("❌ Kota tidak ditemukan")

if __name__ == "__main__":
    city = input("Masukkan nama kota: ")
    get_weather(city)
