import requests
import pprint
import dotenv
import os

dotenv.load_dotenv()

def request_data(city_name):
    '''
        Returns <b>true</b> if status code is less that 400( 2xx, 3xx) <br/>
        Else returns <b>false</b> for bad status code like 4xx, 5xx etc...
        '''
    api_key = os.getenv('API_KEY')
    try:
        global response
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}")
        
        if response.ok:
            return True
        else:
            # raise an exception for bad status code (eg: 4xx, 5xx)
            response.raise_for_status()
            return False
    
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occured {http_err}')
    except requests.exceptions.ConnectionError as conn_err:
        print(f'Connection error occured {conn_err}')
    except requests.exceptions.Timeout as timeout:
        print(f'Timeout error occured {timeout}')
    except requests.exceptions.RequestException as req_err:
        print(f'An error occured making request {req_err}')

def retrieve_data(city):
    if request_data(city_name=city):
        return response.json()


# print(api_key)
city_name = input("Enter city name: ")

data = retrieve_data(city_name)
pprint.pprint(data)
print(
f"""
\n\n
Your specific coordinates, latitude: {data['coord']['lat']} with longitute: {data['coord']['lon']} shows that...
you are currently in the {data['sys']['country']} inside the city {data['name']}.
The weather now is {data['weather'][0]['description']}.
The wind speed is {data['wind']['speed']}km/s at a degree of {data['wind']['deg']} C with a gust of {data['wind']['gust']}.
\n
Here are some information about where you are now:
Temperature: {data['main']['temp']}
Humidity: {data['main']['humidity']}
Pressure: {data['main']['pressure']}
Ground Level: {data['main']['grnd_level']}
Sea Level: {data['main']['sea_level']}
"""
)
