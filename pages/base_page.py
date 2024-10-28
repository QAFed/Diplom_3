from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import re

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.URL = None

    def driver_get(self, URL):
        self.driver.get(URL)

    def find_element(self, el_xpath):
        return self.driver.find_element(*el_xpath)

    def wait_element(self, el_xpath):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(el_xpath))

    def wait_element_off(self, el_xpath):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(el_xpath))

    def click_element(self, el_xpath):
        self.wait_element(el_xpath)
        self.find_element(el_xpath).click()

    def ac_click_element(self, el_xpath):
        self.wait_element(el_xpath)
        element = self.driver.find_element(*el_xpath)
        actions = ActionChains(self.driver)
        actions.click(element).perform()

    def fill_field(self, el_xpath, load_data):
        self.wait_element(el_xpath)
        self.find_element(el_xpath).click()
        self.find_element(el_xpath).send_keys(load_data)

    def wait_digits_after_change(self, x_path):
        return WebDriverWait(self.driver, 10).until(
            lambda d: re.match(r'^\d+$', d.find_element(*x_path).text) is not None)

    def get_value(self, x_path):
        self.wait_element(x_path)
        return self.driver.find_element(*x_path).text