import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    # Add Customer page
    lnkcusomer_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomer_menuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath="//a[normalize-space()='Add new']"
    texEmail_xpath="//input[@id='Email']"
    texPassword_xpath="//input[@id='Password']"
    texFirstName_xpath ="//input[@id='FirstName']"
    texLastName_xpath="//input[@id='LastName']"
    rdMaleGender_xpath="//input[@id='Gender_Male']"
    rdFemaleGender_xpath="//input[@id='Gender_Female']"
    texDOB_xpath="//input[@id='DateOfBirth']"
    texCompanyName_xpath="//input[@id='Company']"
    che_xpath="//input[@id='IsTaxExempt']"
    drpNewsletter_xpath="//div[@class='input-group-append']//div[@role='listbox']"
    texCustomerRole_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemAdministration_xpath="//span[normalize-space()='Administrators']"
    lstitemForumModerators_xpath="//span[normalize-space()='Forum Moderators']"
    lstitemGuests_xpath="//span[normalize-space()='Guests']"
    lstitemRegistered_xpath="//span[normalize-space()='Registered']"
    lstitemVendors_xpath="//span[normalize-space()='Vendors']"
    drpVender_xpath="//select[@id='VendorId']"
    texAdminComment_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkcusomer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.texEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.texPassword_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.texFirstName_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.texLastName_xpath).send_keys(lastname)

    def setGender(self,gender):
        if gender=="Male":
            self.driver.find_element(By.XPATH,self.rdMaleGender_xpath).click()
        elif gender=="Female":
            self.driver.find_element(By.XPATH,self.rdFemaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.rdMaleGender_xpath).click()

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH,self.texDOB_xpath).send_keys(dob)

    def setCompanyname(self,companyname):
        self.driver.find_element(By.XPATH,self.texCompanyName_xpath).send_keys(companyname)

    def clickCheckBox(self,checkbox):
        self.driver.find_element(By.XPATH,self.che_xpath).click()

    def setNewsletter(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpNewsletter_xpath))
        drp.select_by_visible_text(value)

    def setCustomerRole(self,role):
        self.driver.find_element(By.XPATH,self.texCustomerRole_xpath).click()
        time.sleep(3)
        if role =="Administrators":
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemAdministration_xpath)
        elif role=="ForumModerators":
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemForumModerators_xpath)
        elif role=="Guests":
            self.driver.find_element(By.XPATH,"//span[@title='delete']").click()
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        elif role=="Registered":
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role=="Registered":
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role=="Vendors":
            self.listitem=self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)

        else:
            self.listitem=self.driver.find_element(By.XPATH,"//span[@title='delete']")
            time.sleep(3)
            self.listitem.click()
            # self.driver.execute_script("argumenets[0].click();", self.listitem)

    def setVender(self,value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpVender_xpath))
        drp.select_by_visible_text(value)

    def setAdminComment(self,Admincommment):
        self.driver.find_element(By.XPATH,self.texAdminComment_xpath).send_keys(Admincommment)

    def clickSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()





























