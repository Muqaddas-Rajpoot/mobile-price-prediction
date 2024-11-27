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
blue= st.number_input("Bluetooth", min_value=0, max_value=1, step=1)
clock_speed = st.number_input("Clock speed", min_value=0.0, max_value=2.0, step=0.1)
dual_sim= st.number_input("DUAL SIM ", min_value=0, max_value=1, step=1)
fc= st.number_input("Front camera", min_value=0, max_value=19, step=1)
four_g= st.number_input("Four g", min_value=0, max_value=1, step=1)
int_memory = st.number_input("Internal Memory", min_value=2, max_value=64, step=10)
m_dep= st.number_input("mobile depth", min_value=0, max_value=1, step=1)
mobile_wt = st.number_input("Mobile Weight", min_value=80, max_value=200, step=10)
n_cores = st.number_input("No of cores", min_value=1, max_value=8, step=1)
px_height = st.number_input("Pixel Resolution Height", min_value=0, max_value=1960, step=100)
px_width = st.number_input("Pixel Resolution Width", min_value=500, max_value=1998, step=100)
ram = st.number_input("RAM (MB)", min_value=256, max_value=3998, step=256)
sc_h= st.number_input("Screen height", min_value=5, max_value=19, step=1)
sc_w= st.number_input("Screen width", min_value=5, max_value=18, step=1)
talk_time= st.number_input("Screen width", min_value=2, max_value=20, step=1)
three_g= st.number_input("Three g", min_value=0, max_value=1, step=1)
touch_screen= st.number_input("Touch screen", min_value=0, max_value=1, step=1)
wifi= st.number_input("Wifi", min_value=0, max_value=1, step=1)


# Define price categories
price_categories = {
    0: "Low-Priced",
    1: "Medium-Priced",
    2: "Expensive",
    3: "High-Expensive"
}

# Predict the price
if st.button("Predict Price"):
    # Adjust the input list according to your model's feature requirements
    input_features = np.array([[
        battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory,
        m_dep, mobile_wt, n_cores, px_height, px_width, ram, sc_h, sc_w,
        talk_time, three_g, touch_screen, wifi
    ]])

    # Perform prediction
    prediction = model.predict(input_features)

    # Map prediction to a price category
    price_category = price_categories.get(prediction[0], "Unknown")
    st.success(f"Predicted Price Category: {price_category}")


