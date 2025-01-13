from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def fetch_tiktok_user_data(username):
    # Setup the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open the website
    driver.get('https://omar-thing.nekoweb.org')

    try:
        # Find the username input field and the "Fetch Data" button
        username_input = driver.find_element(By.ID, 'usernameInput')
        fetch_button = driver.find_element(By.ID, 'fetchButton')

        # Enter the username and click "Fetch Data"
        username_input.clear()
        username_input.send_keys(username)
        fetch_button.click()

        # Wait for the data to load (adjust the time as necessary)
        time.sleep(5)

        # Now, extract the result (you might need to inspect the DOM and adjust this)
        # Example: extracting the result that may appear after clicking the button
        result = driver.find_element(By.CLASS_NAME, 'result')  # Modify the selector based on the actual result
        return result.text

    except Exception as e:
        return f"An error occurred: {str(e)}"
    finally:
        # Close the browser after retrieving the data
        driver.quit()

# Example usage
username = input("Enter TikTok username: ")
result = fetch_tiktok_user_data(username)
print(result)
