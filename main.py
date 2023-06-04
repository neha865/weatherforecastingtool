# importing requests and json
import requests
import json
# base URL
CITY = input("enter your City?")
API_KEY = "326adc4e33990675f692de82b399ace2"
# updating the URL
URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
    # getting data in the json format
    data = response.json()
    # getting the main dict block
    main = data['main']
    # getting temperature
    temperature = main['temp']
    # getting the humidity
    humidity = main['humidity']
    # getting the pressure
    pressure = main['pressure']
    # weather report
    report = data['weather']
    print(f"{CITY:-^30}")
    print(f"Temperature: {temperature}")
    print(f"Humidity: {humidity}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {report[0]['description']}")
else:
    # showing the error message
    print("Error in the HTTP request")
