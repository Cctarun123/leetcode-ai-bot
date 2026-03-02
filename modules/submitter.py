from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def select_python_language(driver):
    wait = WebDriverWait(driver, 10)
    try:
        # Check if Python3 is already selected to avoid unnecessary clicks
        try:
            # Look for the current language label in the button
            # Updated selector for more reliability
            current_lang_elem = driver.find_element(By.XPATH, "//button[contains(@id, 'headlessui-listbox-button')]//div[contains(text(), 'Python3')] | //button[contains(@id, 'headlessui-listbox-button')]//div[contains(text(), 'Python')]")
            if current_lang_elem:
                print("Python3 is already selected.")
                return
        except:
            pass

        print("Attempting to select Python3 language...")
        
        # 1. Click the language selector button
        # Multiple possible selectors for the button
        lang_btn_selectors = [
            "//button[contains(@id, 'headlessui-listbox-button')]",
            "//button[contains(@class, 'flex cursor-pointer items-center')]",
            "//div[contains(@class, 'select-none') and contains(text(), 'C++')]/.."
        ]
        
        lang_btn = None
        for selector in lang_btn_selectors:
            try:
                btn = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                if btn.is_displayed():
                    lang_btn = btn
                    break
            except:
                continue
        
        if not lang_btn:
            print("Language selector button not found. Assuming correct language is selected.")
            return

        # Scroll and click
        driver.execute_script("arguments[0].scrollIntoView(true);", lang_btn)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", lang_btn)
        print("Language menu opened.")
        time.sleep(1)

        # 2. Find and click 'Python3' in the dropdown
        # The dropdown items usually have role='option'
        python_selectors = [
            "//li//div[text()='Python3']",
            "//div[@role='option']//div[text()='Python3']",
            "//div[contains(@class, 'select-none') and text()='Python3']"
        ]
        
        python_option = None
        for selector in python_selectors:
            try:
                opt = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                if opt.is_displayed():
                    python_option = opt
                    break
            except:
                continue
        
        if python_option:
            driver.execute_script("arguments[0].click();", python_option)
            print("Python3 selected!")
        else:
            print("Python3 option not found in dropdown.")
            
        time.sleep(2)
        
    except Exception as e:
        print(f"Warning: Language selection failed or timed out: {e}")
        print("Continuing with current language...")

def submit_solution(driver, code):
    wait = WebDriverWait(driver, 30)

    try:
        # 1. Stay on current URL if it's already the problem page
        print(f"Current URL: {driver.current_url}")
        
        # 2. Ensure Python3 is selected
        select_python_language(driver)
        
        # 3. Wait for Monaco editor and focus it
        print("Looking for Monaco editor...")
        editor_container = None
        editor_selectors = [
            "//div[contains(@class, 'monaco-editor')]",
            "//div[@role='code']",
            "//div[contains(@class, 'editor-container')]"
        ]
        
        for selector in editor_selectors:
            try:
                container = wait.until(EC.presence_of_element_located((By.XPATH, selector)))
                if container.is_displayed():
                    editor_container = container
                    break
            except:
                continue
                
        if not editor_container:
            raise Exception("Could not find Monaco editor container.")
            
        print("Editor found. Focusing and clearing...")
        # Scroll to editor
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", editor_container)
        time.sleep(1)
        
        # Click exactly where the code should go (deep click)
        try:
            # Try to find the lines area for a more targeted click
            lines_area = editor_container.find_element(By.CLASS_NAME, "view-lines")
            ActionChains(driver).move_to_element(lines_area).click().perform()
        except:
            ActionChains(driver).move_to_element(editor_container).click().perform()
            
        time.sleep(1)

        # 3. Clear existing code (CTRL+A, BACKSPACE)
        # We do this twice just to be super sure
        for _ in range(2):
            ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
            time.sleep(0.5)
            ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
            time.sleep(0.5)
        
        time.sleep(1)

        # 4. Enter new code
        print("Entering solution code...")
        
        # Try JavaScript injection first as it's the most reliable for Monaco
        # We'll try to find the editor instance using LeetCode's common internal structures
        try:
            print("Attempting to set code via JavaScript...")
            js_script = """
                try {
                    // Try different ways to find the editor model
                    var model = null;
                    if (window.monaco && monaco.editor) {
                        var models = monaco.editor.getModels();
                        if (models && models.length > 0) {
                            model = models[0];
                        }
                    }
                    
                    if (model) {
                        model.setValue(arguments[0]);
                        return true;
                    }
                } catch (e) {
                    console.error("Monaco setValue failed: " + e);
                }
                return false;
            """
            success = driver.execute_script(js_script, code)
            if success:
                print("Code set successfully via JavaScript.")
            else:
                raise Exception("Monaco model not found or accessible via window.monaco.")
        except Exception as js_err:
            print(f"JavaScript injection failed: {js_err}. Falling back to typing simulation...")
            # If JS fails, we'll try to use a more robust "typing" method
            # We use ActionChains with the code
            ActionChains(driver).send_keys(code).perform()

        time.sleep(2)

        # 5. Click the Submit button
        print("Locating Submit button...")
        submit_btn = None
        submit_selectors = [
            "//button[@data-cy='submit-code-btn']",
            "//button[contains(@class, 'submit')]",
            "//button[contains(text(),'Submit')]",
            "//button[contains(., 'Submit')]",
            "//button[contains(@class, 'green') and contains(., 'Submit')]"
        ]
        
        for selector in submit_selectors:
            try:
                # Use a shorter wait for each selector
                btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, selector)))
                if btn.is_displayed() and btn.is_enabled():
                    submit_btn = btn
                    break
            except:
                continue
        
        if not submit_btn:
            # Final desperate attempt to find ANY green button that might be Submit
            try:
                btns = driver.find_elements(By.TAG_NAME, "button")
                for btn in btns:
                    if "Submit" in btn.text and btn.is_displayed():
                        submit_btn = btn
                        break
            except:
                pass
                
        if not submit_btn:
            raise Exception("Could not find an active Submit button.")
            
        print(f"Clicking Submit button: {submit_btn.text}")
        # JS click is often more reliable than standard click for these dynamic buttons
        driver.execute_script("arguments[0].click();", submit_btn)
        
        print("Submitted! Waiting for results to appear...")
        # Longer wait for result to appear
        time.sleep(12)

        # 6. Wait for result
        print("Looking for submission result status...")
        result_selectors = [
            "//span[contains(@data-e2e-locator, 'submission-result-status')]",
            "//div[contains(@class, 'success')]",
            "//div[contains(text(), 'Accepted')]",
            "//div[contains(@class, 'result')]//span",
            "//a[contains(@href, '/submissions/')]/span"
        ]
        
        for selector in result_selectors:
            try:
                result_elem = driver.find_element(By.XPATH, selector)
                if result_elem.is_displayed():
                    res_text = result_elem.text.strip()
                    if res_text:
                        print(f"Result found: {res_text}")
                        return res_text
            except:
                continue
                
        return "Submitted (Check browser for result status)"

    except Exception as e:
        print(f"!!! Submission Error: {e}")
        return f"Error: {str(e)}"