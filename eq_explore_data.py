from pathlib import Path
import json
import plotly.express as px
#creates a path object that represents a file path
path = Path("eq_1_day_m1.geojson")
#stores the converted text into contents
#this uses a method of path object
contents = path.read_text(encoding = "utf-8")
#this converts a json formatted object into a python object
all_eq_data = json.loads(contents)
#stores the dictionary of earthquake features into the variable for convenience
all_eq_dicts = all_eq_data["features"]

#creates an empty list of magnitudes, longitudes and latitudes
magnitudes, longitudes, latitudes = [], [], []
#loops over each dictionary in the full list 
for eq_dict in all_eq_dicts:
    #each earthquake magnitude is stored in the properties section of the dict under the key "mag"
    #gets the magnitudes by using two keys to get the value
    mag = eq_dict["properties"]["mag"]
    #each longitude / latitude are stored under the key "geometry", and under coordinates
    #this dictionary geometry has a list in it
    #the first value [0] is the longitude while the second [1] is latitude
    longitude = eq_dict["geometry"]["coordinates"][0]
    latitude = eq_dict["geometry"]["coordinates"][1]
    #appends the magnitudes to the list
    magnitudes.append(mag)
    longitudes.append(longitude)
    latitudes.append(latitude)

title = "Global Earthquakes (1 Day)"
#keywords are important because scatter_geo takes a lot of methods
#these keywords help it identify what is what
fig = px.scatter_geo(lat = latitudes, lon = longitudes, title = title)
fig.show()