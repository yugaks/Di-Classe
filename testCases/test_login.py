import pytest
from selenium import webdriver
from pageObjects.Loginpage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPasswordl()
    logger=LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_homePageTitle(self,setup):

        self.logger.info("************** Test_001_Login *****************")
        self.logger.info("************** Verifing home page title *****************")


        self.driver=setup
        self.driver.get(self.baseUrl)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************home page title test is passed *****************")

        else:
            self.driver.save_screenshot(".\\Screeshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.info("**************home page title test is failed *****************")

            assert False
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self,setup):
        # self.logger.info("************** Verifing login test *****************")

        self.driver=setup
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        self.lp.SetUserName(self.username)
        self.lp.SetPassword(self.password)
        self.lp.Login()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("************** login test is passed *****************")
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screeshots\\"+"test_login.png")
            self.logger.info("************** login test is failed *****************")
            self.driver.close()
            assert False




