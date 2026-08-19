import streamlit as st

st.title("🎯 Career Goals")

st.write("Set your career goal and plan your future.")

goal = st.text_input("What is your career goal?")
job_role = st.text_input("Target job role")
target_date = st.date_input("Target date")
description = st.text_area("Describe your goal")

if st.button("Save Career Goal"):
    st.success("Career goal saved successfully! 🎉")