import streamlit as st

st.set_page_config(
    page_title="CareerPath",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 CareerPath")

st.subheader("Build Your Career. Track Your Growth.")

st.write(
    "Your personal student career planning and learning companion."
)

st.divider()

st.header("👋 Welcome to CareerPath!")

st.write(
    "CareerPath helps you plan your career, develop your skills, "
    "learn important technologies, and track your progress."
)

st.write("### 🚀 Start your career journey")

if st.button("Get Started ➡️", use_container_width=True):

    st.session_state.started = True

if st.session_state.get("started", False):

    st.success("🎉 Welcome! Let's build your career journey step by step.")

    st.write("### Your Career Journey")

    st.write("1. 👤 Create your Profile")
    st.write("2. 🎯 Set your Career Goal")
    st.write("3. 🛠️ Add your Skills")
    st.write("4. 📚 Start Learning")
    st.write("5. 📊 Track your Progress")

    st.info(
        "Use the navigation menu on the left to explore CareerPath."
    )