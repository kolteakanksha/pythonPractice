import requests


id = input("which ID you want to delete?")
resp = requests.delete(f"https://reqres.in/api/users/{id}")
info = resp.json()
print(info)
print(resp.status_code)
