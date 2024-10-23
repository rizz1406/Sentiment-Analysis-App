# frontend/app.py
import streamlit as st
import requests

# Streamlit app title
st.title("Sentiment Analysis App")

# Input text area for user
user_input = st.text_area("Enter Text to Analyze Sentiment:")

# Button to analyze sentiment
if st.button("Analyze"):
    if user_input:
        try:
            # Send a POST request to the model service running in Docker
            response = requests.post("http://model:5001/predict", json={"text": user_input})
            
            if response.status_code == 200:
                # Extract sentiment result from the response
                result = response.json().get("sentiment")
                st.write(f"**Sentiment:** {result.capitalize()}")
            else:
                st.write("❌ Error in fetching sentiment! Please try again.")
        except requests.exceptions.ConnectionError:
            st.write("🚫 Could not connect to the model service. Make sure it's running and reachable!")
    else:
        st.write("⚠️ Please enter some text!")
