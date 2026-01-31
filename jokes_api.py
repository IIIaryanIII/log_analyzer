import requests

jokes_url ="https://official-joke-api.appshot.com/random_joke"

def get_joke():
    joke = requests.get(url=jokes_url)
    print(joke.json())

get_joke()