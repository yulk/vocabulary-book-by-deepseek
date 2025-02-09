import requests
import os

URL = "http://localhost:11434/api/generate"


headers = {
    "Content-Type": "application/json"
}

def call_ollama_generate(prompt, model="deepseek-r1:14b", system=None):

    payload = {
        "model": model,
        "stream": False,
        "prompt": prompt,
        "system": system,

    }
    
    response = requests.request("POST", URL, json=payload, headers=headers)
    return response.json()['response']


if __name__ == "__main__":
    response = call_ollama_generate("为什么天空是蓝的")
    print(response)
