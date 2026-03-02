# Building an Intelligent LeetCode Automated Solver with Python & GPT API

## Introduction
In the world of competitive programming, efficiency is key. However, students often spend a significant amount of time on the repetitive tasks of searching for problems, understanding requirements, and manually submitting solutions. This project introduces an **Automated LeetCode Problem Solving and Submission System**, designed to automate the entire lifecycle of a LeetCode problem—from discovery to final submission.

## The Problem
Manual problem-solving involves several time-consuming steps:
1. Searching for a specific problem number.
2. Manually extracting the problem description and constraints.
3. Writing and testing a solution.
4. Manually submitting it to the LeetCode platform.

Our system eliminates these manual steps, allowing for a seamless, automated flow.

## The Solution: System Architecture
The project is built using a modular Python architecture, leveraging powerful libraries like Selenium for browser automation and OpenAI's GPT API for intelligent solution generation.

### Key Modules:
- **Discovery Module**: Uses the LeetCode API to dynamically find any problem by its ID.
- **Extraction Module**: Scrapes the problem description and constraints using robust Selenium locators.
- **Intelligence Module**: Integrates with GPT-4o-mini to generate optimized, production-grade Python code.
- **Fallback Database**: Includes a pre-built database of solutions for the first 50 problems to ensure reliability.
- **Automation Module**: Handles browser orchestration, language selection (Python3), and direct JavaScript-based code injection into the Monaco editor.
- **Logging Module**: Tracks every submission and result in a local SQLite database for analytics.

## Technology Stack
- **Python**: Core programming language.
- **Selenium**: Web automation and browser orchestration.
- **OpenAI GPT API**: Large Language Model for code generation.
- **Requests**: API communication.
- **SQLite**: Local data persistence.

## Step-by-Step Pipeline
1. **User Input**: Enter a problem number (e.g., #1 Two Sum).
2. **Fetch Slug**: System finds the problem's URL slug via API.
3. **Open & Extract**: Selenium opens the problem and extracts the text.
4. **AI Generation**: GPT-4o-mini generates an optimized Python solution.
5. **Auto-Submit**: System switches the compiler to Python3 and injects the code.
6. **Result Logging**: The final result (e.g., "Accepted") is stored in the database.

## Ethical Considerations
While this tool demonstrates the power of automation and AI, it is designed for educational purposes. Understanding the generated code is mandatory for true learning, and we encourage users to use AI as a learning aid rather than a shortcut.

## Conclusion
This project demonstrates how Python and AI can be combined to solve real-world productivity challenges. By automating the repetitive parts of competitive programming, we can focus more on the logic and algorithmic thinking that truly matters.

---
**Project Details:**
- **Institution**: Lovely Professional University
- **Course**: Python & Full Stack Development
- **Developer**: [Your Name]
- **GitHub**: [Link to your Repo]
