import random
import streamlit as st

choices = ["rock", "paper", "scissors"]
bot_choice = random.choice(choices)

st.title("ROCK PAPER SCISSORS")
col1, col2, col3 = st.columns(3)

with col1:
    btn1=st.button("Rock")
with col2:
    btn2=st.button("Paper")
with col3:
    btn3=st.button("Scissors")

def user_choices():
    if btn1:
        return "rock"
    elif btn2:
        return "paper"
    elif btn3:
        return "scissors"
    else:
        st.write("Choose rock paper scissors")

choice = user_choices()

def game_logic():
    if bot_choice == choice:
       st.title("Draw")
       st.write(f"Bot: {bot_choice}")
       st.write(f"User: {choice}")
    elif bot_choice == "paper" and choice == "scissors":
       st.title("User won")
       st.write(f"Bot: {bot_choice}")
       st.write(f"User: {choice}")
    elif bot_choice == "paper" and choice == "rock":
        st.title("Bot won")
        st.write(f"Bot: {bot_choice}")
        st.write(f"User: {choice}")
    elif bot_choice == "scissors" and choice == "paper":
        st.title("Bot won")
        st.write(f"Bot: {bot_choice}")
        st.write(f"User: {choice}")
    elif bot_choice == "rock" and choice == "paper":
        st.title("User won")
        st.write(f"Bot: {bot_choice}")
        st.write(f"User: {choice}")
    elif bot_choice == "scissors" and choice == "rock":
        st.title("Bot won")
        st.write(f"Bot: {bot_choice}")
        st.write(f"User: {choice}")
    elif bot_choice == "rock" and choice == "scissors":
        st.title("Bot won")
        st.write(f"Bot: {bot_choice}")
        st.write(f"User: {choice}")
    else:
        st.title("Rock Paper Scissors")

game_logic()