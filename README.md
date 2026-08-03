# Selenium Web Automation Testing
![Selenium CI](https://github.com/balla930510-cmd/selenium-test/actions/workflows/ci.yml/badge.svg)

This project demonstrates web UI automation testing using **Python, Selenium WebDriver, and Pytest**.

The project implements a maintainable Selenium automation framework using the **Page Object Model (POM)** design pattern, **Explicit Wait**, reusable **BasePage methods**, Pytest fixtures, and **GitHub Actions CI**.

---

## ✨ Features

- Login Automation Testing
- Form Interaction Testing
- Button Interaction Testing
- Page Object Model (POM)
- BasePage Architecture
- Explicit Wait with WebDriverWait
- Reusable Selenium Methods
- Pytest Fixture
- Assertion Verification
- Automatic Failure Screenshot
- Timestamped Screenshot Naming
- GitHub Actions CI
- CI Screenshot Artifact

---

## 🛠 Technologies

- Python 3.13.9
- Selenium 4.46.0
- Pytest 8.4.2
- Google Chrome
- ChromeDriver
- Git
- GitHub Actions
- Page Object Model (POM)

---

## 📂 Project Structure

```text
selenium-test/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── form_page.py
│   └── button_page.py
│
├── test/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_form.py
│   └── test_button.py
│
├── screenshots/
│
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```
---

## 🏗 Test Architecture

```text
                    GitHub Actions
                          │
                          ▼
                    Pytest Test Cases
                          │
                          ▼
                   Page Object Model
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
        LoginPage     FormPage    ButtonPage
             │            │            │
             └────────────┼────────────┘
                          ▼
                      BasePage
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
          click()    send_keys()   get_attribute()
                          │
                          ▼
                   Explicit Wait
                          │
                          ▼
                  Selenium WebDriver
                          │
                          ▼
                    Chrome Browser
                          │
                          ▼
                   Target Website
                          │
                          ▼
                     Assertions
                          │
                          ▼
                    Test Result
```

---

## 🧩 Framework Design
### Page Object Model

- LoginPage
- FormPage
- ButtonPage
---

```markdown
### BasePage

`BasePage` provides reusable Selenium operations shared across all Page Objects.

Common methods include:

- `click()` – Click an element after waiting for it to be clickable.
- `send_keys()` – Enter text into an input field.
- `get_text()` – Retrieve visible element text.
- `get_attribute()` – Retrieve an element attribute.
- `wait_for_element()` – Wait for an element to become visible.
- `wait_for_clickable()` – Wait for an element to become clickable.


```markdown
### Explicit Wait

The framework uses Selenium `WebDriverWait` and Expected Conditions to improve test stability and avoid unnecessary fixed delays.

Example:

```python
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(locator)
)
```
```markdown
### Why Page Object Model?

The Page Object Model separates test logic from page-specific UI interactions.

This provides:

- Better code maintainability
- Reduced code duplication
- Reusable page methods
- Easier locator maintenance
- Cleaner test cases
```


## 🔧 Installation
## Clone the repository:
```bash
git clone https://github.com/balla930510-cmd/selenium-test.git
```
## Navigate to the project:
```bash
cd selenium-test
```

## Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 💻 Test Environment

| Item | Version |
|------|---------|
| Local OS | Windows 11 |
| Local Python | 3.13.9 |
| CI Python | 3.12 |
| Selenium | 4.46.0 |
| Pytest | 8.4.2 |
| Browser | Google Chrome |
| WebDriver | Selenium Manager |

## 🚀 Selenium Automation Testing

### Test Coverage

- Login Testing
- Form Testing
- Button Testing

---

## 📋 Test Cases

| Test Case | Description |
|-----------|-------------|
| TC001 | Login Success |
| TC002 | Invalid Username |
| TC003 | Invalid Password |

---

## ▶ Run Tests

```bash
pytest
```

---

## 🔄 Continuous Integration
## The CI workflow performs:
```
Push / Pull Request
        ↓
Checkout Repository
        ↓
Setup Python
        ↓
Install Dependencies
        ↓
Run Pytest
        ↓
Test Result
```
## Workflow file:
```bash
.github/workflows/ci.yml
```
## 📸 Failure Screenshot
```
screenshots/
└── test_login_success_20260802_221530.png
```

## 📦 GitHub Actions Artifact

When a test fails, Selenium automatically captures a screenshot.

The screenshot is saved with the test name and timestamp:

```text
screenshots/
└── test_login_success_20260802_221530.png
```
## ✅ Test Result Summary

| Item | Result |
|------|--------|
| Total Test Cases | 3 |
| Passed | 3 |
| Failed | 0 |
| Success Rate | 100% |

---

## 📸 Test Execution Results

### Button Test

![Button Test](screenshots/button_test.png)

---

### Form Test

![Form Test](screenshots/form_test.png)

---

### Login Test

![Login Test](screenshots/login_test.png)

---

## 🔍 Login Test Details

### TC001 – Login Success

**Expected Result**

User successfully logs into the system.

![Login Success](screenshots/login_success.png)

---

### TC002 – Invalid Username

**Expected Result**

Display the message:

> Your username is invalid!

![Invalid Username](screenshots/login_invalid_username.png)

---

### TC003 – Invalid Password

**Expected Result**

Display the message:

> Your password is invalid!

![Invalid Password](screenshots/login_invalid_password.png)

---

## 👨‍💻 Author

Bai, Chen-Liang

Department of Mathematics  
Information Mathematics Program

Fu Jen Catholic University

GitHub: [balla930510-cmd](https://github.com/balla930510-cmd)

Email: balla930510@gmail.com

---

## 📄 License

This project is created for learning and portfolio purposes.

Copyright © 2026 Bai Chen-Liang. All rights reserved.