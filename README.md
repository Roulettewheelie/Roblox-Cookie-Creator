🚀 Automated Account Creation Script for Roblox 🤖
Overview
This Python script automates the process of creating a new account on Roblox while handling FunCaptcha verification through the 2Captcha service. It mimics human behavior, making it less detectable by anti-bot measures.

⚡ Features
Automatically fills in the registration form
Solves FunCaptcha using 2Captcha
Saves cookies for future sessions
Mimics human-like interactions with pauses
Headless browsing option available
📝 Requirements
Before you start, make sure you have the following:

Python installed on your machine (preferably Python 3.6 or above)
Selenium library: Install using pip install selenium
Requests library: Install using pip install requests
Chrome WebDriver: Download it from here and provide the correct path in the script.
An account on 2Captcha to solve captchas:
API Key from your 2Captcha account
📦 Installation Steps
Clone or Download the script:

Save the provided script into a .py file, for example, roblox_account_creator.py.
Configure API Keys:

Replace YOUR_2CAPTCHA_API_KEY and YOUR_FUNCAPTCHA_SITE_KEY in the script with your actual API keys.
Path to ChromeDriver:

Update the path in the line Service('/path/to/chromedriver') to point to your ChromeDriver executable.
Run the Script:

Open a terminal or command prompt.
Navigate to the directory where the script is saved.
Run the script using the command:
CopyReplit
python roblox_account_creator.py
Check for Cookies:

After successful execution, cookies will be saved in a file named cookies.json for further use.
🔑 Important Notes
I am not responsible for any bans and dont hate too much its just a prototype
🎉 Credits
Revamp/Tmw
🎈 Have Fun!
Feel free to modify the script to suit your needs. If you encounter any issues or have suggestions, don't hesitate to reach out or contribute improvements!
