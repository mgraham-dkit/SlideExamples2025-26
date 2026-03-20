import json

with open("sample_single_object.json") as json_file:
    data = json.load(json_file)
    print(f"JSON data: {data}")
    print(f"Type of variable json object is read into: {type(data)}")

with open("sample_object_array.json") as json_file:
    data = json.load(json_file)
    print(f"JSON data: {data}")
    print(f"Type of variable json array is read into: {type(data)}")

# Working with JSON in a string
# JSON object
text_json_object = "{\"name\" :\"Hilary\", \"age\":45 }"
json_object = json.loads(text_json_object)
print(f"JSON data: {json_object}")
print(f"Type of variable json array is read into: {type(json_object)}")

# JSON array
text_json_object2 = "{\"name\" :\"Savannah\", \"age\":65 }"
text_json_object3 = "{\"name\" :\"Albert\", \"age\":78 }"
text_array = f"[{text_json_object}, {text_json_object2}, {text_json_object3}]"
json_array = json.loads(text_array)
print(f"JSON data: {json_array}")
print(f"Type of variable json array is read into: {type(json_array)}")