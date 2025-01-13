import streamlit as st
import requests

# Function to fetch TikTok user data
def fetch_tiktok_data(username):
    url = f'https://api.tiktok.com/user/{username}'  # Replace with the correct endpoint
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # Return the JSON data if the request is successful
    else:
        return None  # Return None if there's an error

# Streamlit UI elements
st.title('TikTok User Data Fetcher')

username = st.text_input('Enter TikTok username:', '')

if username:
    data = fetch_tiktok_data(username)
    
    if data:
        st.write(data)  # Display the fetched data
    else:
        st.error('Failed to fetch data. Please check the username or try again later.')
