# main.py

import requests
import json
from emotion import myFunc 

proxies = {'https': 'http://127.0.0.1:8888'}

def request(prompt, url="http://localhost:11434/api/generate", emotion=None):
    data = {
        "model": "llama3",
        "prompt": f"{prompt} Emotion detected: {emotion}" if emotion else prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=data, proxies=proxies)
        
        # Check if the request was successful
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return None

        # Check content type
        if 'application/json' not in response.headers.get('Content-Type', ''):
            print("Error: Response is not in JSON format")
            return None

        print("<BraveMind>: ", end="")
        for line in response.iter_lines():
            if line:
                try:
                    # Parse JSON from the line
                    response_json = json.loads(line.decode('utf-8'))
                    
                    # Extract and print the generated text
                    generated_text = response_json.get('response', '')
                    print(generated_text, end="")
                    return generated_text  # Return the generated text from the chatbot

                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

initial_prompt = '''
You are a therapist for soldiers suffering with PTSD, addiction, depression, etc. Reply in heartfelt messages and ask them about their issues. Always advance the conversation by asking questions to further the diagnosis. Make each response within 2 sentences, don't be too long and talk too much. Make the therapy session like a one-on-one session that's very conversational.
'''

if __name__ == "__main__":
    
    while True:
        user_input = input("<User>: ")

        detected_emotion = myFunc()

        response = request(initial_prompt, emotion=detected_emotion)
        
        print("\n")
        print(detected_emotion)
