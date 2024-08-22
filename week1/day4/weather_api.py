import pyowm
import dotenv
import os

dotenv.load_dotenv()

api_key  = os.getenv('API_KEY')
owm = pyowm.OWM(api_key)

observation = owm.weather_manager().weather_at_place("Accra, gh")
w = observation.to_dict()
print(f"full data-> {w}")
print(f"\nfull weather forcast-> {w['weather']}")
print(f"\npressure-> {w['weather']['pressure']}")
print(f"\nwind-> {w['weather']['wind']}")
print(f"\ntemperture-> {w['weather']['temperature']}")