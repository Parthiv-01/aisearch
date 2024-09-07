import streamlit as st
import requests
import toml

# Load the API key and base URL from the config file
api_key = st.secrets["auth"]["API_KEY"]
base_url = st.secrets["auth"]["BASE_URL"]

# Set up headers for the API request
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Function to get a response from the NVIDIA API
def get_ai_response(user_input):
    payload = {
        "model": "meta/llama-3.1-405b-instruct",
        "messages": [{"role": "user", "content": user_input}],
        "temperature": 0.2,
        "top_p": 0.7,
        "max_tokens": 1024
    }
    
    # Sending request to the NVIDIA API
    response = requests.post(f"{base_url}/chat/completions", headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        # Access the content from the response
        ai_message = result['choices'][0]['message']['content']
        return ai_message
    else:
        return f"Error: {response.status_code}, {response.text}"

# Streamlit app interface
st.title("AI Chat")

# Input for user to send to AI
user_input = st.text_input("You:", placeholder="Type your message here...")

# Button to submit user input and get response
if st.button("Send"):
    if user_input:
        # Fetch the AI response
        response = get_ai_response(user_input)
        st.text_area("AI Response:", value=response, height=200)
    else:
        st.warning("Please enter a message to send.")

# Instructions for users
st.write("Enter a message to chat with the AI")
