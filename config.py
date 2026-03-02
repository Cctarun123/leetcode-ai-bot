from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LEETCODE_EMAIL = os.getenv("LEETCODE_EMAIL")
LEETCODE_PASSWORD = os.getenv("LEETCODE_PASSWORD")