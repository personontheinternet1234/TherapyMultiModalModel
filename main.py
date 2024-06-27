import requests
import json

# Define proxies if needed (optional)
proxies = {'https': 'http://127.0.0.1:8888'}


def request(prompt, url = "http://localhost:11434/api/generate"):
    data = {
    "model": "tinyllama",
    "prompt": prompt
}

    # A POST request to the API
    response = requests.post(url, json=data, proxies=proxies)

    # Split response by lines and parse each line as JSON
    print("<BraveMind>: ", end="", sep="")
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


print(
    ''' 
    
     ___                              __ __   _           _ 
    | . >  _ _   ___   _ _   ___     |  \  \ <_> ._ _   _| |
    | . \ | '_> <_> | | | | / ._>    |     | | | | ' | / . |
    |___/ |_|   <___| |__/  \___.    |_|_|_| |_| |_|_| \___|
    6/27/2024 V.1.0 
    
    <BraveMind's Secretary>: Your therapist is in an appointment and will be with you shortly...
    
    '''
)

request(
    '''
    Your task is to have real conversations with servicemembers about what might be on their mind. 
    ANSWER SUCCINCTLY, like a therapist would. Too much text in a single answer could scare the me.
    You can start by greeting me casually, and asking for their name.'''
)

while(True):
    print("\n")
    print("\n")
    user_input = input("<User>: ")
    request(user_input)