import streamlit as st

st.title('Local AI Chatbot')


user_message = st.chat_input('Ask something')

if user_message:
    
    with st.chat_message('user'):
        st.write(user_message)
    
    with st.chat_message('assistante'):
        st.write('This is where the AI response will appear')