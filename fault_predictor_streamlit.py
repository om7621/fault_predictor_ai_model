import streamlit as st
import joblib
import numpy as np
from PIL import Image

# Load model
model = joblib.load("fault_model.pkl")

# Set page config
st.set_page_config(
    page_title="AI Fault Predictor - Flavi Dairy Solutions",
    page_icon="🧠",
    layout="wide"
)

# Load logos
col1, col2, col3 = st.columns(3)
with col1:
    st.image("gtu_logo.png", width=150)
with col2:
    st.image("flavi_logo.png", width=180)
with col3:
    st.image("intel_logo.png", width=150)

# Header
st.markdown("""
    <h1 style='text-align: center; color: #2c3e50;'>Fault Prediction AI Application</h1>
    <h4 style='text-align: center; color: gray;'>Developed under Intel AI Digital Readiness Program in collaboration with Flavi Dairy Solutions and GTU</h4>
    <hr style='border: 1px solid #ccc;'>
""", unsafe_allow_html=True)

# Sidebar - Machinery selection
machinery = st.sidebar.selectbox("Select Machinery", ["Motor", "Milk Blender", "Churning Machine", "Packaging Unit"])

# Info for selected machine
machinery_info = {
    "Motor": "Enter real-time motor data including temperature, vibration, and pressure.",
    "Milk Blender": "Provide sensor readings for blender operation.",
    "Churning Machine": "Churning systems involve critical rotating components; monitor vibration and temperature.",
    "Packaging Unit": "Focus on conveyor and sealing unit sensor data."
}
st.sidebar.markdown(f"**🛠 Info:** {machinery_info[machinery]}")

# Machinery images
machinery_images = {
    "Motor": "motor.png",
    "Milk Blender": "milk_blender.png",
    "Churning Machine": "churning_machine.png",
    "Packaging Unit": "packaging_unit.png"
}

st.markdown(f"""
    <div style='text-align: center;'>
        <img src='{machinery_images[machinery]}' width='400' style='border:1px solid #ddd; border-radius:10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);'>
        <p style='color:gray'><b>{machinery}</b></p>
    </div>
""", unsafe_allow_html=True)

# Input fields
st.markdown(f"### Enter Sensor Data for: {machinery}")
st.info("Refer to typical range: Vibration (0.1–1.0 mm/s), Temp (60–120 °C), Pressure (7–10 bar)")

col1, col2, col3 = st.columns(3)

with col1:
    vibration = st.number_input("Vibration (mm/s)", min_value=0.0, max_value=5.0, value=0.5)
with col2:
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=200.0, value=90.0)
with col3:
    pressure = st.number_input("Pressure (bar)", min_value=0.0, max_value=15.0, value=8.0)

col4, col5 = st.columns(2)
with col4:
    rms_vib = st.number_input("RMS Vibration", min_value=0.0, max_value=5.0, value=0.6)
with col5:
    mean_temp = st.number_input("Mean Temp", min_value=0.0, max_value=200.0, value=90.0)

# Predict
if st.button("🔍 Predict Fault"):
    input_data = np.array([[vibration, temperature, pressure, rms_vib, mean_temp]])
    prediction = model.predict(input_data)[0]
    label_map = {0: "No Fault", 1: "Minor Fault", 2: "Critical Fault"}
    st.success(f"Prediction Result: **{label_map[prediction]}**")

    if prediction == 2:
        st.error("⚠ Critical issue detected! Immediate inspection recommended.")
    elif prediction == 1:
        st.warning("Minor irregularity. Schedule maintenance soon.")
    else:
        st.balloons()
        st.info("System is working normally.")

# Footer
st.markdown("""
    <hr>
    <p style='text-align: center; color: gray;'>© 2025 Flavi Dairy Solutions | Developed with ❤️ by Om Singh</p>
""", unsafe_allow_html=True)
