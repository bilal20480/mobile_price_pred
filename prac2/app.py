import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load("mobile_price_model.pkl")

# App title
st.title("Mobile Price Prediction")

# User inputs
st.sidebar.header("Enter Mobile Specifications:")
ram = st.sidebar.slider("RAM (GB)", min_value=2, max_value=12, step=1)
storage = st.sidebar.slider("Storage (GB)", min_value=16, max_value=256, step=16)
battery = st.sidebar.slider("Battery (mAh)", min_value=2000, max_value=6000, step=500)
camera = st.sidebar.slider("Camera (MP)", min_value=8, max_value=48, step=4)

# Predict button
if st.sidebar.button("Predict Price"):
    input_data = pd.DataFrame(
        [[ram, storage, battery, camera]],
        columns=["RAM (GB)", "Storage (GB)", "Battery (mAh)", "Camera (MP)"]
    )
    prediction = model.predict(input_data)[0]
    st.write(f"Predicted Price: ${prediction:.2f}")
