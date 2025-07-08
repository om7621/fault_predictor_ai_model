import streamlit as st
import joblib
import numpy as np
from PIL import Image

# Load model
model = joblib.load('fault_model.pkl')

# Set page config
st.set_page_config(page_title="Fault Predictor AI", layout="centered")

# Load logos
st.image("flavi_logo.png", width=150)
st.image("intel_logo.png", width=100)
st.image("gtu_logo.png", width=100)

st.title("🚨 Fault Prediction AI System")
st.subheader("Based on Temperature and Vibration Data")
st.markdown("**Developed in collaboration with Flavi Dairy Solutions India under Intel AI Digital Readiness Program (GTU)**")

st.divider()

# Input Fields
st.header("🔧 Input Sensor Data")

vib = st.number_input("Vibration (mm/s)", min_value=0.0)
temp = st.number_input("Temperature (°C)", min_value=0.0)
pressure = st.number_input("Pressure (bar)", min_value=0.0)
rms = st.number_input("RMS Vibration", min_value=0.0)
mean_temp = st.number_input("Mean Temp", min_value=0.0)

if st.button("Predict Fault Type"):
    input_data = np.array([[vib, temp, pressure, rms, mean_temp]])
    prediction = model.predict(input_data)[0]

    st.success(f"🧠 Predicted Fault Type: **{prediction}**")
    if prediction == 0:
        st.info("✅ No Fault")
    elif prediction == 1:
        st.warning("⚠️ Minor Fault Detected")
    else:
        st.error("❌ Major Fault Detected")

