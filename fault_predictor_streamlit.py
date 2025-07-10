import streamlit as st
import joblib
import pandas as pd
from PIL import Image
import os

# ----------------------- Page Config ----------------------- #
st.set_page_config(
    page_title="Fault Prediction AI App",
    layout="centered",
    initial_sidebar_state="auto",
)

# ----------------------- Header and Branding ----------------------- #
st.image("images/gtu_logo.png", width=100)
st.image("images/intel_logo.png", width=100)
st.image("images/flavi_logo.png", width=120)

st.markdown("""
    <h2 style='text-align: center;'>Fault Prediction AI Model</h2>
    <h4 style='text-align: center;'>Based on Temperature and Vibration Data</h4>
    <p style='text-align: center;'>Developed in collaboration with Flavi Dairy Solutions India</p>
    <p style='text-align: center;'>Under Intel AI Digital Readiness Program by GTU</p>
    <hr style='border:1px solid #bbb;'>
""", unsafe_allow_html=True)

# ----------------------- Load Model ----------------------- #
model = joblib.load("fault_model.pkl")

# ----------------------- Machinery Dropdown ----------------------- #
st.subheader("🛠️ Select Machinery")
machine_options = {
    "Motor": "motor.png",
    "Milk Blender": "milk_blender.png",
    "Churning Machine": "churning_machine.png",
    "Packaging Unit": "packaging_unit.png"
}
selected_machine = st.selectbox("Choose the machine you want to monitor:", list(machine_options.keys()))
image_path = f"images/{machine_options[selected_machine]}"

if os.path.exists(image_path):
    st.image(image_path, caption=selected_machine, use_column_width=True)
else:
    st.warning("Image not found.")

# ----------------------- User Input ----------------------- #
st.subheader(":gear: Enter Sensor Values")
st.markdown("""
**Reference Ranges (Example):**  
- Vibration: 0.1 to 5.0 mm/s  
- Temperature: 30 to 100 °C  
- Pressure: 1.0 to 5.0 bar  
- RMS Vibration: 0.1 to 4.0  
- Mean Temperature: 35 to 90 °C
""")

vib = st.number_input("Vibration (mm/s)", min_value=0.0, max_value=10.0)
temp = st.number_input("Temperature (°C)", min_value=0.0, max_value=150.0)
press = st.number_input("Pressure (bar)", min_value=0.0, max_value=10.0)
rms_vib = st.number_input("RMS Vibration", min_value=0.0, max_value=10.0)
mean_temp = st.number_input("Mean Temperature (°C)", min_value=0.0, max_value=150.0)

# ----------------------- Prediction ----------------------- #
if st.button("Predict Fault"):
    input_df = pd.DataFrame([[vib, temp, press, rms_vib, mean_temp]],
                            columns=["Vibration", "Temperature", "Pressure", "RMS_Vibration", "Mean_Temp"])
    prediction = model.predict(input_df)[0]
    st.success(f"Prediction: {'⚠️ Fault Detected' if prediction == 1 else '✅ No Fault Detected'}")
