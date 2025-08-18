from tkinter import *
import webbrowser
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent='RailwayMapCityToCoordinates')

def openMap():
    try: 
        location = geolocator.geocode(f"{cityEntry.get()} {stateEntry.get()}")
    except Exception:
        infoLabel.config(text="We could not load correctly. Please check your internet connection.")
        mainPageButton = Button(text="Open OpenRailway Map Main Page")
        mainPageButton.pack(side="bottom")
    try:
        latitude = location.latitude
        longitude = location.longitude
        link = (f"https://openrailwaymap.app/#view=12.17/{latitude}/{longitude}")
        webbrowser.open_new(link)
    except AttributeError:
        infoLabel.config(text="We could not find your city. Please make sure your spelling is correct.")
        latitude = 39.9527237
        longitude = -75.1635262
    except Exception:
        latitude = 39.9527237
        longitude = -75.1635262

window = Tk()
window.title("OpenRailwayMap City to Coordinates")
cityLabel = Label(text="City/Area: ")
cityLabel.pack()
cityEntry = Entry()
cityEntry.pack()
stateLabel = Label(text="State/Country")
stateLabel.pack()
stateEntry = Entry()
stateEntry.pack()
infoButton = Button(text="Open", command=openMap)
infoButton.pack()
infoLabel = Label(text="RailwayMap City to Coordinates by andrewsawesome \n github.com/andrewsawesome/OpenRailwayMapCityToCoordinates")
infoLabel.pack()


window.mainloop()
