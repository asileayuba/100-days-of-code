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
    
    # Initialize the context with default icon URL and error (if needed)
    context = {
        "icon_url": "https://openweathermap.org/img/wn/10d@2x.png",  # Default icon URL
    }

    if city:
        # Fetch the weather data for the specified city
        weather_data_result = get_weather(city)
        
        if weather_data_result is not None:
            # Extract weather details and add them to the context
            icon_id = weather_data_result["weather"][0]["icon"]
            context.update({
                "icon_url": f"https://openweathermap.org/img/wn/{icon_id}@2x.png",
                "weather": weather_data_result['weather'][0]['main'],
                "weather_description": weather_data_result['weather'][0]['description'],
                "city": weather_data_result['name'],
                "country": weather_data_result['sys']['country'],
                "wind_speed": weather_data_result['wind']['speed'],
                "pressure": weather_data_result['main']['pressure'],
                "humidity": weather_data_result['main']['humidity'],
                "temperature": weather_data_result['main']['temp'],
            })
        else:
            # Add an error message to the context
            context["error"] = "City not found or API issue"

    return render(request, "index.html", context)
