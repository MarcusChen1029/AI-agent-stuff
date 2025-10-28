import requests
import json
import os
file = "fax.json"
try:
    with open(file, 'r') as f:
        fact_archive = json.load(f)
except FileNotFoundError:
    fact_archive = []

def get_stuff():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    response = requests.get(url)

    response.raise_for_status()

    fact = response.json()
    return fact['text']

if __name__ == "__main__":
    fact = get_stuff()
    if fact not in fact_archive:
        fact_archive.append(fact)
        with open(file, 'w') as f:
            json.dump(fact_archive, f, indent=4)
    print(fact)
