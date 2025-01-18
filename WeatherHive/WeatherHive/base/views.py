from django.shortcuts import render
import requests  # Used to make HTTP requests
import json  # Used to handle JSON data

# Function to fetch weather data for a given city using OpenWeatherMap API
def get_weather(city):
    # Base URL for the OpenWeatherMap API
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    # Your API key to authenticate with the OpenWeatherMap service
    api_key = "91df26171e12a91e9dd20e6819b5ebeb"
    # Parameters to be sent with the API request
    parameters = {
        "q": city,        # The city name entered by the user
        "appid": api_key, # The API key for authentication
        "units": 'metric' # Unit of temperature (Celsius)
    }
    # Sending a GET request to the API
    response = requests.get(base_url, params=parameters)
    # Check if the API request was successful
    if response.status_code == 200:
        # If successful, return the JSON response
        return response.json()
    else:
        # If not successful, return None
        return None

# View function for the home page
def home(request):
    # Retrieve the city name from the GET request's query parameters
    city = request.GET.get('city')
    # Default icon URL in case no valid weather data is available
    icon_url = "https://openweathermap.org/img/wn/10d@2x.png"
    if city:
        # Fetch the weather data for the specified city
        weather_data_result = get_weather(city)
        
        if weather_data_result is not None:
            # Extract the weather icon ID and generate the icon URL
            icon_id = weather_data_result["weather"][0]["icon"]
            icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
            # Extract weather details from the API response
            weather = weather_data_result['weather'][0]['main']  # Main weather condition
            weather_description = weather_data_result['weather'][0]['description']  # Detailed weather description
            city = weather_data_result['name']  # City name (corrected for API results)
            country = weather_data_result['sys']['country']  # Country code
            wind_speed = weather_data_result['wind']['speed']  # Wind speed
            pressure = weather_data_result['main']['pressure']  # Atmospheric pressure
            humidity = weather_data_result['main']['humidity']  # Humidity percentage
            temperature = weather_data_result['main']['temp']  # Current temperature
        else:
            # If weather data is not available, render the template without details
            return render(request, "index.html")
    
    # Render the home page with the weather data and icon
    return render(request, "index.html", {
        "icon_url": icon_url,                 # Weather icon URL
        "weather": weather,                   # Main weather condition
        "weather_description": weather_description, # Detailed weather description
        "city": city,                         # City name
        "country": country,                   # Country code
        "wind_speed": wind_speed,             # Wind speed
        "pressure": pressure,                 # Atmospheric pressure
        "humidity": humidity,                 # Humidity percentage
        "temperature": temperature,           # Current temperature
    })
    
    # Redundant return statement; unreachable code
    return render(request, "index.html")
