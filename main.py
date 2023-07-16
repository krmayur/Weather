import requests
from datetime import datetime

# API key
API_KEY = "7bf056cbb952ccef3f74d37c6ac71d73"

def get_weather(city):
    # API URL
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    # Send GET request
    response = requests.get(URL)

    # Check the status of the request
    if response.status_code == 200:
        # Get data in json format
        data = response.json()
        main = data['main']
        # Get temperature, humidity and pressure
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        print(f"Temperature: {temperature-273}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report[0]['description']}")
    else:
        print("Error in the API request")

def main():
    city = input("Enter the city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()