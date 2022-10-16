# Portofolio QA - Web Automation Testing using pytest

> a script to do login test with automation using selenium pytest

> website used (https://id.blooket.com/login)

# Requirements
- Python 3.10.6
- selenium 4.4.3
- ChromeDriver 106.0.5249.61
- pytest 7.1.3
- pytest-html 3.1.1
- pytest-html-reporter 0.2.9

# Scenario Test
![image](https://user-images.githubusercontent.com/112541317/196014905-51537fee-ef16-4e43-af92-c779c5be3aaf.png)

# Step write code
1. User imports library
2. User create a list to accommodate invalid user data named "Account"
3. User write @pytest.fixture to group steps / code that is run repeatedly and create function setup()
4. User create function test_login_success() for login successfully
5. User write @pytest.mark.parametrize to call list Account
6. User create function test_login_unsuccess() for login failed

# How to Run?
1. Open terminal
2. Make sure the file path location is correct
3. Type 'pytest -v test_tugas05.py'
4. if you want get the report, type 'pytest -v automation-login.py --html=login-report.html'
5. Then press enter

# The Result

You will see the result in Terminal: If **Success**, you will see green text with information 'PASSED'. If **Fail**, you will see red text with text with information 'FAILED'

> if you already have pytest-html you will get a report like this https://shidqiadiatma.github.io/web_automation_testing_using_pytest/login-report.html

> and if you already have pytest-html-reporter you will get a report like this https://shidqiadiatma.github.io/web_automation_testing_using_pytest/pytest_html_report.html#dashboard



