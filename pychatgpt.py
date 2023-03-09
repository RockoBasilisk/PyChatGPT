#!/usr/bin/env python3
import os
import requests
import json

def ask2gpt(message):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('APIKEY')}"
    }
    data = {
        "engine": "davinci",
        "prompt": message,
        "temperature": 0.5,
        "max_tokens": 150
    }
    return requests.post(url, headers=headers, data=json.dumps(data))

def main():
    while True:
        message=str(input("( Send QUIT for exit ) Prompt: "))
        if message == "QUIT":
            break
        response = ask2gpt(message)
        print("ChatGPT: "+response.json()["error"]["message"] if "error" in response.json() else response.json()["choices"][0]["text"])

if __name__ == "__main__":
    main()
