import streamlit as st
import ollama

st.title("Local AI Chatbot")

# initialize chat history
# session state is the memory of the app
if "messages" not in st.session_state:
    st.session_state.messages = []

# display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
        
#'''
#Messages are stored like this
#{
# "role": "user",
# "content": "Hello"
#}
#'''

# user input
user_message = st.chat_input("Ask something")

if user_message:

    # store user message
    st.session_state.messages.append(
        {"role": "user", 
         "content": user_message}
    )

    with st.chat_message("user"):
        st.write(user_message)

    # Ollama response
    assistant_message_placeholder = st.empty()
    
    assistant_text = '' # incremental text
    
    # Stream response from ollama
    stream = ollama.chat(
        model ='llama3',
        messages=st.session_state.messages,
        stream=True
    )
    
    for chunk in stream:
        text = chunk['message']['content']
        assistant_text +=text
        # Display current chunk
        assistant_message_placeholder.markdown(assistant_text)
   
   
   # store the assistant response in the history
    
    st.session_state.messages.append(
        {"role": "assistant", 
         "content": assistant_text}
    )

    # with st.chat_message("assistant"):
    #    st.write(assistant_response)