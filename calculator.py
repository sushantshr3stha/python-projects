import math
import operator
import random
import streamlit as st



st.title("Calculator")

st.write("This is a simple calculator app built with Streamlit.")

num1 = float(st.number_input("Enter the first number:"))
num2 = float(st.number_input("Enter the second number:"))

def add():
    return num1 + num2

def subtract():
    return num1 - num2

def multiply():
    return num1 * num2

def divide():
    if num2 != 0:
        return num1/num2


col1, col2, col3, col4 = st.columns(4)

with col1:
    btn1 = st.write("+")
    btn2 = st.write("-")
with col2:
    btn3 = st.write("*")
    btn4 = st.write("/")

if btn1:
    st.write("the sum of two numbers are: ", add())
