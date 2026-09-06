from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(
    page_title="⎊ Friday",
    page_icon="⎚-⎚",
    layout="centered"
)

st.title("Generative AI Chatbot")

#intitiate chat history 

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#show the chat history 
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


#llm initalizing
llm = ChatGroq(
    model= "qwen/qwen3.8-27b",
    temperature=0.2
)

#input box 
user_prompt = st.chat_input("Ask chatbot..")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user", "content":user_prompt})

    response = llm.invoke(
        input= [{"role":"system","content":'You are a helpful assistant. Be concise and accurate'},*st.session_state.chat_history]

    )
    assistant_response = response.content 
    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)