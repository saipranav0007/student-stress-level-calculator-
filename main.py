"""
DASHBOARD (Streamlit - pure Python, no HTML files)
----------------------------------------------------
Run with: python -m streamlit run app.py
"""

import streamlit as st
import pandas as pd
import os
from mathamatics import calculate_stress_score, classify_stress
from data_handler import load_data
from stressrules import get_all_explanations

st.set_page_config(page_title="Student Stress Level Monitor", layout="wide", page_icon="🧠")

st.markdown("""
    <style>
    .stApp {
        background-color: #FDFDF9;
    }
    h1, h2, h3, h4 {
        color: #111111 !important;
    }
    p, li, span, div {
        color: #1A1A1A;
    }
    div.stButton > button {
        background-color: #A8E6A1 !important;
        color: #111111 !important;
        border: 1px solid #7FCB78 !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        padding: 0.6em 1.2em !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    }
    div.stButton > button:hover {
        background-color: #8FD888 !important;
        color: #111111 !important;
        border: 1px solid #6BBF64 !important;
    }
    div.stButton > button p {
        color: #111111 !important;
        font-weight: 700 !important;
    }
    div[data-testid="stMetric"] {
        background-color: #F3F3EC;
        border-radius: 12px;
        padding: 15px;
        border: 1px solid #E5E5DD;
    }
    .info-card {
        background-color: #F3F3EC;
        border-left: 5px solid #A8E6A1;
        border-radius: 8px;
        padding: 14px 18px;
        margin: 10px 0px;
    }
    </style>
""", unsafe_allow_html=True)

col_logo, col_title = st.columns([1, 4])
with col_logo:
    logo_path = "kiet_logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=180)
    else:
        st.write("🏫")
with col_title:
    st.title("🧠 Student Stress Level Monitor")
    st.caption("A rule-based Python tool to measure student stress from daily lifestyle habits")

st.divider()

tab1, tab2, tab3, tab4 = st.tabs([
    "📋 Problem Statement",
    "🧮 Mathematics",
    "💻 Programming",
    "📊 Live Output",
])

with tab1:
    st.header("Problem Statement")
    st.markdown("""
    <div class="info-card">
    Students face daily stress from academic workload, screen time, and lifestyle
    habits, but rarely have a simple, objective way to measure or track it.
    This project calculates a quantitative <b>stress score (0-100)</b> from 5 daily
    lifestyle inputs, classifying it as <b>Low, Medium, or High</b>, so students
    get an early, data-driven signal before stress builds up.
    </div>
    """, unsafe_allow_html=True)

    st.subheader("Core Subject: Psychology / Human Health (Stress Physiology)")
    st.write("Each factor below is backed by real health/psychology research — this is the *why* behind the formula:")
    for factor, info in get_all_explanations().items():
        with st.expander(f"🔹 {factor.replace('_', ' ').title()}  (weight: {info['weight']})"):
            st.write(info["reason"])
            st.caption(f"✅ Ideal range: {info['ideal_range']}")

with tab2:
    st.header("Mathematics Used")

    st.markdown('<div class="info-card"><b>Why this matters:</b> raw numbers like "8 hours of sleep" vs "2 hours of social time" cannot simply be added together — they are on different scales and pull in different directions. These 4 steps turn 5 unrelated numbers into ONE meaningful, comparable score.</div>', unsafe_allow_html=True)

    st.subheader("Step 1: Min-Max Normalization")
    st.latex(r"\text{normalized} = \frac{\text{value}}{\text{max\_value}}")
    st.write("**Where it's used:** every one of the 5 factors (sleep, study, screen time, social activity, exercise) gets divided by its max possible value (12 hours), turning it into a fraction between 0 and 1. This is what makes a small number like social activity comparable to a bigger number like study hours.")

    st.subheader("Step 2: Weighted Sum Formula")
    st.latex(r"\text{Score} = \sum_{i=1}^{n} (\text{normalized}_i \times \text{weight}_i)")
    st.write("**Where it's used:** each normalized factor is multiplied by a weight (see the table below) and all 5 results are added together. A positive weight (like study hours) pushes the score UP. A negative weight (like sleep) pulls it DOWN. This is the step where your psychology reasoning actually gets baked into a number.")

    st.subheader("Step 3: Rescaling to 0-100")
    st.latex(r"\text{Score}_{0-100} = \frac{\text{Score} - \text{min}}{\text{max} - \text{min}} \times 100")
    st.write("**Where it's used:** the raw weighted sum (a small, meaningless decimal) is stretched to fit a familiar 0-100 range, the same way a percentage works — this is purely for making the result human-readable.")

    st.subheader("Step 4: Threshold Classification")
    st.write("**Where it's used:** once we have a 0-100 score, simple comparison logic turns it into a label:")
    st.markdown("""
    - 🟢 **0-34** → Low stress
    - 🟡 **35-64** → Medium stress
    - 🔴 **65-100** → High stress
    """)

    st.subheader("Weights currently used")
    weights_df = pd.DataFrame([
        {"Factor": k, "Weight": v["weight"], "Effect": "⬆️ Increases stress" if v["weight"] > 0 else "⬇️ Reduces stress"}
        for k, v in get_all_explanations().items()
    ])
    st.table(weights_df)

