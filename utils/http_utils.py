import requests

def make_request(url, method, data):
    response = requests.request(method, url, data=data)
    return response.json()
