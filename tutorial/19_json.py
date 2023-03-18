import json

#create string in the format of json file
x = '{"name" : "WGC575", "age" : 17, "Hometown" : "CHN"}'

#loads x as a dictionary from json
y = json.loads(x)

print(y["name"])

obj_py = {
    "name"  : "WGC575",
    "age"   : "17",
    "home"  : "CHN"
}

#dumps dictionary object into json
obj_js = json.dumps(obj_py)

print(obj_js)

#other containers like tuple, set could also be converted to json

