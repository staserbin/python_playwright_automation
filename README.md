# Test Automation Framework

This project is a test automation framework built with:

- **Python 3.12+**
- **Pytest** – test runner
- **Playwright** – browser automation
- **Allure** – rich and interactive test reports
- **pytest-html** – lightweight HTML report
- **Page Object Model (POM)** – clean and scalable test structure

---

## Installation

1. **Create and activate a virtual environment** (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```

2. **Install project dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
   
3. **Install Allure Pytest plugin:**

    ```bash
    pip install allure-pytest
    ```

4. **Install Allure CLI (used to serve the report):**

    ```bash
    brew install allure
    ```

## Running Tests

1. **All tests can be executed via the provided shell script:**

    ```bash
    ./run_tests.sh
    ```
   
## Viewing Reports

1. **After running tests, use the following command to launch the Allure report in your browser:**

    ```bash
    allure serve reports/allure-results
    ```

2. **An additional lightweight pytest HTML report is generated here:**

    ```bash
    reports/report.html
    ```
