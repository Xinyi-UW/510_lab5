import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import psycopg2

# Load environment variables
load_dotenv()

# Configure the API
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Define the model
model = genai.GenerativeModel('gemini-pro')

# Function to generate content
def generate_content(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Streamlit UI setup
st.title("Architect Playground")
st.image("images/architectural image1.png")


prompt = st.text_area("Please input your needs")
if st.button("Generate"):
    reply = generate_content(prompt)
    st.write(reply)
