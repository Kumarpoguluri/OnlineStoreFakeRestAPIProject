# Online Store Fake REST API Automation Framework

A robust API automation testing framework built using **Python**, **Pytest**, and **Requests** to validate RESTful APIs for an Online Store application using the FakeStoreAPI.

---

## 🚀 Project Overview

This project demonstrates end-to-end API automation testing practices including:

* CRUD operations testing
* Response validation
* Authentication testing
* Logging and reporting
* Reusable utilities
* Scalable framework design

The framework is designed following industry-standard automation practices and can be extended for real-world enterprise API testing.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Pytest
* **API Library:** Requests
* **Reporting:** Allure Reports
* **Logging:** Python Logging
* **IDE:** PyCharm
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```bash
OnlineStoreFakeRestAPIProject/
│
├── testcases/              # API test cases
├── utilities/              # Reusable utility functions
├── logs/                   # Execution logs
├── reports/                # Test execution reports
├── testdata/               # Test data files
├── requirements.txt        # Project dependencies
├── pytest.ini              # Pytest configuration
└── README.md
```

---

## ✅ Features Implemented

* API GET request validation
* API POST request validation
* API PUT request validation
* API DELETE request validation
* Status code verification
* Response body validation
* JSON response parsing and assertions
* Logging implementation
* HTML/Allure reporting
* Reusable helper methods
* Pytest fixtures support

---

## 🔥 APIs Covered

This framework validates APIs from:

https://fakestoreapi.com

### Modules Tested

* Products API
* Users API
* Carts API
* Authentication API

---

## ▶️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/kasikumarP/OnlineStoreFakeRestAPIProject.git
```

### 2️⃣ Navigate to Project

```bash
cd OnlineStoreFakeRestAPIProject
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Test Cases

### Run all tests

```bash
pytest -v -s
```

### Generate Allure Report

```bash
pytest --alluredir=./allure-results
```

### Open Allure Report

```bash
allure serve allure-results
```

---

## 📊 Reporting

The framework supports:

* Pytest Reports
* Allure Reports
* Console Logs
* Execution Logs

---

## 🧪 Sample Test Scenarios

* Validate product details by ID
* Create new product
* Update existing product
* Delete product
* Validate authentication token
* Verify response status codes and response body

---

## 💡 Key Learning Outcomes

* REST API automation framework design
* Pytest framework implementation
* API request handling using Requests library
* Assertions and validations
* Reporting integration
* Framework modularization
* Real-world automation practices

---

## 📌 Future Enhancements

* CI/CD integration with Jenkins
* Docker execution support
* Environment configuration management
* Parallel execution
* Data-driven testing
* Enhanced reporting dashboards

---

## 👨‍💻 Author

### Kumar Poguluri

Automation Test Engineer | Python Selenium | API Testing | Pytest | QA Automation

GitHub:
https://github.com/kasikumarP

---

## ⭐ Support

If you found this project useful, consider giving this repository a ⭐ on GitHub.
