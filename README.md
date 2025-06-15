# local-llm

## Ollama

- CLI & daemon for managing local LLMs  
- `ollama pull <model>`, `ollama run <model>`  
- OpenAI-compatible REST API (`http://localhost:11434`)  
- Built-in support for tool-calling & multimodal inputs  

---

## Alternatives to Ollama

- **Hugging Face + Transformers/Accelerate**  
- **llama.cpp** (CPU-only, GGML)  
- **GPT4All** / **MLC-LLM** / **text-generation-webui**  
- **Hugging Face Text Generation Inference** server  

---

## Guide – Step 1  

**Install Ollama**  

```bash
# macOS (Homebrew)
brew install ollama

# Linux
curl https://ollama.com/install.sh | sh
```

Or directly download from https://ollama.com/download

---

## Guide – Step 2

**Download a model with Ollama**

```bash
# e.g. gemma3:1b
ollama run gemma3:1b
```

---

## Guide – Step 3

**Test API integration with cURL**

```bash
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt":"Why is the sky blue?",
  "stream": false 
}'
```

---

## Guide – Step 4

in terminal, run
py try_local_llm.py

---

## Guide – Step 5

**Build a UI to interact with**

```bash
pip install streamlit

streamlit run chat_app.py

8501 is default, if having issues run

streamlit run chat_app.py --server.port 8502
```

---
