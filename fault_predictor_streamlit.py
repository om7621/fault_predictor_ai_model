# 🔵 Header Title
st.markdown(
    "<h1 style='text-align: center; color: #1f77b4;'>Smart Fault Prediction System</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h5 style='text-align: center;'>Developed under GTU × Intel × Flavi Dairy Collaboration</h5>",
    unsafe_allow_html=True
)

# 🔶 Centered Logos in a single row
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.image("images/gtu_logo.png", width=100)
with col2:
    st.image("images/flavi_logo.png", width=100)
with col3:
    st.image("images/intel_logo.png", width=100)

st.markdown("---")  # Horizontal line

# 🛠️ Machinery Selection
st.subheader("🛠️ Select Machinery")
machine_options = {
    "Motor": "motor.png",
    "Milk Blender": "milk_blender.png",
    "Churning Machine": "churning_machine.png",
    "Packaging Unit": "packaging_unit.png"
}

selected_machine = st.selectbox("Choose a machine", list(machine_options.keys()))

# 🖼️ Center Machinery Image
machine_image_path = f"images/{machine_options[selected_machine]}"
center_col = st.columns(3)[1]  # Middle column
with center_col:
    st.image(machine_image_path, width=300)
