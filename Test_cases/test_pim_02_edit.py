from PageObjects.login_page_POM import LoginPage_Actions
from PageObjects.pim_page_edit_employee_POM import Pimpage_Edit_Actions
from PageObjects.myinfo_page_POM import MyinfoPage_Actions
from Test_utilities.customLogger import logGen
from time import sleep
class Test_pim_employee_edit:


    def test_pim_search(self,setup_browser):
        """
        Testcase to search for an employee
        """
        self.driver = setup_browser
        logs_obj = logGen.logger()
        LoginPage_Actions_obj = LoginPage_Actions(self.driver)
        pimpage_actions_obj = Pimpage_Edit_Actions(self.driver)
        myinfopage_obj = MyinfoPage_Actions(self.driver)

        LoginPage_Actions_obj.login_to_orangehrm_valid()
        logs_obj.info("successfull Login")

        pimpage_actions_obj.pim_click()
        logs_obj.info("PIM clicked")

        pimpage_actions_obj.employee_pim_search()
        logs_obj.info("Employee search done")
        sleep(2)
        self.driver.implicitly_wait(5)

        pimpage_actions_obj.employee_pim_edit_click()
        logs_obj.info("Employee EDIT button clicked")
        sleep(5)
        self.driver.implicitly_wait(5)

        # myinfopage_obj.EnterFirstName_myinfo("Madhu")
        # logs_obj.info("Entered First Name")
        # self.driver.implicitly_wait(1)

        myinfopage_obj.EnterMiddleName_myinfo("XXXXX")
        logs_obj.info("Entered Middle Name")
        self.driver.implicitly_wait(1)

        myinfopage_obj.EnterLastName_myinfo("Mathiiiiiii")
        logs_obj.info("Entered Last Name")
        self.driver.implicitly_wait(1)

        myinfopage_obj.EnterNickName_myinfo("maddy")
        logs_obj.info("Entered Nick Name")
        self.driver.implicitly_wait(1)

        # myinfopage_obj.EnterEmpID_myinfo("7777777")
        # logs_obj.info("Entered EmpID")
        # self.driver.implicitly_wait(1)

        myinfopage_obj.EnterOtherID_myinfo("772345777")
        logs_obj.info("Entered OtherID")
        self.driver.implicitly_wait(1)

        myinfopage_obj.EnterDriverLicense_myinfo("LLL7777")
        logs_obj.info("Entered Driver License")
        self.driver.implicitly_wait(1)

        myinfopage_obj.EnterLicenseExpiry_myinfo("2023-07-10")
        logs_obj.info("Entered Driver Expiry")
        self.driver.implicitly_wait(1)

        myinfopage_obj.EnterSsnNum_myinfo("66666")
        logs_obj.info("Entered SSNNum")
        self.driver.implicitly_wait(1)

        myinfopage_obj.EnterSinNum_myinfo("0000")
        logs_obj.info("Entered SINNum")
        self.driver.implicitly_wait(1)

        myinfopage_obj.EnterNationality_myinfo()
        logs_obj.info("Entered Nationality")
        self.driver.implicitly_wait(1)

        myinfopage_obj.EnterMarital_myinfo()
        logs_obj.info("Entered Marital")
        self.driver.implicitly_wait(1)

        myinfopage_obj.EnterDOB_myinfo("2023-08-01")
        logs_obj.info("Entered DOB")
        self.driver.implicitly_wait(1)

        myinfopage_obj.EnterGender_myinfo()
        logs_obj.info("Entered Gender")
        self.driver.implicitly_wait(1)

        myinfopage_obj.EnterMilitary_myinfo("2023")
        logs_obj.info("Entered Military service")
        self.driver.implicitly_wait(1)

        myinfopage_obj.ClickOnSave_myinfo()
        logs_obj.info("Clicked on SAVE button in Personal Details")
        self.driver.implicitly_wait(1)

        myinfopage_obj.BloodType_myinfo()
        logs_obj.info("Selected Blood Type")
        self.driver.implicitly_wait(1)

        myinfopage_obj.ClickOnSave_custom()
        logs_obj.info("Clicked on SAVE button in Custom Field")
        self.driver.implicitly_wait(1)

        # myinfopage_obj.AttachmentsAdd_myinfo()
        # logs_obj.info("Clicked on Attachment ADD button and selected the image from the filepath and uploaded")
        # sleep(2)

