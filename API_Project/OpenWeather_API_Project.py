# DSC 510
# Week 12
# Programming Assignment Week 12 - Final project assignment to pull details from the openweather api.
# Shadin Chatila
# 2/25/2024

import requests
from requests.exceptions import RequestException

#Class to contain the weather data and its methods.
class WeatherData:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather_data(self, location_type, location, unit, state=None):
        geo_url = ''

        # Construct the URL based on location type
        if location_type == "city":
            geo_url = f'http://api.openweathermap.org/geo/1.0/direct?q={location}&state={state}&limit=1&appid={self.api_key}'
        elif location_type == "zip":
            if len(location) == 5 and location.isdigit():
                country_code = 'US'
                geo_url = f'http://api.openweathermap.org/geo/1.0/zip?zip={location},{country_code}&appid={self.api_key}'
            else:
                raise ValueError("Invalid zip code format. Please enter a 5-digit numeric code.")

        # Check if geo_url is valid
        if not geo_url:
            raise ValueError("Invalid location type. Please enter 'city' or 'zip'.")

        try:
            # Make the API request to get geographic data
            response = requests.get(geo_url)
            response.raise_for_status()
        except RequestException as e:
            print("Error making API request:", e)
            return None

        if response.status_code == 200:
            data = response.json()
            if not data:
                print("No location found.")
                return None

            if location_type == 'city':
                latitude = data[0]["lat"]
                longitude = data[0]["lon"]
            elif location_type == 'zip':
                latitude = data['lat']
                longitude = data['lon']

            # Set the unit parameter for weather data
            unit_param = 'metric' if unit == 'C' else 'imperial' if unit == 'F' else 'standard'
            weather_api_url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={self.api_key}&units={unit_param}"

            try:
                # Make the API request to get weather data
                weather_response = requests.get(weather_api_url)
                weather_response.raise_for_status()
            except RequestException as e:
                print("Error fetching weather data:", e)
                return None

            weather_json = weather_response.json()
            return weather_json

    def display_weather(self, weather_json, unit):
        # Display weather details based on unit
        if unit == 'C':
            print(f"\nCurrent Weather Conditions For {weather_json['name']}")
            print(f"Current Temp: {weather_json['main']['temp']}°C")
            print(f"High Temp: {weather_json['main']['temp_max']}°C")
            print(f"Low Temp: {weather_json['main']['temp_min']}°C")
            print(f"Pressure: {weather_json['main']['pressure']}hPa")
            print(f"Humidity: {weather_json['main']['humidity']}%")
            print(f"Description: {weather_json['weather'][0]['description'].capitalize()}")
        elif unit == 'F':
            print(f"\nCurrent Weather Conditions For {weather_json['name']}")
            print(f"Current Temp: {weather_json['main']['temp']}°F")
            print(f"High Temp: {weather_json['main']['temp_max']}°F")
            print(f"Low Temp: {weather_json['main']['temp_min']}°F")
            print(f"Pressure: {weather_json['main']['pressure']}hPa")
            print(f"Humidity: {weather_json['main']['humidity']}%")
            print(f"Description: {weather_json['weather'][0]['description'].capitalize()}")
        else:
            print(f"\nCurrent Weather Conditions For {weather_json['name']}")
            print(f"Current Temp: {weather_json['main']['temp']}°K")
            print(f"High Temp: {weather_json['main']['temp_max']}°K")
            print(f"Low Temp: {weather_json['main']['temp_min']}°K")
            print(f"Pressure: {weather_json['main']['pressure']}hPa")
            print(f"Humidity: {weather_json['main']['humidity']}%")
            print(f"Description: {weather_json['weather'][0]['description'].capitalize()}")

    def get_api_key(self):
        return self.api_key

    def set_api_key(self, api_key):
        self.api_key = api_key

def main():
    #Set the api key
    api_key = "9f324d5cbd880a50957acfc6276131c2"

    weather_data = WeatherData(api_key)

    while True:
        try:
            # Prompt user for location type
            while True:
                location_type = input("Enter location type (city or zip): ").lower()
                if location_type in ['city', 'zip']:
                    break
                else:
                    print("Invalid location type. Please enter 'city' or 'zip'.")

            # Prompt user for location
            while True:
                location = input("Enter location: ")
                if location:
                    break
                else:
                    print("Location cannot be empty.")

            # Prompt user for state if location type is city
            state = ''

            if location_type == 'city':
                while True:
                    state = input("Enter the state abbreviation (e.g., TX, NE): ").upper()
                    if len(state) == 2 and state.isalpha():
                        break
                    else:
                        print("Invalid state abbreviation. Please enter a 2-letter abbreviation (e.g., TX, NE).")

            # Validate ZIP code if location type is zip
            if location_type == 'zip':
                while True:
                    if location.isdigit():
                        break
                    else:
                        print("ZIP code must contain only numeric characters.")
                        location = input("Enter location: ")

            # Prompt user for preferred unit
            while True:
                unit = input("Enter preferred unit (C for Celsius, F for Fahrenheit or any key for Kelvin): ").upper()
                if unit in ['C', 'F', 'K']:
                    break
                else:
                    print("Invalid unit. Please enter 'C' for Celsius, 'F' for Fahrenheit, or any key for Kelvin.")

            # Make a call to the class to capture the details
            weather_json = weather_data.get_weather_data(location_type, location, unit, state)

            # Call method to display the weather data
            weather_data.display_weather(weather_json,unit)

        except Exception as e:
            print("An unexpected error occurred:", e)

        # Allow user to go again if they want to
        choice = input(
            "Do you want to check another location? (Enter 'Y' to continue, any other key to exit): ").lower()
        if choice != "y":
            break

    print("Exiting the program now...")

if __name__ == "__main__":
    main()
