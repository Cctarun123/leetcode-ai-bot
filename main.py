from modules.automation import start_browser, login_leetcode
from modules.problem_map import problem_map
from modules.extractor import open_problem, extract_problem_text, get_slug_from_api
from modules.gpt_engine import generate_solution
from modules.formatter import clean_code
from modules.submitter import submit_solution
from modules.logger import log_result
import sys

def main():
    print("\n=== Automated LeetCode Solver (API Discovery Enabled) ===\n")

    number = input("Enter problem number (e.g., 1 to 3000+): ").strip()

    # Try dynamic discovery first (covers all problems)
    slug = get_slug_from_api(number)
    
    # Fallback to local map if API fails
    if not slug and number in problem_map:
        slug = problem_map[number]
        print(f"Slug found in local map: {slug}")

    if not slug:
        print(f"Problem number {number} could not be discovered.")
        sys.exit(1)

    print(f"Selected problem: {slug}")

    # Start browser
    driver = start_browser()

    try:
        # Manual login
        login_leetcode(driver)

        print("\nOpening problem page...")
        open_problem(driver, slug)

        print("Extracting problem text...")
        problem_text = extract_problem_text(driver)
        print("Problem statement extracted successfully.")

        print("Generating solution via GPT API...")
        try:
            raw_solution = generate_solution(problem_text, number)
            solution = clean_code(raw_solution)
            
            print("\n===== AI GENERATED SOLUTION =====\n")
            print(solution)
            print("\n==================================\n")

            print("Directly entering and submitting solution...")
            status = submit_solution(driver, solution)
            print(f"Submission result: {status}")

            log_result(slug, status)
            
        except Exception as gpt_error:
            print(f"\nGPT Error: {gpt_error}")
            if "Quota" in str(gpt_error):
                print("Skipping submission due to missing API quota.")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
    finally:
        input("\nExecution finished. Press Enter to close browser...")
        driver.quit()

if __name__ == "__main__":
    main()
