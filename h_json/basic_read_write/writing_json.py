import json

# Convert single dictionary to JSON
user_detail1 = {
    "name": "Helen",
    "age": 43
}
with open("dict_converted_to_json.json", "w") as file:
    json.dump(user_detail1, file, indent=4)

print(f"Dictionary converted to JSON: {json.dumps(user_detail1)}")

# Convert list of dictionaries to JSON
user_detail2 = {
    "name": "Anthony",
    "age": 29
}
user_detail3 = {
    "name": "Leslie",
    "age": 42
}

details = [user_detail1, user_detail2, user_detail3]
print(f"List of dictionaries converted to JSON: {json.dumps(details, indent=4)}")
