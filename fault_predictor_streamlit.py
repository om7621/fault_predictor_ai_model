import streamlit as st
import joblib
import pandas as pd

# Load Model
model = joblib.load("fault_model.pkl")

# --- Page Setup ---
st.set_page_config(page_title="Smart Fault Predictor", layout="centered")

# --- Title & Logos ---
st.markdown("""
    <h1 style='text-align: center; color: #1f77b4;'>Smart Fault Prediction System</h1>
    <h5 style='text-align: center;'>Developed under GTU × Intel × Flavi Dairy Collaboration</h5>
""", unsafe_allow_html=True)

logo_col1, logo_col2, logo_col3 = st.columns([1, 1, 1])
with logo_col1:
    st.image("images/gtu_logo.png", width=100)
with logo_col2:
    st.image("images/flavi_logo.png", width=100)
with logo_col3:
    st.image("images/intel_logo.png", width=100)

st.markdown("---")

# --- Machinery Selection ---
st.subheader("🛠️ Select Machinery")
machine_options = {
    "Motor": "motor.png",
    "Milk Blender": "milk_blender.png",
    "Churning Machine": "churning_machine.png",
    "Packaging Unit": "packaging_unit.png"
}
selected_machine = st.selectbox("Choose a machine", list(machine_options.keys()))

# Display machinery image centered
center_col = st.columns(3)[1]
with center_col:
    st.image(f"images/{machine_options[selected_machine]}", width=300)

st.markdown("---")

# --- Input Section ---
st.subheader("📥 Enter Sensor Data")
st.markdown("""
*Refer to the hint ranges for acceptable inputs.
""")

col1, col2 = st.columns(2)
with col1:
    vibration = st.number_input("Vibration (mm/s)", min_value=0.0, max_value=100.0, help="E.g., 0-50")
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=150.0, help="E.g., 25-100")
    pressure = st.number_input("Pressure (bar)", min_value=0.0, max_value=20.0, help="E.g., 0.5-10")
with col2:
    rms_vibration = st.number_input("RMS Vibration", min_value=0.0, max_value=100.0, help="E.g., 5-60")
    mean_temp = st.number_input("Mean Temp", min_value=0.0, max_value=150.0, help="E.g., 25-90")

# --- Predict ---
if st.button("🔍 Predict Fault"):
    input_data = pd.DataFrame.from_dict({
        'Vibration': [vibration],
        'Temperature': [temperature],
        'Pressure': [pressure],
        'RMS_Vibration': [rms_vibration],
        'Mean_Temp': [mean_temp],
    })

    try:
        prediction = model.predict(input_data)[0]
        st.success(f"🧠 Predicted Fault Label: {prediction}")
    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")

# --- Footer ---
st.markdown("---")
st.markdown("<center>Made with ❤️ for Dairy Industry Automation</center>", unsafe_allow_html=True)
