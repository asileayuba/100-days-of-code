from django.shortcuts import render
import requests
import json


def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "91df26171e12a91e9dd20e6819b5ebeb"
    params = 


def home(request):
    return render(request, "index.html")