# 🔐 CodeSentry – AI-Powered Security Code Reviewer

## 📌 Overview

CodeSentry is an AI-powered security code review assistant built using the Google Gemini API and Python.

The application accepts:

- A natural language security-related query
- A source code snippet

It uses a Large Language Model (LLM) configured as a cybersecurity expert and automatically invokes a local vulnerability scanning tool whenever potentially unsafe code patterns are detected.

The tool analyzes the code, identifies security risks, explains vulnerabilities in simple language, and recommends secure alternatives.

---

## 🎯 Objective

The objective of this project is to build an intelligent code-review assistant that can:

- Detect common security vulnerabilities
- Explain risks in plain language
- Suggest secure coding practices
- Automatically invoke a local scanning tool through Gemini Function Calling
- Produce structured security review reports

---

## 🛠 Technologies Used

- Python 3.10+
- Google Gemini API
- Google GenAI SDK
- Pytest
- Regex-based Static Analysis

---

## 📂 Project Structure

```text
code_sentry/
│
├── main.py                 # Entry point
├── tools.py                # Vulnerability scanner tool
├── prompts.py              # Security expert system prompt
├── requirements.txt        # Dependencies
├── README.md               # Documentation
│
└── tests/
    └── test_tools.py       # Unit tests
```

---

## 🚀 Features

### AI Security Expert

The Gemini model is configured using a system prompt that instructs it to:

- Act as a security engineer
- Review source code
- Detect vulnerabilities
- Explain risks clearly
- Suggest secure fixes

---

### Automatic Tool Calling

The model automatically decides when to invoke:

```python
scan_vulnerabilities()
```

No manual vulnerability scan trigger is required.

---

### Structured Security Reports

The application generates reports in the following format:

- Summary Verdict
- Security Findings
- Severity Levels
- Line References
- Recommended Fixes
- Developer-Friendly Explanation

---

## 🔍 Vulnerabilities Detected

The local scanner detects common security issues such as:

### 1. Hardcoded Credentials

Example:

```python
password = "admin123"
```

Risk:

- Credentials may leak through repositories or logs.

---

### 2. Unsafe eval()

Example:

```python
eval(user_input)
```

Risk:

- Allows arbitrary code execution.

---

### 3. Unsafe exec()

Example:

```python
exec(user_code)
```

Risk:

- Executes untrusted code.

---

### 4. SQL Injection Patterns

Example:

```python
query = f"SELECT * FROM users WHERE id={user_id}"
```

Risk:

- Database compromise through malicious input.

---

### 5. Command Injection

Example:

```python
subprocess.run(cmd, shell=True)
```

Risk:

- Allows execution of arbitrary system commands.

---

### 6. Insecure Deserialization

Examples:

```python
pickle.loads(data)
```

```python
yaml.load(data)
```

Risk:

- May execute malicious payloads.

---

### 7. Weak Hashing Algorithms

Examples:

```python
hashlib.md5()
```

```python
hashlib.sha1()
```

Risk:

- Vulnerable to collisions and attacks.

---

### 8. Missing Input Validation

User-controlled input used without validation.

Risk:

- Injection attacks and unexpected behavior.

---

## ⚙️ Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/tamanna0777/code_sentry.git
```

```bash
cd code_sentry
```

---

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3: Configure Gemini API Key

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Or set it directly:

### Windows

```cmd
set GEMINI_API_KEY=YOUR_API_KEY
```

### PowerShell

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

---

## ▶️ Running the Application

Execute:

```bash
python main.py
```

You will be prompted to enter:

1. Security question
2. Code snippet

Terminate code input using:

```text
END
```

---

## 💻 Sample Demo

### User Query

```text
Is this code safe for production?
```

### Code Snippet

```python
user_input = input()

eval(user_input)

password = "admin123"

import subprocess
subprocess.run(user_input, shell=True)
```

---

### Output

```text
===== SECURITY REVIEW =====

Summary Verdict:
High Risk

Findings:

1. Unsafe eval()
Severity: High

2. Command Injection
Severity: High

3. Hardcoded Credential
Severity: Medium

Developer Explanation:
This code is not safe for production because it allows
arbitrary code execution and command injection while
storing credentials directly in source code.
```

---

## 🧪 Running Unit Tests

Execute:

```bash
python -m pytest -v
```

Expected Output:

```text
tests/test_tools.py::test_eval_detection PASSED
tests/test_tools.py::test_clean_code PASSED

2 passed
```

---

## 📋 Assumptions

- Vulnerability detection is heuristic and regex-based.
- The scanner focuses on common security issues.
- The project is intended for educational and academic purposes.
- The tool does not replace professional security audits.
- Gemini decides when tool invocation is required.

---

## 🛡 Error Handling

The application gracefully handles:

- Empty code snippets
- Invalid user input
- Gemini API errors
- Service unavailability (503 errors)
- Tool execution failures

Instead of crashing, meaningful error messages are displayed.

---

## ✅ Functional Requirements Mapping

| Requirement | Status |
|------------|---------|
| Accept User Query | ✅ |
| Accept Code Snippet | ✅ |
| Security Expert System Prompt | ✅ |
| Local Tool Implementation | ✅ |
| Automatic Tool Invocation | ✅ |
| Structured Output | ✅ |
| Vulnerability Detection | ✅ |
| Unit Testing | ✅ |
| Error Handling | ✅ |
| README Documentation | ✅ |

---

## 📸 Demo Screenshots Included

The submission contains screenshots showing:

1. Project Structure
2. Vulnerability Scanner Implementation
3. System Prompt Configuration
4. Unit Test Execution
5. Application Execution
6. Security Review Output

---

## 👩‍💻 Author

**Tamanna Raju Shaikh**  
B.Tech Computer Science & Engineering  
Sanjivani University

---

## 📜 License

This project was developed as part of **Assignment 6 – AI-Powered Security Code Reviewer** for academic purposes.
