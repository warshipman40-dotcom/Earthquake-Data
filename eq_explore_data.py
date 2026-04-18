from pathlib import Path
import json

#creates a path object that represents a file path
path = Path("eq_1_day_m1.geojson")
#stores the converted text into contents
#this uses a method of path object
contents = path.read_text(encoding = "utf-8")
#this converts a json formatted object into a python object
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))