from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_locators.test_locators import PimPage_EmployeeList_Locators,MyinfoPage_Locators,Dashboardpage_Locators

class Pimpage_Edit_Actions:
    def __init__(self, driver):
        self.driver = driver
        self.pim_emp_loc_obj = PimPage_EmployeeList_Locators()
        self.myinfo_loc_obj = MyinfoPage_Locators()
        self.dashboard_loc_obj = Dashboardpage_Locators()
        self.wait = WebDriverWait(self.driver, timeout=10)

    def pim_click(self):
        """
        Clicking on PIM from the Menu
        :return:
        """
        pim_click_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.dashboard_loc_obj.pim_loc_menu_xpath)))
        pim_click_we.click()

    def employee_pim_search(self):
        """
        Searching an employee by giving input in the text field
        :return:
        """
        employeename_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_emp_loc_obj.empname_loc_textbox_xpath)))
        employeename_we.clear()
        employeename_we.send_keys("Madhu")
        emp_search_we = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.pim_emp_loc_obj.search_loc_btn_xpath)))
        emp_search_we.click()

    def employee_pim_edit_click(self):
        """
        Clicking on Edit button
        :return:
        """
        emp_pim_edit_we = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.pim_emp_loc_obj.edit_loc_btn_xpath)))
        emp_pim_edit_we.click()

