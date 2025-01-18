from django.shortcuts import render
import requests
import json


def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "91df26171e12a91e9dd20e6819b5ebeb"
    parameters = {
        "q": city,
        "appid": api_key,
        "units": 'metric'
    }
    response = requests.get(base_url, params = parameters)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def home(request):
    city = request.GET.get('city')
    if city:
        weather_data_result = get_weather(city)
        
        if weather_data_result is not None:
            weather_data = json.dumps(weather_data_result, indent=4)
            print(weather_data)
            
    return render(request, "index.html")