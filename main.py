# import tensorflow as tf
import requests

proxies = {'https': 'http://127.0.0.1:8888'}

payload = {
"model": "tinyllama",
"prompt": "test"
}

# The API endpoint
url = "http://localhost:11434/api/generate"

# A GET request to the API
response = requests.get(url, params=payload)

# Print the response
response_json = response
# print(response_json)