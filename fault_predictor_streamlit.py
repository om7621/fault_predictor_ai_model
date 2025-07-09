import streamlit as st
import joblib
import numpy as np
import os

# ---------------------- Page Config ----------------------
st.set_page_config(
    page_title="Fault Predictor AI",
    layout="centered",
    page_icon="🔧"
)

# ---------------------- Branding -------------------------
st.image("images/gtu_logo.png", width=100)
st.image("images/intel_logo.png", width=100)
st.image("images/flavi_logo.png", width=150)

st.markdown("""
    <h2 style='text-align: center;'>Fault Prediction AI Model</h2>
    <h5 style='text-align: center;'>Based on Temperature & Vibration Data</h5>
    <h6 style='text-align: center;'>Project made under Intel AI Digital Readiness Program (GTU)</h6>
    <h6 style='text-align: center;'>In collaboration with Flavi Dairy Solutions India</h6>
    <hr style='border:1px solid #ccc'>
""", unsafe_allow_html=True)

# ---------------------- Machine Image Display -------------------------
machine_options = {
    "Motor": "motor.png",
    "Milk Blender": "milk_blender.png",
    "Churning Machine": "churning_machine.png",
    "Packaging Unit": "packaging_unit.png"
}

selected_machine = st.selectbox("Select Machine", list(machine_options.keys()))
image_path = f"images/{machine_options[selected_machine]}"

if os.path.exists(image_path):
    st.image(image_path, caption=selected_machine, use_column_width=True)
else:
    st.warning("Image not found. Please check your directory structure.")

# ---------------------- Input Fields -------------------------
st.subheader("📥 Enter Sensor Data")

col1, col2 = st.columns(2)

with col1:
    vibration = st.number_input("Vibration (mm/s)", min_value=0.0, value=5.0, step=0.1)
    rms_vibration = st.number_input("RMS Vibration", min_value=0.0, value=5.5, step=0.1)
    pressure = st.number_input("Pressure (bar)", min_value=0.0, value=1.0, step=0.1)

with col2:
    temperature = st.number_input("Temperature (°C)", min_value=0.0, value=30.0, step=0.5)
    mean_temp = st.number_input("Mean Temp", min_value=0.0, value=29.0, step=0.5)

# ---------------------- Prediction -------------------------
if st.button("🔍 Predict Fault"):
    try:
        model = joblib.load("fault_model.pkl")

        # Dummy rolling values, assumed from average ranges
        vib_roll_mean = vibration * 0.95
        vib_roll_std = 0.4
        temp_roll_mean = temperature * 0.97
        temp_roll_std = 0.5
        pressure_roll_mean = pressure * 0.96
        pressure_roll_std = 0.3

        input_data = np.array([
            vibration, temperature, pressure,
            rms_vibration, mean_temp,
            vib_roll_mean, vib_roll_std,
            temp_roll_mean, temp_roll_std,
            pressure_roll_mean, pressure_roll_std
        ]).reshape(1, -1)

        prediction = model.predict(input_data)[0]
        st.success(f"🧠 Predicted Fault Label: {prediction}")

    except Exception as e:
        st.error(f"❌ Error: {e}")

# ---------------------- Footer -------------------------
st.markdown("<hr><center>© 2025 Flavi Dairy Solutions | GTU | Intel</center>", unsafe_allow_html=True)
