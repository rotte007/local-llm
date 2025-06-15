import requests

def query_ollama(prompt, model="gemma3:1b"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload, stream=True)
    response.raise_for_status()
    output = ""
    for line in response.iter_lines():
        if line:
            data = line.decode("utf-8")
            if data.startswith('{'):
                import json
                chunk = json.loads(data)
                output += chunk.get("response", "")
    return output

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    result = query_ollama(prompt)
    print("\nModel response:\n", result)