from django.test import TestCase, Client
from django.urls import reverse
import requests
from unittest.mock import patch

# Test cases for the application
class WeatherAppTests(TestCase):
    def setUp(self):
        # Create a test client for sending requests
        self.client = Client()
        self.valid_city = "London"
        self.invalid_city = "InvalidCity"
        self.api_url = "https://api.openweathermap.org/data/2.5/weather"
        self.api_key = "91df26171e12a91e9dd20e6819b5ebeb"
    
    @patch('requests.get')  # Mock requests.get for testing without making actual API calls
    def test_get_weather_valid_city(self, mock_get):
        # Mock a successful API response
        mock_response = {
            "weather": [{"main": "Clear", "description": "clear sky", "icon": "01d"}],
            "main": {"temp": 25, "pressure": 1012, "humidity": 50},
            "wind": {"speed": 5},
            "sys": {"country": "GB"},
            "name": "London",
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Test the get_weather function
        from .views import get_weather
        response = get_weather(self.valid_city)
        self.assertIsNotNone(response)
        self.assertEqual(response['name'], "London")
        self.assertEqual(response['main']['temp'], 25)

    @patch('requests.get')
    def test_get_weather_invalid_city(self, mock_get):
        # Mock an unsuccessful API response
        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = None

        # Test the get_weather function with an invalid city
        from .views import get_weather
        response = get_weather(self.invalid_city)
        self.assertIsNone(response)

    def test_home_view_valid_city(self):
        # Test the home view with a valid city
        response = self.client.get(reverse('home'), {'city': self.valid_city})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        # Check if weather data is passed to the template context
        self.assertIn("temperature", response.context)
        self.assertIn("weather", response.context)

    def test_home_view_invalid_city(self):
        # Test the home view with an invalid city
        response = self.client.get(reverse('home'), {'city': self.invalid_city})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertNotIn("temperature", response.context)
        self.assertNotIn("weather", response.context)

    def test_home_view_no_city(self):
        # Test the home view with no city parameter
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertNotIn("temperature", response.context)
        self.assertNotIn("weather", response.context)
