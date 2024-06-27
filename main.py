import requests
import json

# Define proxies if needed (optional)
proxies = {'https': 'http://127.0.0.1:8888'}

# Function to make a request to oLLaMA with LLaMA 3 model
def request(prompt, url="http://localhost:8000/api/generate"):
    data = {
        "model": "llama3",
        "prompt": prompt
    }

    # A POST request to the API
    response = requests.post(url, json=data, proxies=proxies)

    # Split response by lines and parse each line as JSON
    print("<BraveMind>: ", end="")
    for line in response.iter_lines():
        if line:
            try:
                # Parse JSON from the line
                response_json = json.loads(line)

                # Extract and print the generated text
                generated_text = response_json.get('response', '')
                print(generated_text, end="")

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

# Initial message
print('''
 
   
     ___                              __ __   _           _
    | . >  _ _   ___   _ _   ___     |  \  \ <_> ._ _   _| |
    | . \ | '_> <_> | | | | / ._>    |     | | | | ' | / . |
    |___/ |_|   <___| |__/  \___.    |_|_|_| |_| |_|_| \___|
    6/27/2024 V.1.0
   
    <BraveMind's Secretary>: Your therapist is in an appointment and will be with you shortly...
   
    '''
)

# Start conversation loop
request(
    '''
    You are a therapist. Avoid replying with a list. Never reply with a list.
    '''
)

while True:
    print("\n")
    user_input = input("<User>: ")
    request(user_input)
