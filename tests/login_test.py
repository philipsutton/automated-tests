import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://demo.opencart.com')
        self.frontend_link = "https//demo.opencart.com"
        self.backend_link = "https://demo.opencart.com/admin/"

    def test_login_successful(self):
        driver = self.driver
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "My Account"))).click()
        driver.find_element(By.LINK_TEXT, "Login").click()
        time.sleep(1)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys(
            'philip@example.com')
        driver.find_element(By.ID, "input-password").send_keys('testpassword' + Keys.ENTER)

        def login_successful():
            try:
                WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, "//a[text()= 'Edit your account information']")))
                return True
            except:
                return False
        self.assertTrue(login_successful(), "Cannot login")

    def test_invalid_credentials(self):
        driver = self.driver
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.LINK_TEXT, "My Account"))).click()
        driver.find_element(By.LINK_TEXT, "Login").click()
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys('philip@example.com')
        driver.find_element(By.ID, "input-password").send_keys('iiiii'+ Keys.ENTER)

        def warning_message_displayed():
            try:
                WebDriverWait(driver,2).until(EC.presence_of_element_located((By.XPATH,"//div[text()= ' Warning: No match for E-Mail Address and/or Password.']"))).click()
                return True
            except:
                return False
        self.assertTrue(warning_message_displayed())



    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    #unittest.main()
#email_form = driver.find_element(By.ID, "input-emaill")
#self.assertEqual(email_form.get_attribute('value'), 'philip@sutton.pl', "Wrong account")