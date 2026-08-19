import streamlit as st

st.title("🛠️ Skills Tracker")

st.write("Add your skills and track your learning progress.")

skill = st.text_input("Enter a skill")

level = st.selectbox(
    "Select your skill level",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.button("Add Skill"):
    if skill:
        st.success(f"{skill} added successfully! 🎉")
    else:
        st.warning("Please enter a skill.")