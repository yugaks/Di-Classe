import time

import pytest
from selenium import webdriver
from pageObjects.Loginpage import LoginPage
from utilities import XLUtilities
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/Logindataexl.xlsx"
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("******* Test_002_DDT_Login ********")
        self.logger.info("******* login test is started ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.rows=XLUtilities.getRowCount(self.path,'Sheet1')

        st_status=[]

        for r in range(2,self.rows+1):
            self.user=XLUtilities.readData(self.path,'sheet1',r,1)
            self.password = XLUtilities.readData(self.path,'sheet1',r,2)
            self.exp=XLUtilities.readData(self.path, 'sheet1', r,3)

            self.lp.SetUserName(self.user)
            self.lp.SetPassword(self.password)
            self.lp.Login()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info("***passed**")
                    self.lp.Logout()
                    st_status.append("pass")
                elif self.exp=='Fail':
                    self.logger.info("***Failed**")
                    self.lp.Logout()
                    st_status.append("fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("***passed**")
                    self.lp.Logout()
                elif self.exp=='Fail':
                    self.logger.info("***passed**")
                    st_status.append("pass")

        if 'Fail' not in st_status:
            self.logger.info("****Login DDT passed***")
            self.driver.close()
            assert True
        else:
            self.logger.info("****Login DDT failed***")
            self.driver.close()
            assert False




