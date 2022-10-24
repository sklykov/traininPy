"""Demo of a simple HTTP request."""

import requests

req = requests.get("https://swapi.dev/api/people/2/")
print("HTTP response code:", req.status_code)
if req.status_code == 200:
    person = req.json()
    for film in person['films']:
        req = requests.get(film)
        if req.status_code == 200:
            film = req.json()
            print(person['name'], "appeared in film:", film['title'])
