import requests
import json

import schedule
import time

file = "fax.json"


try:
    with open(file, 'r') as f:
        fact_archive = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    fact_archive = []

def get_stuff():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    response = requests.get(url)
    response.raise_for_status()
    fact = response.json()
    return fact['text']

def do_thing():
    global fact_archive

    fact = get_stuff()
    while fact in fact_archive:
        fact = get_stuff()
    print(fact)
    fact_archive.append(fact)
    with open(file, 'w') as f:
        json.dump(fact_archive, f, indent=4)
    

if __name__ == "__main__":
    schedule.every(10).seconds.do(do_thing)
    while True:
        schedule.run_pending()
        time.sleep(1)
