import streamlit as st
import requests

# URL של ה-API (שינוי בהתאם לכתובת שלך
API_URL = "http://app_container:8000/login/"

st.title("User Login")

# טופס התחברות
st.header("Login")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    response = requests.post(API_URL, json={"username": username, "password": password})
    if response.status_code == 200:
        st.success("Login successful!")
    else:
        st.error("Invalid username or password.")

