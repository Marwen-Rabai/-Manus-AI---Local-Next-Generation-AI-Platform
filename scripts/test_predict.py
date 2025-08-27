import requests
r = requests.post('http://127.0.0.1:5000/predict', json={'input':'hello world'})
print(r.status_code, r.text)
