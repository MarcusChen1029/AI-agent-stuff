import requests
import json

def get_stuff():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    response = requests.get(url)

    response.raise_for_status()

    fact = response.json()
    return fact['text']

if __name__ == "__main__":
    fact = get_stuff()
    print(fact)