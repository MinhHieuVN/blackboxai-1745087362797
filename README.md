
Built by https://www.blackbox.ai

---

# Facebook Friend Request Bot

## Project Overview
The Facebook Friend Request Bot is a Python script that automates the process of sending friend requests on Facebook using Selenium. This tool allows users to specify a list of Facebook profiles to which they want to send friend requests. 

**Note:** Automating interactions on Facebook may violate Facebook's terms of service. Use this script responsibly and at your own risk.

## Installation

To get started with the Facebook Friend Request Bot, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/facebook_friend_request_bot.git
   cd facebook_friend_request_bot
   ```

2. **Install Python dependencies:**
   Ensure you have Python 3.x installed. Then, install Selenium using pip:
   ```bash
   pip install selenium
   ```

3. **Install WebDriver:**
   You will need either ChromeDriver or GeckoDriver to control your browser. Make sure to download and install the appropriate version, and add it to your PATH.

   - **ChromeDriver:** [Download Here](https://chromedriver.chromium.org/downloads)
   - **GeckoDriver:** [Download Here](https://github.com/mozilla/geckodriver/releases)

## Usage

1. Open the `facebook_friend_request_bot.py` file.
2. Update the `TARGET_PROFILES` list with the Facebook profile URLs to which you want to send friend requests.

   Example:
   ```python
   TARGET_PROFILES = [
       "https://www.facebook.com/zuck"
   ]
   ```

3. Run the script:
   ```bash
   python facebook_friend_request_bot.py
   ```

4. Enter your Facebook email and password when prompted.

## Features

- Automates sending friend requests to multiple Facebook profiles.
- Easily configurable list of target profiles.
- Supports Chrome and Firefox browsers.
- User-friendly prompts for email and password input.

## Dependencies

This project uses the following Python library:

- [Selenium](https://pypi.org/project/selenium/)

To install the dependencies, you can run:
```bash
pip install -r requirements.txt
```

*Note:* If you don't have a `requirements.txt` file, you can create one with the following content:
```
selenium
```

## Project Structure

```
facebook_friend_request_bot/
├── facebook_friend_request_bot.py   # The main script to run the bot
└── requirements.txt                  # Dependencies (optional)
```

## Disclaimer

Please be aware that using automated scripts on Facebook may lead to your account being temporarily or permanently banned. Always comply with the platform's guidelines and practice ethical usage.