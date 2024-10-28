from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
import allure
class RegisterPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/register'

    field_name = (By.XPATH, '//label[text()="Имя"]/parent::div/input')
    field_email = (By.XPATH, '//label[text()="Email"]/parent::div/input')
    field_pass = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')
    button_registrer = (By.XPATH, '//button[text()="Зарегистрироваться"]')

    # def __init__(self, driver):
    #     self.driver = driver
    #
    # def open_page(self):
    #     self.driver.get(self.URL)
    @allure.step('open page')
    def open_page(self):
        self.driver_get(RegisterPage.URL)
    #
    # def wait_element(self, el_xpath):
    #     WebDriverWait(self.driver, 5).until(
    #         expected_conditions.visibility_of_element_located(el_xpath))
    #
    # def click_element(self, el_xpath):
    #     self.wait_element(el_xpath)
    #     self.driver.find_element(*el_xpath).click()
    #
    # def fill_field(self, el_xpath, load_data):
    #     self.wait_element(el_xpath)
    #     self.driver.find_element(*el_xpath).click()
    #     self.driver.find_element(*el_xpath).send_keys(load_data)
