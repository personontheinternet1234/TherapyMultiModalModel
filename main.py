# import tensorflow as tf
import requests

proxies = {'https': 'http://127.0.0.1:8888'}

# Data
data = {
    "model": "tinyllama",
    "prompt": "why is the sky blue"
}

# The API endpoint
url = "http://localhost:11434/api/generate"

# A POST request to tthe API
response = requests.post(url, json=data)

# Print the response
print(response)
response_content = response.content
print(response_content)
response_text = response.text
print(response_text)

