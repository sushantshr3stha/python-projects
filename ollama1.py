import streamlit as st
import ollama

st.title("GreatSage")
st.write("I am a chatbot")

# Load the pre-trained OLAMA model
model = ollama.Olama("olama-base")

st.write("Please enter your thoughts:")

user_input = st.text_input("Enter your thoughts")

if user_input:
    # Send user's message to OLAMA
    response = model.generate(user_input)

    # Show OLAMA's response
    st.write("Assistant:", response)
