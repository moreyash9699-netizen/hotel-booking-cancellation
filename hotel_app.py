import streamlit as st
import pandas as pd
import joblib

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Hotel Cancellation Predictor",
    page_icon="🏨",
    layout="centered"
)

# -------------------------------
# Load Model & Features
# -------------------------------
model = joblib.load("hotel_cancellation_model.pkl")
features = joblib.load("model_features.pkl")

# -------------------------------
# App Header
# -------------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #2C3E50;'>🏨 Grand Stay Hotel</h1>
    <h3 style='text-align: center; color: #16A085;'>Booking Cancellation Prediction System</h3>
    <p style='text-align: center; color: gray;'>
    Helping hotel managers identify high-risk bookings in advance
    </p>
    <hr>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Sidebar – User Input
# -------------------------------
st.sidebar.header("📋 Enter Booking Details")

lead_time = st.sidebar.number_input(
    "⏳ Lead Time (days)",
    min_value=0,
    help="Number of days between booking and arrival"
)

adr = st.sidebar.number_input(
    "💰 ADR (Average Daily Rate)",
    min_value=0.0,
    help="Average price per night"
)

special_requests = st.sidebar.number_input(
    "⭐ Total Special Requests",
    min_value=0,
    help="Number of special requests made by the guest"
)

parking = st.sidebar.number_input(
    "🚗 Required Car Parking Spaces",
    min_value=0,
    help="Number of parking spaces requested"
)

deposit_type = st.sidebar.selectbox(
    "💳 Deposit Type",
    ["Non Refund", "No Deposit"]
)

market_segment = st.sidebar.selectbox(
    "🌐 Market Segment",
    ["Online TA", "Direct", "Offline TA/TO"]
)

customer_type = st.sidebar.selectbox(
    "👤 Customer Type",
    ["Transient", "Transient-Party"]
)

# -------------------------------
# Convert Input to Model Format
# -------------------------------
input_data = pd.DataFrame([{
    'lead_time': lead_time,
    'adr': adr,
    'total_of_special_requests': special_requests,
    'required_car_parking_spaces': parking,
    'deposit_type_Non Refund': 1 if deposit_type == "Non Refund" else 0,
    'market_segment_Online TA': 1 if market_segment == "Online TA" else 0,
    'market_segment_Direct': 1 if market_segment == "Direct" else 0,
    'market_segment_Offline TA/TO': 1 if market_segment == "Offline TA/TO" else 0,
    'customer_type_Transient': 1 if customer_type == "Transient" else 0,
    'customer_type_Transient-Party': 1 if customer_type == "Transient-Party" else 0
}])

# Ensure correct column order
input_data = input_data.reindex(columns=features, fill_value=0)

# -------------------------------
# Prediction Section
# -------------------------------
st.markdown("### 🔍 Prediction Result")

if st.button("🔮 Predict Cancellation"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error(
            "❌ **High Risk Booking**\n\n"
            "This booking is **likely to be canceled**.\n\n"
            "📌 Suggested Action:\n"
            "- Ask for partial advance payment\n"
            "- Send confirmation reminder\n"
            "- Monitor booking closely"
        )
    else:
        st.success(
            "✅ **Low Risk Booking**\n\n"
            "This booking is **unlikely to be canceled**.\n\n"
            "📌 Booking looks stable."
        )

# -------------------------------
# Footer
# -------------------------------
st.markdown(
    """
    <hr>
    <div style="text-align: center; color: gray;">
        <p>
        Developed using <b>Machine Learning</b> & <b>Streamlit</b><br>
        Internship Project – Data Science & AI/ML
        </p>
        <p style="font-size:16px; font-weight:bold; color:#2C3E50;">
        ~ YASH MORE
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
