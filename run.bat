@echo off

:: =========================
:: CONSTANTS / PATHS
:: =========================

set ALLURE_RESULTS=reports\allure-results
set ALLURE_HTML=reports\allure-html
set PYTEST_HTML=reports\report.html

:: =========================
:: STEP 1 - CREATE VENV
:: =========================

echo Creating Virtual Environment...

python -m venv venv

:: =========================
:: STEP 2 - ACTIVATE VENV
:: =========================

echo Activating Virtual Environment...

call venv\Scripts\activate.bat

:: =========================
:: STEP 3 - INSTALL PACKAGES
:: =========================

echo Installing Required Packages...

pip install -r requirements.txt

:: =========================
:: STEP 4 - CLEAN OLD REPORTS
:: =========================

echo Cleaning Previous Reports...

if exist %ALLURE_RESULTS% rmdir /s /q %ALLURE_RESULTS%
if exist %ALLURE_HTML% rmdir /s /q %ALLURE_HTML%
if exist %PYTEST_HTML% del %PYTEST_HTML%

:: =========================
:: STEP 5 - RUN TESTS
:: =========================

echo Running Tests...

pytest -s -v ^
--alluredir=%ALLURE_RESULTS% ^
--html=%PYTEST_HTML% --self-contained-html ^
testcases/

:: =========================
:: STEP 6 - GENERATE REPORT
:: =========================

echo Generating Allure Report...

allure generate %ALLURE_RESULTS% -o %ALLURE_HTML% --clean

:: =========================
:: STEP 7 - OPEN REPORT
:: =========================

echo Opening Allure Report...

allure open %ALLURE_HTML%

pause

