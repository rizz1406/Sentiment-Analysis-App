# frontend/app.py
import streamlit as st
import requests

# Streamlit app
st.title("Sentiment Analysis App")

user_input = st.text_area("Enter Text to Analyze Sentiment:")

if st.button("Analyze"):
    if user_input:
        response = requests.post("http://model-service:5001/predict", json={"text": user_input})
        
        if response.status_code == 200:
            result = response.json().get("sentiment")
            st.write(f"Sentiment: {result.capitalize()}")
        else:
            st.write("Error in fetching sentiment!")
    else:
        st.write("Please enter some text!")
