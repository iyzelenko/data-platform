import streamlit as st
import pandas as pd

st.title("Student Analytics Dashboard")

data = {
    "faculty": ["IT", "IT", "Math", "Math", "Physics"],
    "student": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "grade": [90, 86, 95, 87, 82]
}

df = pd.DataFrame(data)

faculty = st.selectbox(
    "Faculty",
    df["faculty"].unique()
)

filtered_df = df[df["faculty"] == faculty]

st.write(f"Detailed analytics for {faculty}")

st.dataframe(filtered_df)

st.subheader("Average Grade")

st.metric(
    label="Avg Grade",
    value=round(filtered_df["grade"].mean(), 2)
)

chart_df = (
    df.groupby("faculty")["grade"]
    .mean()
    .reset_index()
)

st.subheader("Average Grade by Faculty")

st.bar_chart(chart_df.set_index("faculty"))