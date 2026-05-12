import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("model.pkl")

# Title
st.title("🌦️ Weather Summary Prediction")

st.write("Enter weather details to predict summary")

# Inputs
temp = st.number_input("Temperature (C)", value=10.0)
app_temp = st.number_input("Apparent Temperature (C)", value=10.0)
humidity = st.number_input("Humidity", value=0.5)
wind_speed = st.number_input("Wind Speed (km/h)", value=10.0)
wind_bearing = st.number_input("Wind Bearing (degrees)", value=100.0)
visibility = st.number_input("Visibility (km)", value=10.0)
pressure = st.number_input("Pressure (millibars)", value=1015.0)
snow = st.selectbox("Snow?", [0, 1])

# Label mapping
labels = {
    0: "Clear",
    1: "Cloudy",
    2: "Foggy",
    3: "Rain",
    4: "Windy"
}

# Prediction
if st.button("Predict"):
    features = np.array([[temp, app_temp, humidity, wind_speed,
                          wind_bearing, visibility, pressure, snow]])

    prediction = model.predict(features)[0]
    probs = model.predict_proba(features)

    st.success(f"Prediction: {labels[prediction]}")
    st.write(f"Confidence: {np.max(probs):.2f}")