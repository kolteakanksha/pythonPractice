import json

import requests

id= input("what is the id you want to update? ")
name= input("What is the new name? ")
employee={"name": name}
json.dumps()
headers={"Content-type": "application/json"}
resp = requests.post(f"https://reqres.in/api/users{id}", json=employee, headers=headers )
print(type(resp))
info= resp.json()
print(info)
print(resp.status_code)
