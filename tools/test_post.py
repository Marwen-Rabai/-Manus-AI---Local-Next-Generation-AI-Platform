import requests
r = requests.post('http://127.0.0.1:5000/predict', json={'input':'hello'})
print(r.status_code, r.json())
