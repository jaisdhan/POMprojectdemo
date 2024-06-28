import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import unittest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
import HtmlTestRunner

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ser = Service("C:/Users/jdhanjani/PycharmProjects/POMprojectDemo/drivers/chromedriver.exe")
        cls.driver = webdriver.Chrome(service=ser)

        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver

        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

        #self.driver.find_element(By.NAME, "username").send_keys("Admin")
        #self.driver.find_element(By.NAME, "password").send_keys("admin123")
        #self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        #self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i").click()
        #self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

        cls.driver.quit()

        print("Test Completed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/jdhanjani/PycharmProjects/POMprojectDemo/reports"))