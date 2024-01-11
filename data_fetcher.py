import requests

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    return response.json()["title"]