def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def external_api_data():
    import requests
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return response.json()

