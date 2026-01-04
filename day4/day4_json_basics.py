import json

data = {
    "name": "Daniel",
    "goal": "become ai power user",
    "day": 4,
    "active": True,
}

# python -> json (string)
json_string = json.dumps(data, indent=2)
print(json_string)

#json -> python 
parsed = json.loads(json_string)
print (parsed["goal"])
print (parsed["day"])