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
    else:
        return "cant divide by zero"
def square():
    sqr1 = num1*num1
    sqr2 = num2*num2
    return sqr1, sqr2
def sqrt_():
    sqrt1 = math.sqrt(num1)
    sqrt2 = math.sqrt(num2)
    return sqrt1, sqrt2

col1, col2, col3, col4 = st.columns(4)

with col1:
    btn1 = st.button("+")
    btn2 = st.button("-")
    btn5 = st.button("Square")
with col2:
    btn3 = st.button("*")
    btn4 = st.button("/")
    btn6 = st.button("Sqrt")


if btn1:
    st.write("the sum of two numbers are: ", add())
elif btn2:
    st.write("the difference of two numbers are: ", subtract())
elif btn3:
    st.write("the multiplication of two numbers are: ", multiply())
elif btn4:
    st.write("the division of two numbers are: ", divide())
elif btn5:
    st.write(f"the Square of {num1} and {num2} are: ", square())
elif btn6:
    st.write(f"the Square root of {num1} and {num2} are: ", sqrt_())
else:
    st.write("No operation could be performed")
