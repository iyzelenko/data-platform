import streamlit as st
import pandas as pd

st.title("Student Analytics Dashboard")

faculty = st.selectbox(
    "Faculty",
    ["IT", "Math", "Physics"]
)

st.write(f"Detailed analytics for {faculty}")

df = pd.DataFrame({
    "faculty": ["IT", "Math", "Physics"],
    "avg_grade": [88, 91, 85]
})

st.bar_chart(df.set_index("faculty"))