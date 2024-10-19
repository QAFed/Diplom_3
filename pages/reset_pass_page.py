from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.forgot_pass_page import ForgotPage
from selenium.webdriver.common.action_chains import ActionChains

class ResetPage:
    URL = 'https://stellarburgers.nomoreparties.site/reset-password'
    button_save =  (By.XPATH, '//button[text()="Сохранить"]')
    field_pass = (By.XPATH, '//input[@name="Введите новый пароль"]/parent::div')
    button_pass_visible = (By.XPATH, '//div[contains(@class, "password")]/div')


    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(ForgotPage.URL)
        self.click_element(ForgotPage.button_recovery)

    def wait_element(self, el_xpath):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(el_xpath))

    def click_element(self, el_xpath):
        self.wait_element(el_xpath)
        self.driver.find_element(*el_xpath).click()

    def assert_field_pass_active(self):
        assert 'active' in self.driver.find_element(*self.field_pass).get_attribute("class")

    def ac_click_element(self, el_xpath):
        self.wait_element(el_xpath)
        element = self.driver.find_element(*el_xpath)
        actions = ActionChains(self.driver)
        actions.click(element).perform()


