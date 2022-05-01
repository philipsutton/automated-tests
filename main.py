import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class test1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.phptravels.net/login')

    def test_1(self):
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "form-group").click()
        self.driver.find_element(By.CLASS_NAME, "form-group").send_keys(Keys.DOWN + "hello")
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "form-group mb-2").send_keys("hello")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

