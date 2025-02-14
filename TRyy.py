import requests
import json  # JSON formatında düzgün çıktı almak için
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    url = "https://randomfox.ca/floof"
    response = requests.get(url)
    print(response.status_code)
    print(response.text)
    fox = response.json()
    print(fox["image"])
    return fox


url = "https://randomfox.ca/floof"
response = requests.get(url)
print(response.status_code)
print(response.text)
fox = response.json()
print(fox["image"])
