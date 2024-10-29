from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class RegisterPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/register'

    field_name = (By.XPATH, '//label[text()="Имя"]/parent::div/input')
    field_email = (By.XPATH, '//label[text()="Email"]/parent::div/input')
    field_pass = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')
    button_registrer = (By.XPATH, '//button[text()="Зарегистрироваться"]')

    @allure.step('open page')
    def open_page(self):
        self.driver_get(RegisterPage.URL)

    @allure.step('wait button register')
    def wait_button_register(self):
        self.wait_element(self.button_registrer)

    @allure.step('click button register')
    def click_button_register(self):
        self.ac_click_element(self.button_registrer)

    @allure.step('fill field name')
    def fill_field_name(self, t_data):
        self.wait_element(self.field_name)
        self.ac_click_element(self.field_name)
        self.fill_field(self.field_name, t_data)

    @allure.step('fill field email')
    def fill_field_email(self, t_data):
        self.ac_click_element(self.field_email)
        self.fill_field(self.field_email, t_data)

    @allure.step('fill field pass')
    def fill_field_pass(self, t_data):
        self.ac_click_element(self.field_pass)
        self.fill_field(self.field_pass, t_data)
