import pyowm


api_key  = "94c49b283dfb4005b739ebe1125eb833"
owm = pyowm.OWM(api_key)

observation = owm.weather_manager().weather_at_place("Accra, gh")
w = observation.to_dict()
print(f"full data-> {w}")
print(f"\nfull weather forcast-> {w['weather']}")
print(f"\npressure-> {w['weather']['pressure']}")
print(f"\nwind-> {w['weather']['wind']}")
print(f"\ntemperture-> {w['weather']['temperature']}")