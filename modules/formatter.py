import re

def clean_code(code):
    """
    Cleans the GPT output to get only the Python code.
    Removes markdown backticks and language identifiers.
    """
    if not code:
        return ""
        
    # Pattern to match code blocks like ```python ... ``` or just ``` ... ```
    pattern = r"```(?:python|py)?\n(.*?)\n```"
    match = re.search(pattern, code, re.DOTALL)
    
    if match:
        code = match.group(1)
    else:
        # If no code block found, try to remove just the backticks if they exist
        code = code.replace("```python", "").replace("```py", "").replace("```", "")
        
    return code.strip()