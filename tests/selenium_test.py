import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep

class TestSelenium(unittest.TestCase):
    
    def setUp(self):
        firefox_options = Options()
        firefox_options.add_argument("--headless")  # Enable headless mode
        self.browser = webdriver.Firefox(executable_path="./drivers/geckodriver", options=firefox_options)

    def test_acceptable_city_with_space_input(self):
        browser = self.browser
        browser.get('http://127.0.0.1:5000/')
        location = browser.find_element_by_id('location')
        location.send_keys('tel aviv')
        submitButton = browser.find_element_by_css_selector('input[type="submit"]')
        submitButton.send_keys(Keys.ENTER)
        sleep(2)
        assert browser.title == "Weather Home"

    def test_acceptable_city_with_typo_input(self):
        browser = self.browser
        browser.get('http://127.0.0.1:5000/')
        location = browser.find_element_by_id('location')
        location.send_keys('gamat gan')
        submitButton = browser.find_element_by_css_selector('input[type="submit"]')
        submitButton.send_keys(Keys.ENTER)
        sleep(2)
        assert browser.title == "Weather Home"

    def test_acceptable_city_without_space_input(self):
        browser = self.browser
        browser.get('http://127.0.0.1:5000/')
        location = browser.find_element_by_id('location')
        location.send_keys('haifa')
        submitButton = browser.find_element_by_css_selector('input[type="submit"]')
        submitButton.send_keys(Keys.ENTER)
        sleep(2)
        assert browser.title == "Weather Home"

    def test_acceptable_country_input(self):
        browser = self.browser
        browser.get('http://127.0.0.1:5000/')
        location = browser.find_element_by_id('location')
        location.send_keys('israel')
        submitButton = browser.find_element_by_css_selector('input[type="submit"]')
        submitButton.send_keys(Keys.ENTER)
        sleep(2)
        assert browser.title == "Weather Home"

    def test_unacceptable_empty_input(self):
        browser = self.browser
        browser.get('http://127.0.0.1:5000/')
        submitButton = browser.find_element_by_css_selector('input[type="submit"]')
        submitButton.send_keys(Keys.ENTER)
        sleep(2)
        assert browser.title == "Weather Error"

    def test_unacceptable_numbers_home_input(self):
        browser = self.browser
        browser.get('http://127.0.0.1:5000/')
        location = browser.find_element_by_id('location')
        location.send_keys('1234')
        submitButton = browser.find_element_by_css_selector('input[type="submit"]')
        submitButton.send_keys(Keys.ENTER)
        sleep(2)
        assert browser.title == "Weather Home"

    def test_acceptable_numbers_error_home_input(self):
        browser = self.browser
        browser.get('http://127.0.0.1:5000/')
        location = browser.find_element_by_id('location')
        location.send_keys('sdgdfhgfjhdfsfs')
        submitButton = browser.find_element_by_css_selector('input[type="submit"]')
        submitButton.send_keys(Keys.ENTER)
        sleep(2)
        location = browser.find_element_by_id('location')
        location.send_keys('france')
        submitButton = browser.find_element_by_css_selector('input[type="submit"]')
        submitButton.send_keys(Keys.ENTER)
        sleep(2)
        assert browser.title == "Weather Home"

    def test_unacceptable_gibberish_input(self):
        browser = self.browser
        browser.get('http://127.0.0.1:5000/')
        location = browser.find_element_by_id('location')
        location.send_keys('asdqwhgfedfgh')
        submitButton = browser.find_element_by_css_selector('input[type="submit"]')
        submitButton.send_keys(Keys.ENTER)
        sleep(2)
        assert browser.title == "Weather Error"

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
