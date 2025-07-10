import streamlit as st
import joblib
import pandas as pd
from PIL import Image

# --------------------------- Page Config -----------------------------
st.set_page_config(page_title="Smart Dairy Fault Predictor", layout="wide")

# --------------------------- Splash Header -----------------------------
st.markdown("""
    <div style='text-align: center; padding: 20px 0;'>
        <h1 style='font-size: 3em; color: #0e4c92;'>Smart Fault Prediction System</h1>
        <p style='font-size: 1.2em; color: grey;'>Developed under GTU x Intel x Flavi Dairy Collaboration</p>
    </div>
""", unsafe_allow_html=True)

# --------------------------- Logo Row -----------------------------
col_logo1, col_logo2, col_logo3 = st.columns([1, 1, 1])
with col_logo1:
    st.image("images/gtu_logo.png", width=100)
with col_logo2:
    st.image("images/flavi_logo.png", width=100)
with col_logo3:
    st.image("images/intel_logo.png", width=100)

st.markdown("---")

# --------------------------- Machine Selector -----------------------------
st.subheader("🛠️ Select Machinery")
machine_images = {
    "Motor": "images/motor.png",
    "Milk Blender": "images/milk_blender.png",
    "Churning Machine": "images/churning_machine.png",
    "Packaging Unit": "images/packaging_unit.png"
}

machine = st.selectbox("Choose a machine", list(machine_images.keys()))
st.image(machine_images[machine], width=300, caption=f"Selected Machine: {machine}")

st.markdown("---")

# --------------------------- Input Section -----------------------------
st.markdown("### 📥 Sensor Data Entry")
col1, col2 = st.columns(2)
with col1:
    vibration = st.number_input("Vibration (mm/s)", 0.0, 10.0, step=0.1, help="Typical: 0.2 - 2.5")
    temperature = st.number_input("Temperature (°C)", 0.0, 100.0, step=0.5, help="Typical: 25 - 70")
    pressure = st.number_input("Pressure (bar)", 0.0, 10.0, step=0.1, help="Typical: 1 - 5")
with col2:
    rms_vibration = st.number_input("RMS Vibration", 0.0, 10.0, step=0.1, help="Typical: 0.1 - 1.5")
    mean_temp = st.number_input("Mean Temperature", 0.0, 100.0, step=0.5, help="Average running temp")

# --------------------------- Model Prediction -----------------------------
model = joblib.load("fault_model.pkl")

input_data = pd.DataFrame([{
    "Vibration": vibration,
    "Temperature": temperature,
    "Pressure": pressure,
    "RMS_Vibration": rms_vibration,
    "Mean_Temp": mean_temp,
    "Vib_Rolling_Mean": vibration,
    "Vib_Rolling_Std": 0.1,
    "Temp_Rolling_Mean": temperature,
    "Temp_Rolling_Std": 0.1,
    "Pressure_Rolling_Mean": pressure,
    "Pressure_Rolling_Std": 0.1
}])

if st.button("🔍 Predict Fault"):
    prediction = model.predict(input_data)[0]
    st.success(f"⚠️ Predicted Fault Label: {prediction}")

# --------------------------- Footer -----------------------------
st.markdown("""
    <hr>
    <div style='text-align: center;'>
        <small style='color: grey;'>Copyright © 2025 GTU x Intel x Flavi Dairy Solutions</small>
    </div>
""", unsafe_allow_html=True)
