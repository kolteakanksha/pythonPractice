import requests

name= input("What is the new name? ")
employee={"name": name}
headers={"Content-type": "application/json"}
resp = requests.post(f"https://reqres.in/api/users", json=employee, headers=headers )
info= resp.json()
print(info)
print(resp.status_code)
