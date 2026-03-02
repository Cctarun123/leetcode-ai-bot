from openai import OpenAI
from config import OPENAI_API_KEY
import sys

# Use relative import to avoid ModuleNotFoundError when running from root
try:
    from modules.solutions_db import get_local_solution
except ModuleNotFoundError:
    from solutions_db import get_local_solution

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_solution(problem_text, problem_number=None):
    # Try the local database first for the common problems to save API quota
    if problem_number:
        print(f"Checking local database for problem number: '{problem_number}'")
        local_sol = get_local_solution(problem_number)
        if local_sol:
            print(f"Local solution found for problem {problem_number}. Using fallback database code.")
            return local_sol
        else:
            print(f"No local solution found for problem {problem_number} in solutions_db.py")

    print(f"Calling OpenAI API (GPT-4o-mini) for problem solution...")
    prompt = f"""
    You are an expert competitive programmer.
    Solve this LeetCode problem in Python.
    Return ONLY the Python code. No markdown, no explanations.

    Problem:
    {problem_text}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        if "insufficient_quota" in str(e):
            print("\n!!! OPENAI API QUOTA EXCEEDED !!!")
            print("Please check your OpenAI billing and plan at https://platform.openai.com/account/billing")
            
            # Final fallback: if API fails, try to return local solution if not already checked
            if problem_number:
                local_sol = get_local_solution(problem_number)
                if local_sol:
                    print("API failed but found a local solution. Falling back to pre-defined code.")
                    return local_sol
            
            print("No local fallback found for this problem.")
            raise Exception("OpenAI API Quota Exceeded and no local fallback available.")
        else:
            raise e