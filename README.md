# Automated LeetCode Problem Solving and Submission System

An intelligent system built with Python and Selenium to automate problem discovery, solution extraction, and submission on LeetCode.

## 🚀 Features
- **Automated Discovery**: Dynamically fetches problem information using LeetCode's public API.
- **Problem Extraction**: Extracts problem statements and constraints directly from the LeetCode description page.
- **AI-Powered Solutions**: Generates optimized Python solutions using OpenAI's GPT API.
- **Smart Fallback**: Includes a local database for common problems (1-50) to ensure functionality even without API credits.
- **Auto-Submission**: Switches to Python3, injects the solution into the Monaco editor via JavaScript, and submits automatically.
- **Result Logging**: Maintains a local SQLite database to track every submission and result.

## 🛠️ Technology Stack
- **Language**: Python 3.x
- **Automation**: Selenium WebDriver
- **AI Integration**: OpenAI GPT API
- **Database**: SQLite3
- **Network**: Requests

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd leetcode-ai-bot
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_api_key_here
   LEETCODE_EMAIL=your_email_here
   LEETCODE_PASSWORD=your_password_here
   ```

## 🚀 How to Run
```bash
python main.py
```
1. Enter the LeetCode problem number when prompted.
2. The browser will open the login page—perform a manual login for the first time.
3. Once logged in, press **Enter** in the terminal to resume.
4. The system will handle the rest!

## 📄 Project Info
- **Institution**: Lovely Professional University
- **Course**: Python & Full Stack Development
- **Deadline**: 26/02/2026

## 📜 License
This project is for educational purposes only. Please follow LeetCode's terms of service.
