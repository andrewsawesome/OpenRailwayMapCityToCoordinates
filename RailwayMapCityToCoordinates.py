import webbrowser
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='myapplication')
city = input("What city would you like to go to? ")
state = input("In what state/country (Full name or two-letter abbreviation)? ")
try:
    location = geolocator.geocode(f"{city} {state}")
except Exception:
    print("We could not load correctly. Please check your internet connection.")
try:
    latitude = location.latitude
    longitude = location.longitude
except AttributeError:
    print("We could not find your city. Please make sure your spelling is correct.")
    latitude = 39.9527237
    longitude = -75.1635262
except Exception:
    latitude = 39.9527237
    longitude = -75.1635262
print(latitude)
print(longitude)
link = (f"https://openrailwaymap.fly.dev/#view=12.17/{latitude}/{longitude}")
webbrowser.open_new(link)
