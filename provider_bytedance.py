import requests
import os

URL = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
MAX_TOKENS = 4096


"""
curl https://ark.cn-beijing.volces.com/api/v3/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ARK_API_KEY" \
  -d '{
    "model": "ep-20250226225639-lbdsg",
    "messages": [
      {"role": "system","content": "你是人工智能助手."},
      {"role": "user","content": "常见的十字花科植物有哪些？"}
    ]
  }'
"""

headers = {
    "Authorization": f"Bearer {os.environ['BYTEDANCE_API_KEY']}",
    "Content-Type": "application/json"
}

def call_bytedance_chat(prompt, system=None, format="text", model="ep-20250226225639-lbdsg"):
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
        #print(response.text)
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(e)
        return None

# env $(grep -v '^#' .env | xargs)  python3.8 provider_siliconflow.py
if __name__ == "__main__":
    print(os.environ['BYTEDANCE_API_KEY'])
    response = call_bytedance_chat("天空为什么是蓝色的,output JSON", system="You are a helpful assistant designed to output JSON.")
    print(response)
