import requests

api_key  = "94c49b283dfb4005b739ebe1125eb833"
city_name = "Accra"
data = dict()
print(data)

api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
response = requests.get(url=api_url)

if response.status_code == 200:
    data = response.json()


print(data)
