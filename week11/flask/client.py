import requests

r = requests.get("http://localhost:5000/hello")
print(r.text)

r = requests.get("http://localhost:5000/")
print(r.text)
