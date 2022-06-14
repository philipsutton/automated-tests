import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get('https://demo.opencart.com')

    def test_login_successful(self):
        driver = self.driver

        def navigate_to_login_page():
            try:
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
                return True
            except:
                return False

        def enter_details():
            try:
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='input-email']"))).send_keys('philip@example.com')
                time.sleep(5)
                driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys('testpassword' + Keys.ENTER)
                time.sleep(60)
                driver.find_element(By.XPATH, "//button[text()='Login']").click()
                return True
            except:
                return False

        def message_shown():
            try:
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[text()= 'Edit your account information']")))
                return True
            except:
                return False

        self.assertTrue(navigate_to_login_page(), "Navigation to login page failed")
        self.assertTrue(enter_details(), "Unable to enter details in login field")
        self.assertTrue(message_shown(), "Login unsuccessful despite correct details")


    def test_login_incorrect_details(self):
        driver = self.driver

        def navigate_to_login_page():
            try:
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
                return True
            except:
                return False

        def enter_details():
            try:
                WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='input-email']"))).send_keys('philip@example.com')
                time.sleep(5)
                driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys('testpassword' + Keys.ENTER)
                time.sleep(60)
                driver.find_element(By.XPATH, "//button[text()='Login']").click()
                return True
            except:
                return False

        def message_shown():
            try:
                WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,"//div[text()= ' Warning: No match for E-Mail Address and/or Password.']")))
                return True
            except:
                return False

        self.assertTrue(navigate_to_login_page(), "Navigation to login page failed")
        self.assertTrue(enter_details(), "Unable to enter details in login field")
        self.assertTrue(message_shown(), "No message displayed")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
