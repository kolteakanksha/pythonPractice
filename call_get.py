import requests

inp= input("what is your ID?")
resp = requests.get(f"https://reqres.in/api/users/{inp}")
info= resp.json()
print(info)
print(resp.status_code)


# resp = requests.get(f"https://reqres.in/api/users")
# info= resp.json()
# print(info)
# print(resp.status_code)