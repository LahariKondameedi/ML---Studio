import streamlit as st

st.set_page_config(
    page_title="ML Studio",
    page_icon="🤖"
)

st.title("🤖 ML Studio")
st.write("Welcome to your AI and Machine Learning workspace!")

name = st.text_input("Enter your name")

if st.button("Get Started"):
    if name.strip():
        st.success(f"Welcome to ML Studio, {name}!")
    else:
        st.warning("Please enter your name.")
