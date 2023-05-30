import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.Loginpage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_003_AddCustomer:
    baseUrl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPasswordl()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("************** Test_003_AddCustomer *****************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassword(self.password)
        self.lp.Login()
        self.logger.info("************** Login Succesful *****************")

        self.logger.info("************** staarting add customer test *****************")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("************** Providing customer information *****************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Ravi")
        self.addcust.setLastName("yuga")
        self.addcust.setGender("Male")
        self.addcust.setDOB("08/22/1993")
        self.addcust.setCompanyname("infosys")
        self.addcust.setCustomerRole("Guest")
        self.addcust.setVender("Vendor 2")
        self.addcust.setAdminComment("This is for testing")
        self.addcust.clickSave()

        self.logger.info("**saving customer info***")

        self.logger.info("** Add customer validation started ***")
        self.meg=self.driver.find_element(By.TAG_NAME,"body").text
        print(self.meg)
        if 'The new customer has been added successfully.' in self.meg:
            assert True == True
            self.logger.info("** Add customer test passed ***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addcust_scr.png")
            self.logger.info("** Add customer test failed ***")
            assert False == False

        self.driver.close()
        self.logger.info("** Editing home page title ***")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))







