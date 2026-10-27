"""Optional smoke test. Start the server first, then run: python test_api.py"""
import json
import urllib.error
import urllib.request

BASE_URL = "http://127.0.0.1:5000"

def get(path):
    with urllib.request.urlopen(BASE_URL + path, timeout=10) as response:
        return response.status, response.read().decode("utf-8")

def post(path, payload):
    req = urllib.request.Request(
        BASE_URL + path,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.status, response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        return error.code, error.read().decode("utf-8")

print("GET /:", get("/"))
print("GET /health:", get("/health"))
print("POST /predict:", post("/predict", {
    "location": "Whitefield",
    "total_sqft": 1200,
    "bedrooms": 2,
    "bath": 2
}))
