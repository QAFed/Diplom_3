from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class PersonalPage:
    URL = 'https://stellarburgers.nomoreparties.site/account/profile'
    button_order_history = (By.XPATH, '//a[text()="История заказов"]')
    button_logout = (By.XPATH, '//button[text()="Выход"]')

    def __init__(self, driver):
        self.driver = driver

    def wait_element(self, el_xpath):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(el_xpath))

    def click_element(self, el_xpath):
        self.wait_element(el_xpath)
        self.driver.find_element(*el_xpath).click()