with tab3:
    st.header("Programming Approach")

    st.subheader("Libraries Used")
    st.markdown("""
    - **pandas** — reads/writes the CSV data as a table, and loops through every student's row
    - **streamlit** — turns this Python script into the interactive dashboard you're looking at right now
    """)

    st.subheader("Program Logic / Algorithm")
    st.code("""
1. Store factor weights (dictionary)               -> mathamatics.py
2. normalize(value, max_value)                       -> scales one number to 0-1
3. calculate_stress_score(5 inputs):
     - normalize each of the 5 factors
     - multiply each by its weight
     - sum them all
     - rescale total to 0-100
     - return score
4. classify_stress(score):
     - if/elif/else against thresholds
     - return "Low" / "Medium" / "High"
5. Main program:
     - single student -> call functions once (this dashboard's sliders)
     - many students (CSV) -> loop through each row, repeat steps 3-4
    """, language="text")

    st.subheader("Key Concepts Used")
    st.markdown("""
    - **Variables** — store each factor's value
    - **Dictionary** — store weights as key → value pairs
    - **Functions** — one clear job per function (normalize, score, classify)
    - **Loop** — repeats the calculation for every student in a CSV
    - **Conditional (if/elif/else)** — turns the score into a Low/Medium/High label
    """)

    with st.expander("📄 View mathamatics.py source code"):
        st.code(open("mathamatics.py").read(), language="python")

with tab4:
    st.header("Try It Yourself")
    st.write("Move the sliders to match your own daily habits, then click Calculate.")

    col1, col2 = st.columns(2)
    with col1:
        sleep_hours = st.slider("😴 Sleep Hours", 0.0, 12.0, 7.0)
        study_hours = st.slider("📚 Study Hours", 0.0, 12.0, 4.0)
        screen_time = st.slider("📱 Screen Time (hours)", 0.0, 12.0, 3.0)
    with col2:
        social_activity = st.slider("🗣️ Social Activity (hours)", 0.0, 12.0, 2.0)
        exercise_hours = st.slider("🏃 Exercise (hours)", 0.0, 12.0, 1.0)

    if st.button("✨ Calculate Stress Level"):
        score = calculate_stress_score(sleep_hours, study_hours, screen_time, social_activity, exercise_hours)
        category = classify_stress(score)
        tone_colors = {"Low": "#C9EAC4", "Medium": "#F5D48A", "High": "#B0413E"}
        text_colors = {"Low": "#1B3A1B", "Medium": "#4A3200", "High": "#FFFFFF"}
        m_col, g_col = st.columns([1, 1.5])
        with m_col:
            st.metric("Stress Score", f"{score}/100")
            box_html = "<div style=\"background-color:" + tone_colors[category] + ";color:" + text_colors[category] + ";padding:18px;border-radius:10px;text-align:center;font-size:22px;font-weight:700;\">" + category + " Stress</div>"
            st.markdown(box_html, unsafe_allow_html=True)
        with g_col:
            st.subheader("Gauge")
            st.progress(int(score))
            st.caption("0 (Low) ————————————— 100 (High)")

    st.divider()
    st.header("Sample Dataset Results (50 students)")
    try:
        df = load_data("student_data_50.csv")
        df["stress_score"] = df.apply(lambda row: calculate_stress_score(row["sleep_hours"], row["study_hours"], row["screen_time"], row["social_activity"], row["exercise_hours"]), axis=1)
        df["category"] = df["stress_score"].apply(classify_stress)
        st.dataframe(df, use_container_width=True)
        st.bar_chart(df.set_index("name")["stress_score"])
    except FileNotFoundError:
        st.error("student_data_50.csv not found.")
        