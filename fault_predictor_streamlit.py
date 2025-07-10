import streamlit as st
import joblib
import pandas as pd
from PIL import Image

# --------------------------- App Title -----------------------------
st.set_page_config(page_title="Smart Fault Predictor", layout="wide")

st.markdown("<h1 style='text-align: center;'>🧠 Smart Fault Prediction for Dairy Machinery</h1>", unsafe_allow_html=True)
st.markdown("---")

# --------------------------- Logo Row -----------------------------
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.image("images/gtu_logo.png", width=100)
with col2:
    st.image("images/flavi_logo.png", width=100)
with col3:
    st.image("images/intel_logo.png", width=100)

st.markdown("---")

# --------------------------- Machine Selection -----------------------------
st.subheader("🛠️ Select Machinery")

machine_images = {
    "Motor": "images/motor.png",
    "Milk Blender": "images/milk_blender.png",
    "Churning Machine": "images/churning_machine.png",
    "Packaging Unit": "images/packaging_unit.png"
}

machine = st.selectbox("Choose a machine", list(machine_images.keys()))

# Resize machine image to smaller width
st.image(machine_images[machine], width=300, caption=f"Selected Machine: {machine}")

# --------------------------- Input Section -----------------------------
st.markdown("### 📥 Enter Sensor Data")
st.info("🔢 Enter values based on sensor ranges (check right labels):")

col1, col2 = st.columns(2)

with col1:
    vibration = st.number_input("Vibration (mm/s)", min_value=0.0, max_value=10.0, step=0.1)
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=100.0, step=0.5)
    pressure = st.number_input("Pressure (bar)", min_value=0.0, max_value=10.0, step=0.1)

with col2:
    rms_vibration = st.number_input("RMS Vibration", min_value=0.0, max_value=10.0, step=0.1)
    mean_temp = st.number_input("Mean Temperature", min_value=0.0, max_value=100.0, step=0.5)

# --------------------------- Prediction Logic -----------------------------
model = joblib.load("fault_model.pkl")

input_df = pd.DataFrame([{
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
    prediction = model.predict(input_df)[0]
    st.success(f"⚙️ Predicted Fault Label: **{prediction}**")

# --------------------------- Footer -----------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: grey;'>Developed in collaboration with <b>GTU</b>, <b>Flavi Dairy Solutions</b> & <b>Intel AI for Manufacturing</b></p>",
    unsafe_allow_html=True
)
