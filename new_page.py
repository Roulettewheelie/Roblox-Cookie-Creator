import json
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

API_KEY = 'YOUR_2CAPTCHA_API_KEY'
CAPTCHA_SITE_KEY = 'YOUR_FUNCAPTCHA_SITE_KEY'
TARGET_URL = 'https://www.roblox.com/'

def solve_fun_captcha(api_key, site_key, url):
    response = requests.post('http://2captcha.com/in.php', {
        'key': api_key,
        'method': 'funcaptcha',
        'surl': url,
        'data': site_key
    })

    if response.text.startswith('ERROR'):
        print("Error occurred while submitting the captcha:", response.text)
        return None

    captcha_id = response.text.split('|')[1]

    for _ in range(150):
        time.sleep(2)
        result_response = requests.get(f'http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}')
        
        if 'CAPCHA_NOT_READY' in result_response.text:
            continue
        else:
            return result_response.text.split('|')[1]

    print("Unable to solve the captcha in the given time.")
    return None

def create_account():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Comment this out if you want to see the browser
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service('/path/to/chromedriver'), options=chrome_options)
    driver.get(TARGET_URL)

    time.sleep(3)  # Wait a few seconds to mimic human browsing behavior

    # Click the Signup button
    signup_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign Up']"))
    )
    signup_button.click()

    time.sleep(2)  # Pause to let the new page load

    # Fill out the registration form
    user_email = f"user{int(time.time())}@example.com"
    user_password = "SecurePassword123"  # Use a secure password
    user_name = f"user{int(time.time())}"

    driver.find_element(By.NAME, "username").send_keys(user_name)
    driver.find_element(By.NAME, "password").send_keys(user_password)
    driver.find_element(By.NAME, "email").send_keys(user_email)

    # Solve the FunCaptcha
    try:
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'funcaptcha')]"))
        )
        
        print("Solving FunCaptcha...")
        captcha_solution = solve_fun_captcha(API_KEY, CAPTCHA_SITE_KEY, TARGET_URL)
        if captcha_solution:
            driver.execute_script("document.getElementsByName('funcaptcha-response')[0].value = arguments[0];", captcha_solution)
            print("FunCaptcha solved successfully.")
        else:
            print("Failed to solve the FunCaptcha.")
            return
    except TimeoutException:
        print("FunCaptcha not found. Please check the XPath.")
        return

    # Submit the form
    print("Submitting the registration form...")
    driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()

    time.sleep(5)  # Wait for the account to be created

    cookies = driver.get_cookies()
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)

    print("Registration completed and cookies saved:", cookies)

    driver.quit()

if __name__ == "__main__":
    create_account()