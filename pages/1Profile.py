import streamlit as st

st.title("👤 Student Profile")

st.write("Create and manage your CareerPath profile.")

name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
course = st.text_input("Enter your course")
college = st.text_input("Enter your college")

if st.button("Save Profile"):
    st.success("Profile saved successfully! 🎉")

    st.subheader("Education Details")

degree = st.text_input("Degree")
branch = st.text_input("Branch")
college = st.text_input("College Name")
semester = st.text_input("Current Semester")
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.01)

if st.button("Save Education"):
    st.success("Education details saved successfully!")