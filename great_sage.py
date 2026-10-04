
import streamlit as st
import google.generativeai as genai

st.title("GreatSage")
st.write("I am a chatbot")

genai.configure("api_key")

model = genai.GenerativeModel("gemini-3.8-flash")

user_input = st.chat_input("Enter your thoughts")

if user_input:
    # Show user's message
    st.chat_message("user").write(user_input)

    # Send user's message to Gemini
    response = model.generate_content(user_input)

    # Show Gemini's response
    st.chat_message("assistant").write(response.text)