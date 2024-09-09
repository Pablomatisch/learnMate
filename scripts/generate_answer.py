import ollama


def generate(prompt):
    answer = ollama.generate(model="qwen2:1.5b", prompt=prompt)

    return answer['response']

def chat(prompt):
    answer = ollama.chat(model="qwen2:1.5b", messages=prompt)

    return answer['response']

def generatestream(prompt):
    stream = ollama.chat(
    model='qwen2:1.5b',
    messages=[{'role': 'user', 'content': prompt}],
    stream=True,
    )
    print("AI: ", end='')
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)
    print(" ")