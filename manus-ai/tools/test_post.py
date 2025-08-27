import requests
import sys

url = "http://127.0.0.1:5000/predict"
try:
    r = requests.post(url, json={"input": "hello"}, timeout=5)
    print(r.status_code, r.text)
except Exception as e:
    print("Request failed:", e)
