from pathlib import Path
import json
import plotly.express as px
#creates a path object that represents a file path
path = Path("eq_30_day_mag.geojson")
#stores the converted text into contents
#this uses a method of path object
contents = path.read_text(encoding = "utf-8")
#this converts a json formatted object into a python object
all_eq_data = json.loads(contents)
#stores the dictionary of earthquake features into the variable for convenience
all_eq_dicts = all_eq_data["features"]

#loops over each dictionary in the full list 
#each earthquake magnitude is stored in the properties section of the dict under the key "mag"
#gets the magnitudes by using two keys to get the value
#each longitude / latitude are stored under the key "geometry", and under coordinates
#this dictionary geometry has a list in it
#the first value [0] is the longitude while the second [1] is latitude
#valid_values uses list comprenhension to loop through all dictionaries and only add it to the list if the magnitude is > 0 and exists
valid_values = [eq_dict for eq_dict in all_eq_dicts if eq_dict["properties"]["mag"] is not None and eq_dict["properties"]["mag"] > 0]
#stores the key values using list comprenhension by looking through our new list of valid values
magnitudes = [eq_dict["properties"]["mag"] for eq_dict in valid_values ]
longitudes = [eq_dict["geometry"]["coordinates"][0] for eq_dict in valid_values]
latitudes = [eq_dict["geometry"]["coordinates"][1] for eq_dict in valid_values]
eq_titles = [eq_dict["properties"]["title"] for eq_dict in valid_values]
title = "Global Earthquakes (30 Days)"
#keywords are important because scatter_geo takes a lot of methods
#these keywords help it identify what is what
fig = px.scatter_geo(lat = latitudes, lon = longitudes, size = magnitudes, title = title, 
    #use values in magnitude to determine the color of each marker on map
    color = magnitudes, 
    #color_continous_scale tells python which color scale to use
    color_continuous_scale = "Spectral",
    #labels takes a dictionary as a value
    #renames the legend from the default "color" to "magnitude"
    labels = {"color" : "Magnitude"},
    #natural earth projection will round the end of the map
    projection = "natural earth", 
    #we pass eq_titles to the hover_name argument and plotly now adds the name of the earthquake to hover points
    hover_name = eq_titles,
    )                                                                                                                                                                                                                                                                                                                                                                                                                                                            
fig.show()
#this gives us the list of different colorscales we can use
#import plotly.express as px
#px.colors.named_colorscales()