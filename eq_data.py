from pathlib import Path
import json
#we will reformat the file so it is easier for us to read
#Read the data as a string
#path is the reference that points to the file
path = Path("eq_1_day_m1.geojson")
#tells python the encoding is utf-8 
contents = path.read_text(encoding = "utf-8")
#converts this to a python object and assigns it to all_eq_data
all_eq_data = json.loads(contents)
#creates a new path for a new file
path = Path("read_eq_data.geojson")
#you can use either path or with open() as file:
#converts the object back to JSON text
readable_contents  = json.dumps(all_eq_data, indent = 4)
#writes the formatted file back to the file
path.write_text(readable_contents)