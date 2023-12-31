import json

def parse_json(string):
    return json.loads(string)

def generate_json(data):
    return json.dumps(data)
