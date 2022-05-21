import time
import unittest
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from xmlrunner import xmlrunner


class CartTestsNoUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://demo.opencart.com')

    def test_add_item_to_cart(self):
        driver = self.driver

        def item_added():
            try:
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Desktops"))).click()
                driver.find_element(By.XPATH, "//a[starts-with(text(),'Mac')]").click()
                driver.find_element(By.XPATH, "//span[contains(text(),'Add to Cart')]").click()
               # WebDriverWait(driver, 5).until(
                #    EC.presence_of_element_located((By.XPATH, "//td[contains(text(),'122')]")))
                return True
            except:
                return False
        self.assertTrue(item_added(), "Error")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output = 'reports'),failfast=False,buffer=False,catchbreak=False)

