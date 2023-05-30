from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    textBox_user_id="Email"
    textBox_password_id="Password"
    button_login_xpath="//button[normalize-space()='Log in']"
    link_logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def SetUserName(self,username):
        self.driver.find_element(By.ID,(self.textBox_user_id)).clear()
        self.driver.find_element(By.ID,(self.textBox_user_id)).send_keys(username)

    def SetPassword(self,password):
        self.driver.find_element(By.ID,(self.textBox_password_id)).clear()
        self.driver.find_element(By.ID,(self.textBox_password_id)).send_keys(password)

    def Login(self):
        self.driver.find_element(By.XPATH,(self.button_login_xpath)).click()

    def Logout(self):
        self.driver.find_element(By.LINK_TEXT,(self.link_logout_linktext)).click














