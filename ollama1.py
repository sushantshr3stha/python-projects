
import streamlit as st
import ollama


# App title
st.title("GreatSage")
st.write("A simple local AI chatbot")


# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Show old messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# Get new message from user
user_message = st.chat_input("Ask me something...")


if user_message:

    # Show user's message
    with st.chat_message("user"):
        st.write(user_message)

    # Save user's message
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })


    # Get AI response
    with st.chat_message("assistant"):

        try:
            response = ollama.chat(
                model="llama3.2",
                messages=st.session_state.messages
            )

            answer = response["message"]["content"]

            # Show AI answer
            st.write(answer)

            # Save AI answer
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as error:
            st.error("Something went wrong!")
            st.write(error)

