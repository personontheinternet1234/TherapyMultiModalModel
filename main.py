import requests
import json

# Define proxies if needed (optional)
proxies = {'https': 'http://127.0.0.1:8888'}

# Data to be sent in the POST request
data = {
    "model": "tinyllama",
    "prompt": "You are a licensed therapist, and will COMMUNICATE ONE-ON-ONE very personally to the messages you receive. Furthermore, you're helping veterans or active duty service members as much as you can with mental health, addiction, PTSD, marital issues. Please begin by describing your purpose."
}

# The API endpoint
url = "http://localhost:11434/api/generate"

# A POST request to the API
response = requests.post(url, json=data, proxies=proxies)

# Split response by lines and parse each line as JSON
for line in response.iter_lines():
    if line:
        try:
            # Parse JSON from the line
            response_json = json.loads(line)

            # Extract and print the generated text
            generated_text = response_json.get('response', '')
            print(generated_text, sep="", end="")

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
