import unittest
from selenium.webdriver.support import expected_conditions as EC
from cached_tests.cart_test_no_user import CartTestsNoUser
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class CartTestsUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://demo.opencart.com')

    def test_add_item_to_cart(self):
        driver = self.driver
        def login():
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "My Account"))).click()
            driver.find_element(By.LINK_TEXT, "Login").click()
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "input-email"))).send_keys(
                'philip@example.com')
            driver.find_element(By.ID, "input-password").send_keys('testpassword' + Keys.ENTER)
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()= 'Edit your account information']")))
        login()
        CartTestsNoUser.test_add_item_to_cart(self)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    #unittest.main()
