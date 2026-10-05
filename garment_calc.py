import streamlit as st
st.title("Garment Calculator")

def calculate_production_time(quantity, minutes_per_garment, workers,efficency):
    total_minutes = quantity * minutes_per_garment
    theoretical_minutes = total_minutes / workers if workers > 0 else 0
    actual_minutes = theoretical_minutes / (efficency / 100)  # Assuming efficency is a percentage value
    hours = actual_minutes / 60
    return hours

st.title("Garment Production Time Predictor")
quantity = st.number_input("Enter the quantity of garments to be produced:", min_value=1, step=1)
minutes = st.number_input("Enter the minutes required to produce one garment:", min_value=0.1, step=0.1)
workers = st.number_input("Enter the number of workers available:", min_value=1, step=1)
efficency = st.number_input("Enter the efficiency of the workers (in percentage):", min_value=0.1, max_value=100.0)

if st.button("Calculate Production Time"):
    calculated_hours = calculate_production_time(quantity, minutes, workers, efficency)
    st.write(f"The estimated production time:", round(calculated_hours, 2), f"hours")