from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def start_browser():

    options = webdriver.ChromeOptions()

    # Remove automation flag
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    options.add_argument("--disable-blink-features=AutomationControlled")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Hide webdriver property
    driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    driver.maximize_window()
    return driver


def login_leetcode(driver):
    driver.get("https://leetcode.com/accounts/login/")
    print("\nLogin manually in the browser.")
    input("After successful login, press Enter here...")
    print("Resuming script execution...")
    time.sleep(2) # Give the browser a moment to settle after login