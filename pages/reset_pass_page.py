from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class ResetPage:
    URL = 'https://stellarburgers.nomoreparties.site/reset-password'
    button_save =  (By.XPATH, '//button[text()="Сохранить"]')

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.URL)

    def wait_element(self, el_xpath):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(el_xpath))
