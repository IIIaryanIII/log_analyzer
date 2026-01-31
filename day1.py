import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url=url)

for key, value in response.json().items():
    if key == "completed":
        if value == False:
            print("The data is not completed in Server")