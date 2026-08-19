import streamlit as st

st.title("📊 Progress Dashboard")

st.write("Track your career development progress.")

skills_completed = st.number_input(
    "Skills completed",
    min_value=0,
    max_value=100,
    value=0
)

courses_completed = st.number_input(
    "Courses completed",
    min_value=0,
    max_value=100,
    value=0
)

projects_completed = st.number_input(
    "Projects completed",
    min_value=0,
    max_value=100,
    value=0
)

if st.button("Calculate Progress"):
    total = skills_completed + courses_completed + projects_completed
    progress = min((total / 30) * 100, 100)

    st.progress(progress / 100)
    st.success(f"Your progress is approximately {progress:.0f}%")