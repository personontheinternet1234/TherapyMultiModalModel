import tensorflow as tf
import requests

# The API endpoint
url = "http://localhost:11434/api/generate"

# A GET request to the API
response = requests.get(url)

# Print the response
response_json = response.json()
print(response_json)

"""
{
"model": "tinyllama",
"prompt": "test"
}
"""