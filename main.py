import requests

proxies = {'https': 'http://127.0.0.1:8888'}

# Data
data = {
    "model": "tinyllama",
    "prompt": "why is the sky blue"
}

# The API endpoint
url = "http://localhost:11434/api/generate"

# A POST request to the API
response = requests.post(url, json=data)

# Check if the response is JSON
if 'application/json' in response.headers.get('Content-Type', ''):
    try:
        # Parse the response to JSON
        response_json = response.json()
       
        # Extract and print the generated text
        # Assuming the generated text is in the 'text' field of the JSON response
        generated_text = response_json.get('text', '')
        print("Here is the response to your prompt:")
        print(generated_text)
    except requests.exceptions.JSONDecodeError as e:
        print("Error decoding JSON:", e)
else:
    # Handle non-JSON response
    print("The response was not in JSON format. Here is the raw response text:")
    print(response.text)

