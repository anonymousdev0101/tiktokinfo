import requests
from bs4 import BeautifulSoup
import streamlit as st

def fetch_tiktok_user_data(username):
    url = f"https://www.tiktok.com/@{username}"

    # Send a GET request to the TikTok page
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data (we're looking for meta tags containing the user data)
        user_data = {}
        try:
            user_data['followers'] = soup.find('strong', {'title': 'Followers'}).text
            user_data['following'] = soup.find('strong', {'title': 'Following'}).text
            user_data['likes'] = soup.find('strong', {'title': 'Likes'}).text
        except AttributeError:
            st.error("Could not retrieve the data from TikTok. Please check the username.")
            return None

        return user_data
    
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to fetch data: {e}")
        return None

# Streamlit UI
st.title("TikTok User Data Fetcher")

username = st.text_input("Enter TikTok Username", "")

if username:
    data = fetch_tiktok_user_data(username)
    if data:
        st.write("User Data:")
        st.write(data)
