import streamlit as st
import pickle
import numpy as np

# Load the saved model
with open("mobile_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Define the app
st.title("Mobile Phone Price Predictor")
st.write("Enter the features of the mobile phone:")

# Define input fields
battery_power = st.number_input("Battery Power (mAh)", min_value=500, max_value=6000, step=100)
ram = st.number_input("RAM (MB)", min_value=256, max_value=8000, step=256)
internal_memory = st.number_input("Internal Memory (GB)", min_value=4, max_value=512, step=1)
px_height = st.number_input("Pixel Height", min_value=0, max_value=3000, step=1)
px_width = st.number_input("Pixel Width", min_value=0, max_value=3000, step=1)

# Add more input fields as per your model

# Predict the price
if st.button("Predict Price"):
    # Adjust the input list according to your model's feature requirements
    input_features = np.array([[battery_power, ram, internal_memory, px_height, px_width]])
    prediction = model.predict(input_features)
    st.success(f"Predicted Price: ₹{prediction[0]:,.2f}")
