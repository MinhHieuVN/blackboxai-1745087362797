"""
Facebook Friend Request Bot using Selenium

This script automates sending friend requests on Facebook.

Requirements:
- Python 3.x
- Selenium (`pip install selenium`)
- ChromeDriver or GeckoDriver installed and in PATH
- User Facebook credentials

Usage:
- Update the TARGET_PROFILES list with Facebook profile URLs to send friend requests to.
- Run the script and enter your Facebook email and password when prompted.

Disclaimer:
Automating interactions on Facebook may violate Facebook's terms of service.
Use this script responsibly and at your own risk.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
import time
import getpass

# List of Facebook profile URLs to send friend requests to
TARGET_PROFILES = [
    # Example: "https://www.facebook.com/zuck"
]

def login_facebook(driver, email, password):
    driver.get("https://www.facebook.com/login")
    wait = WebDriverWait(driver, 10)
    try:
        email_input = wait.until(EC.presence_of_element_located((By.ID, "email")))
        email_input.send_keys(email)
        password_input = driver.find_element(By.ID, "pass")
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        # Wait for home page to load by checking for the search box presence
        wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search Facebook']")))
        print("Logged in successfully.")
    except TimeoutException:
        print("Login failed or page took too long to load.")
        driver.quit()
        exit(1)

def send_friend_request(driver, profile_url):
    driver.get(profile_url)
    wait = WebDriverWait(driver, 10)
    try:
        # Wait for the Add Friend button to be clickable
        add_friend_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@aria-label='Add Friend' or @aria-label='Add friend']")))
        add_friend_button.click()
        print(f"Friend request sent to {profile_url}")
        time.sleep(2)  # Wait a bit after sending request
    except TimeoutException:
        print(f"Add Friend button not found or not clickable on {profile_url}")
    except ElementClickInterceptedException:
        print(f"Could not click Add Friend button on {profile_url} - it might be blocked or already sent.")
    except Exception as e:
        print(f"Unexpected error on {profile_url}: {e}")

def main():
    print("Facebook Friend Request Bot")
    email = input("Enter your Facebook email: ")
    password = getpass.getpass("Enter your Facebook password: ")

    # Setup Chrome WebDriver (make sure chromedriver is in PATH)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        login_facebook(driver, email, password)
        for profile in TARGET_PROFILES:
            send_friend_request(driver, profile)
    finally:
        print("Closing browser.")
        driver.quit()

if __name__ == "__main__":
    main()
