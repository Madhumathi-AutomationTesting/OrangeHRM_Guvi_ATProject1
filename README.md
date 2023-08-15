# OrangeHRM_Framework

Testscases dealing with Login:
=============================

1. TC_Login_1 = Successful Employee Login to OrangeHRM Portal (test_login_01_valid.py)

2. TC_Login_02 = Invalid Employee Login to OrangeHRM Portal (test_login_02_invalid.py)

Testscases dealing with PIM:
===========================
1. TC_PIM_01 = Add a new Employee in the PIM Module (test_pim_01_add.py)

2. TC_PIM_02 = Edit an existing Employee in the PIM Module (test_pim_02_edit.py)

3. TC_PIM_03 = Delete an existing Employee in the PIM Module (test_pim_03_delete.py)

PageObjects = For each Page,A CLASS has been created which contains the functions/tasks to be performed on that page 

Locators = To perform action on the webelements,we need to locate the webelements and they are defined in a separate class file,so it would be easy to maintain the code

Logs = As automation is a quick operation,it will be difficult for us to see what's opening,so its better to log our operations for better understanding 

Screenshots = Its a good practice to capture the screenshot of failed testcases.

Test data = It contains the common data which are to be used all over the testcases.

Test cases = Each testcase contains only the logic.

Though it's not recommended to use implicit wait,I have used it show the input we insert into each field.
Please check automation.log also

