import requests
import pprint
import dotenv
import os

dotenv.load_dotenv()

api_key  = os.getenv('API_KEY')
# print(api_key)
city_name = input("Enter city name: ")

data = dict()
# print(data)

api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
response = requests.get(url=api_url)

if response.status_code == 200:
    data = response.json()
    pprint.pprint(data)
else:
    print(f"{city_name} is an invalid city name")
