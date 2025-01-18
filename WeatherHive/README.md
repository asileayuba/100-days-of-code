# Weather App

This is a simple Django-based weather application that retrieves current weather information from the OpenWeatherMap API. It allows users to search for a city and view the weather details such as temperature, humidity, wind speed, and weather conditions.

## Features

- **City-based weather search**: Allows users to enter a city name and get the current weather details.
- **Weather details displayed**: Displays weather, temperature, humidity, wind speed, pressure, and weather icon.
- **Responsive design**: Works on both desktop and mobile devices.
- **Weather icons**: Fetches and displays relevant weather icons based on the weather conditions.

## Technologies Used

- **Django**: A Python-based web framework used to build the web application.
- **OpenWeatherMap API**: Provides real-time weather data based on city search.
- **HTML/CSS**: For structuring and styling the frontend.
- **JavaScript**: For handling user input and updating the UI dynamically.

## Setup

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/asileayuba/100-days-of-code/tree/0ccbbf57a1ababaea2f252da7fe99cd276dc6270/WeatherHive
    ```

2. **Install dependencies**:
    Navigate to the project folder and install the required dependencies.
    ```bash
    cd weather-app
    pip install -r requirements.txt
    ```

3. **Set up the OpenWeatherMap API**:
    - Go to [OpenWeatherMap](https://openweathermap.org/) and create an account.
    - Obtain your free API key and replace it in the `get_weather` function in `views.py`.

4. **Run the development server**:
    ```bash
    python manage.py runserver
    ```
    Now you can open the application in your browser at `http://127.0.0.1:8000/`.

## Usage

1. Open the application in a browser.
2. Enter a city name in the search box.
3. Click the "Get Weather" button to view the weather details.

## Example Output

Upon entering a city, the application will display:
- Weather condition (e.g., Clear, Cloudy, Rainy)
- Description of the weather (e.g., light rain, few clouds)
- Current temperature
- Wind speed
- Humidity percentage
- Atmospheric pressure
- Relevant weather icon

## Acknowledgments

- Weather data provided by the [OpenWeatherMap API](https://openweathermap.org/).
- Code insights and inspiration from Tommy's Codebase: [YouTube Link](https://youtu.be/qaTRzyb3CLA?si=Ueak_cIdMnzrhKU5)
