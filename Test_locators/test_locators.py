class LoginPage_Locators:
    def __init__(self):
        pass
    username_loc_name = "username"
    password_loc_name = "password"
    login_loc_btn_xpath = '//button[@type="submit"]'
    dashboard_page = "//h6[text()='Dashboard']"
    invalid_loc_text_xpath = "//p[text()='Invalid credentials']"


class Dashboardpage_Locators:
    pim_loc_menu_xpath = '//a[@href="/web/index.php/pim/viewPimModule"]'


class AdminPage_Locators:
    admin_loc_xpath = '//a[@href="/web/index.php/admin/viewAdminModule"]'
    username_loc_textbox_xpath ='(//input[@class="oxd-input oxd-input--active"])[2]'
    userrole_loc_dropdown_xpath = "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[1]"
    employeename_loc_textbox_xpath = '//input[@placeholder="Type for hints..."]'
    status_loc_dropdown_xpath = "(//i[@class='oxd-icon bi-caret-down-fill oxd-select-text--arrow'])[2]"
    add_user_loc_xpath = '//button[@type="button" and @class="oxd-button oxd-button--medium oxd-button--secondary"]'
    # dashboard_page = "//h6[text()='Dashboard']"

class PimPage_EmployeeList_Locators:
    # pim_loc_menu_xpath = '//a[@href="/web/index.php/pim/viewPimModule"]'
    empname_loc_textbox_xpath = '(//input[@placeholder="Type for hints..."])[1]'
    search_loc_btn_xpath = '//button[@type="submit"]'
    edit_loc_btn_xpath = '//button[@class="oxd-icon-button oxd-table-cell-action-space"][2]'
    # delete_loc_btn_xpath = '(//button[@type="button"])[5]'
    delete_loc_btn_xpath = '//button[@class ="oxd-icon-button oxd-table-cell-action-space"][1]'
    alert_loc_yesbtn_xpath = '//button[@class ="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]'

class PimAddEmployee_Locators:
    addemp_loc_tab_xpath = "//a[text()='Add Employee']"
    fname_loc_text_xpath = "//input[@name='firstName']"
    midname_loc_text_xpath = "//input[@name='middleName']"
    lastname_loc_text_xpath = "//input[@name='lastName']"
    empid_loc_text_xpath = '(//input[@class="oxd-input oxd-input--active"])[2]'
    save_loc_btn_xpath = '//button[@type="submit"]'

class MyinfoPage_Locators:
    # Personal Field Locators
    firstname_loc_text_name = 'firstName'
    middlename_loc_text_name = 'middleName'
    lastname_loc_text_name = 'lastName'
    nickname_loc_text_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[4]'
    empid_loc_text_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[5]'
    otherid_loc_text_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[6]'
    driverlicense_loc_text_xpath ='//*[@class="oxd-input oxd-input--active"]//following::input[7]'
    liceexpiry_loc_cal_xpath ='(//input[@placeholder="yyyy-mm-dd"])[1]'
    ssnnum_loc_text_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[9]'
    sinnum_loc_text_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[10]'
    nationality_loc_ddown_xpath ='//*[@class="oxd-select-text-input"]//following::div[1]'
    nationality_loc_selectcountry_xpath = '(//div[@role="listbox"]//child::div)[3]'
    marital_loc_ddown_xpath = '//*[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]//following::div[8]'
    marital_loc_select_xpath = '(//div[@role="listbox"]//child::div)[4]'
    # dob_loc_cal_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[11]'
    dob_loc_cal_xpath = '(//input[@ placeholder="yyyy-mm-dd"])[2]'
    # gender_loc_xpath = '//input[@value="2"]' # This locator doesnt work,ElementInterceptedException
    gender_loc_xpath = '(//span[@class="oxd-radio-input oxd-radio-input--active --label-right oxd-radio-input"])[2]'
    # military_loc_xpath = '//input[@fdprocessedid="n89495"]' #This xpath failed,NosuchElement exception
    # military_loc_xpath = '//*[@class="oxd-input oxd-input--active"]//following::input[14]'
    military_loc_text_xpath = "(//input[@class='oxd-input oxd-input--active'])[10]"
    smoker_loc_radio_xpath ='//i[@class="oxd-icon bi-check oxd-checkbox-input-icon"]'
    save_personal_btn_loc_xpath ='//button[@type="submit"]'

    # Custom Field Locators
    blood_loc_ddown_xpath = '(//div[@class="oxd-select-text--after"])[3]'
    blood_loc_selecttype_xpath = "(//div[@role='listbox']//child::div)[3]"
    savecustom_loc_btn_xpath = '(//button[@type="submit"])[2]'

    #Attachments
    attachadd_loc_btn_xpath = '(//button[@type="button"])[3]'
    browse_loc_btn_xpath = '//div[@class="oxd-file-button"]'
    attachsave_loc_btn_xpath = '(//button[@type="submit"])[3]'