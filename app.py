"""
Football Over 2.5 Goals Prediction App
Author: Felipe Sepúlveda
"""

import streamlit as st
import joblib
import pandas as pd
import requests
import os


# Load model
@st.cache_resource
def load_model():
    return joblib.load("models/model_over25.pkl")


model = load_model()


# Get live matches
@st.cache_data(ttl=60)
def get_live_matches():

    API_KEY = os.getenv("FOOTBALL_API_KEY")

    if not API_KEY:
        return None

    url = "https://v3.football.api-sports.io/fixtures?live=all"

    headers = {
        "x-apisports-key": API_KEY
    }

    r = requests.get(url, headers=headers)
    data = r.json()

    return data["response"]


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

    # Feature engineering
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


# ================= LIVE MATCHES =================

st.divider()
st.subheader("📺 Live Matches")

matches = get_live_matches()

if matches is None:
    st.error("❌ API KEY not configured")

elif len(matches) == 0:
    st.info("No live matches right now")

else:

    # First match
    first = matches[0]

    home = first["teams"]["home"]["name"]
    away = first["teams"]["away"]["name"]

    gh = first["goals"]["home"] or 0
    ga = first["goals"]["away"] or 0

    minute = first["fixture"]["status"]["elapsed"]

    st.markdown("### ⭐ Featured Match")

    st.success(
        f"{home} {gh} - {ga} {away} | ⏱ {minute}'"
    )

    st.divider()

    # All matches
    rows = []

    for m in matches:

        home = m["teams"]["home"]["name"]
        away = m["teams"]["away"]["name"]

        gh = m["goals"]["home"] or 0
        ga = m["goals"]["away"] or 0

        minute = m["fixture"]["status"]["elapsed"]

        total = gh + ga

        # ML features
        minuto_ratio = minute / 90 if minute else 0
        goles_ratio = total / minute if minute else 0

        data = pd.DataFrame([[
            minute,
            total,
            minuto_ratio,
            goles_ratio
        ]], columns=[
            "minuto",
            "total_goles",
            "minuto_ratio",
            "goles_ratio"
        ])

        prob = model.predict_proba(data)[0][1]

        rows.append([
            home,
            away,
            gh,
            ga,
            minute,
            f"{prob*100:.1f}%"
        ])


    df_show = pd.DataFrame(
        rows,
        columns=[
            "Home",
            "Away",
            "Goals Home",
            "Goals Away",
            "Minute",
            "Over 2.5 Probability"
        ]
    )


    st.dataframe(df_show, use_container_width=True)
