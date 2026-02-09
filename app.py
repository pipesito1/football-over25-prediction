"""
Football Over 2.5 Goals Prediction App
Author: Felipe Sepúlveda
"""

import streamlit as st
import joblib
import pandas as pd


# Load model
@st.cache_resource
def load_model():
    return joblib.load("models/model_over25.pkl")


model = load_model()


# Title
st.title("⚽ Football Over 2.5 Goals Prediction")

st.markdown("""
This app predicts whether a football match will have **Over 2.5 Goals**
based on live match information.
""")


# Sidebar
st.sidebar.header("Match Information")


minuto = st.sidebar.number_input(
    "Match Minute",
    min_value=1,
    max_value=120,
    value=60
)

total_goles = st.sidebar.number_input(
    "Total Goals (Home + Away)",
    min_value=0,
    max_value=15,
    value=2
)


# Predict button
if st.button("🔮 Predict"):

    # Feature engineering (igual que en el notebook)
    minuto_ratio = minuto / 90
    goles_ratio = total_goles / minuto


    data = pd.DataFrame([[
        minuto,
        total_goles,
        minuto_ratio,
        goles_ratio
    ]], columns=[
        "minuto",
        "total_goles",
        "minuto_ratio",
        "goles_ratio"
    ])


    prediction = model.predict(data)[0]
    prob = model.predict_proba(data)[0][1]


    if prediction == 1:
        st.success(f"✅ Prediction: OVER 2.5 Goals ({prob*100:.1f}%)")
    else:
        st.warning(f"⚠️ Prediction: UNDER 2.5 Goals ({(1-prob)*100:.1f}%)")
