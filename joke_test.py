import requests
import json
print("Starting")
res = requests.get(
            'https://fungenerators.com/random/joke/',
                headers={"Accept":"application/json"})
print(str(res.json()['joke']))

print("Done")