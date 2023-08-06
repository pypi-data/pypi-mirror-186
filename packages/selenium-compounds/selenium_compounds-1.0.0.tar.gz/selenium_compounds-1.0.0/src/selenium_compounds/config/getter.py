import json

def get_value(value):
    with open("../config/gen_config.json") as f:
        data = json.load(f)
    print(data.get(value))
    return data.get(value)