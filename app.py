import streamlit as st
import pickle
import numpy as np

# Load the saved model
with open("mobile_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f8f9fa;
        font-family: Arial, sans-serif;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    h1 {
        text-align: center;
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# App title
st.title("📱 Mobile Phone Price Predictor")


# Define input fields inside a styled container
with st.container():
    st.markdown("<div class='container'>", unsafe_allow_html=True)

    battery_power = st.number_input("🔋 Battery Power (mAh)", min_value=500, max_value=6000, step=100)
    blue = st.number_input("📶 Bluetooth (0/1)", min_value=0, max_value=1, step=1)
    clock_speed = st.number_input("⏱️ Clock Speed (GHz)", min_value=0.0, max_value=2.0, step=0.1)
    dual_sim = st.number_input("📲 Dual SIM (0/1)", min_value=0, max_value=1, step=1)
    fc = st.number_input("📸 Front Camera (MP)", min_value=0, max_value=19, step=1)
    four_g = st.number_input("📡 4G Enabled (0/1)", min_value=0, max_value=1, step=1)
    int_memory = st.number_input("💾 Internal Memory (GB)", min_value=2, max_value=64, step=10)
    m_dep = st.number_input("📏 Mobile Depth (cm)", min_value=0, max_value=1, step=1)
    mobile_wt = st.number_input("⚖️ Mobile Weight (grams)", min_value=80, max_value=200, step=10)
    n_cores = st.number_input("💻 Number of Cores", min_value=1, max_value=8, step=1)
    px_height = st.number_input("🖼️ Pixel Height", min_value=0, max_value=1960, step=100)
    px_width = st.number_input("🖼️ Pixel Width", min_value=500, max_value=1998, step=100)
    ram = st.number_input("📚 RAM (MB)", min_value=256, max_value=3998, step=256)
    sc_h = st.number_input("📏 Screen Height (cm)", min_value=5, max_value=19, step=1)
    sc_w = st.number_input("📏 Screen Width (cm)", min_value=5, max_value=18, step=1)
    talk_time = st.number_input("📞 Talk Time (hours)", min_value=2, max_value=20, step=1)
    three_g = st.number_input("📶 3G Enabled (0/1)", min_value=0, max_value=1, step=1)
    touch_screen = st.number_input("👆 Touchscreen (0/1)", min_value=0, max_value=1, step=1)
    wifi = st.number_input("📡 Wi-Fi Enabled (0/1)", min_value=0, max_value=1, step=1)

    st.markdown("</div>", unsafe_allow_html=True)

# Define price categories
price_categories = {
    0: "💰 Low-Priced",
    1: "💵 Medium-Priced",
    2: "💎 Expensive",
    3: "🏆 High-Expensive"
}

# Predict the price
if st.button("💡 Predict Price"):
    input_features = np.array([[
        battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory,
        m_dep, mobile_wt, n_cores, px_height, px_width, ram, sc_h, sc_w,
        talk_time, three_g, touch_screen, wifi
    ]])

    prediction = model.predict(input_features)

    price_category = price_categories.get(prediction[0], "Unknown")
    st.success(f"🎉 Predicted Price Category: {price_category}")

