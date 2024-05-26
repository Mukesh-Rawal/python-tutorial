# Convert dictionary to json
import json
dict = {
    'name': 'Mukesh',
    'age': 33,
    'city': 'Noida'
}

to_json = json.dumps(dict)
print(type(to_json))

print(to_json)
js = to_json

new_dict = json.loads(js)
print(type(new_dict))
print(new_dict)