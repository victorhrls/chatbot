# Local AI Chatbot with Ollama + Streamlit

A simple **chatbot running locally** with a LLaMA model using **Ollama** and a **Streamlit web interface**.  

It supports **chat history** and **streaming responses** like ChatGPT.

---

## Features

- Web chat interface with Streamlit  
- Local LLaMA model via Ollama  
- Keeps full conversation history  
- Streams responses **in real time**  
- Simple, beginner-friendly Python code  

---

## Architecture

user input -> streamlit interface -> python app logic -> ollama (llama model) -> assistant response -> streamlit displays the message


**Layers explained:**

1. **Interface (Streamlit)**  
   - Shows chat bubbles  
   - Collects user input  
   - Updates UI as AI replies  

2. **Application (Python)**  
   - Handles user input  
   - Stores chat history in `st.session_state.messages`  
   - Sends messages to the model  
   - Receives responses  

3. **Model (Ollama + LLaMA)**  
   - Runs locally  
   - Generates AI replies  
   - Supports streaming partial responses  

---

## How Streaming Works

- Each time the user sends a message, the **full chat history** is sent to Ollama.  
- The model generates the reply in **small chunks**.  
- In Python, we loop over these chunks:

```python
assistant_text = ""
placeholder = st.empty()

for chunk in ollama.chat(model="llama3", messages=messages, stream=True):
    text = chunk["message"]["content"]
    assistant_text += text
    placeholder.markdown(assistant_text)