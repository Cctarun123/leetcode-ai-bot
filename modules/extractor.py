from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

def get_slug_from_api(problem_number):
    """
    Automated Discovery: Fetches the problem slug using LeetCode's public API.
    Works for ALL problems (3000+).
    """
    try:
        url = "https://leetcode.com/api/problems/all/"
        print(f"Searching for problem #{problem_number} via LeetCode API...")
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for problem in data['stat_status_pairs']:
                if str(problem['stat']['question_id']) == str(problem_number):
                    return problem['stat']['question__title_slug']
        return None
    except Exception as e:
        print(f"API discovery failed: {e}")
        return None

def open_problem(driver, slug):
    driver.get(f"https://leetcode.com/problems/{slug}/description/")


def extract_problem_text(driver):
    wait = WebDriverWait(driver, 30)
    print("Waiting for problem description to load...")
    
    # Try multiple selectors for the problem description
    selectors = [
        "//div[@data-track-load='description_content']",
        "//div[contains(@class, 'description__')]",
        "//div[contains(@class, 'question-content')]",
        "//div[@id='descriptionContent']"
    ]
    
    description_text = ""
    for selector in selectors:
        try:
            element = wait.until(EC.presence_of_element_located((By.XPATH, selector)))
            if element.is_displayed():
                description_text = element.text
                if description_text.strip():
                    return description_text
        except:
            continue
            
    # If standard selectors fail, try a more aggressive approach
    try:
        # Wait a bit for dynamic content
        import time
        time.sleep(5)
        all_text = driver.find_element(By.TAG_NAME, "body").text
        if "Example 1:" in all_text:
            return all_text
    except:
        pass

    raise Exception("Could not extract problem text. The page might not have loaded correctly.")