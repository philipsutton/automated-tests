import time
import unittest
from selenium.webdriver.support import expected_conditions as EC
from tests.cart_test_no_user import CartTestsNoUser
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://demo.opencart.com')

    def test_add_item_to_cart(self):

        def navigate_to_main_page():
            try:
                # navigate to page command
                return True
            except:
                return False

        def search_item():
            try:
                # navigate to page command
                return True
            except:
                return False

        self.assertTrue(navigate_to_main_page(), "Navigation to main page failed")
        self.assertTrue(search_item(), "Unable to find item")


    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
