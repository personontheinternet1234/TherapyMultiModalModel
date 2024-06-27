import tensorflow as tf
import requests

proxies = {'https': 'http://127.0.0.1:8888'}

# The API endpoint
url = "http://localhost:11434/api/generate"

# A GET request to the API
response = requests.get(url, verify=False, proxies=proxies)

# Print the response
response_json = response.json()
print(response_json)

"""
{
"model": "tinyllama",
"prompt": "test"
}
"""