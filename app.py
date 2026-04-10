import streamlit as st
import pandas as pd

from data import generate_data
from logic import irrigation_decision, irrigation_duration
from model import predict_moisture

st.set_page_config(page_title="Smart Irrigation", layout="centered")

st.title("🌱 Smart Irrigation AI System")
st.caption("AI-powered irrigation decision support system")

# تخزين البيانات
if "data_history" not in st.session_state:
    st.session_state.data_history = []

# زرار
if st.button("Generate New Data"):
    new_data = generate_data()
    st.session_state.data_history.append(new_data)

# لو فيه بيانات
if st.session_state.data_history:

    data = st.session_state.data_history[-1]

    # عرض البيانات
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Moisture", data["moisture"])

    with col2:
        st.metric("Temperature", data["temperature"])

    # القرار
    decision = irrigation_decision(data["moisture"])
    duration = irrigation_duration(data["moisture"], data["temperature"])

    st.subheader("🚰 Decision")
    st.success(decision)

    if duration > 0:
        st.write(f"💧 Irrigation Duration: {duration} minutes")

    # DataFrame
    df = pd.DataFrame(st.session_state.data_history)

    st.subheader("📊 Moisture Over Time")
    st.line_chart(df["moisture"])

    # Prediction
    prediction = predict_moisture(df)

    if prediction:
        st.subheader("🔮 Predicted Moisture")
        st.write(f"{prediction:.2f}")

        if prediction < 30:
            st.warning("⚠️ Soil will be dry soon!")

    # Alerts
    if data["moisture"] < 20:
        st.error("🚨 Critical soil dryness")

    # Insights
    st.subheader("📈 Insights")

    st.write(f"Average Moisture: {df['moisture'].mean():.2f}")
    st.write(f"Dry times: {sum(df['moisture'] < 30)}")

else:
    st.info("Click button to generate data")