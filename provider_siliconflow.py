import requests
import os

URL = "https://api.siliconflow.cn/v1/chat/completions"
MAX_TOKENS = 4096


headers = {
    "Authorization": f"Bearer {os.environ['SILICONFLOW_API_KEY']}",
    "Content-Type": "application/json"
}

def call_siliconflow_chat(prompt, system=None, format="text", model="deepseek-ai/DeepSeek-V3"):
    payload = {
        "model": model,
        "messages": [],
        "stream": False,
        "max_tokens": MAX_TOKENS,
        "stop": ["null"],
        "temperature": 0.7,
        "top_p": 0.7,
        "top_k": 50,
        "frequency_penalty": 0.5,
        "n": 1,
        "response_format": {"type": format},
    }

    if system is not None:
        payload["messages"].append({
            "role": "system",
            "content": system
        })
    payload["messages"].append({
        "role": "user",
        "content": prompt
    })

    try:
        response = requests.request("POST", URL, json=payload, headers=headers)
        print(response.text)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(e)
        return None

# env $(grep -v '^#' .env | xargs)  python3.8 provider_siliconflow.py
if __name__ == "__main__":
    print(os.environ['SILICONFLOW_API_KEY'])
    #response = call_siliconflow_chat("天空为什么是蓝色的")
    response = call_siliconflow_chat("天空为什么是蓝色的", system="You are a helpful assistant designed to output JSON.", format="json_object")
    print(response)
