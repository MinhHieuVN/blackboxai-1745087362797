"""
Facebook Friend Request Bot for Mobile using Appium

This script automates sending friend requests on Facebook mobile web using Appium.

Requirements:
- Python 3.x
- Appium server running
- Appium Python client (`pip install Appium-Python-Client`)
- Mobile device or emulator with Chrome browser
- User Facebook credentials

Usage:
- Start Appium server
- Connect your mobile device or start emulator
- Run this script and enter your Facebook email and password when prompted

Disclaimer:
Automating interactions on Facebook may violate Facebook's terms of service.
Use this script responsibly and at your own risk.
"""

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time
import getpass

def login_facebook(driver, email, password):
    driver.get("https://m.facebook.com/login")
    wait = WebDriverWait(driver, 20)
    try:
        email_input = wait.until(EC.presence_of_element_located((By.ID, "m_login_email")))
        email_input.send_keys(email)
        password_input = driver.find_element(By.ID, "m_login_password")
        password_input.send_keys(password)
        login_button = driver.find_element(By.NAME, "login")
        login_button.click()
        # Wait for home page to load by checking for the search box presence
        wait.until(EC.presence_of_element_located((By.NAME, "q")))
        print("Logged in successfully.")
    except TimeoutException:
        print("Login failed or page took too long to load.")
        driver.quit()
        exit(1)

def send_friend_requests_in_suggestions(driver):
    # Navigate to friend suggestions page on mobile
    driver.get("https://m.facebook.com/friends/center/suggestions")
    wait = WebDriverWait(driver, 20)
    time.sleep(5)  # Wait for the page to load fully

    # Scroll down to load more suggestions
    scroll_pause_time = 2
    last_height = driver.execute_script("return document.body.scrollHeight")
    for _ in range(3):  # Scroll 3 times to load more suggestions
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    # Find all Add Friend buttons in the suggestions
    try:
        add_friend_buttons = driver.find_elements(By.XPATH, "//a[contains(@href, 'friend_request') and contains(text(), 'Add Friend')]")
        print(f"Found {len(add_friend_buttons)} friend suggestion(s) to send requests to.")
        for button in add_friend_buttons:
            try:
                button.click()
                print("Friend request sent.")
                time.sleep(2)  # Wait between requests to avoid detection
            except ElementClickInterceptedException:
                print("Could not click Add Friend button - it might be blocked or already sent.")
            except Exception as e:
                print(f"Unexpected error when clicking Add Friend button: {e}")
    except Exception as e:
        print(f"Error finding Add Friend buttons: {e}")

def main():
    print("Facebook Friend Request Bot for Mobile")
    email = input("Enter your Facebook email: ")
    password = getpass.getpass("Enter your Facebook password: ")

    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",  # Change as per your device/emulator
        "deviceName": "Android Emulator",  # Change as per your device/emulator
        "browserName": "Chrome",
        "automationName": "UiAutomator2"
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    try:
        login_facebook(driver, email, password)
        send_friend_requests_in_suggestions(driver)
    finally:
        print("Closing browser.")
        driver.quit()

if __name__ == "__main__":
    main()
