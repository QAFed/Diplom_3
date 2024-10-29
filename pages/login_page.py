from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/login'
    link_recover_pass = (By.XPATH, '//a[text()="Восстановить пароль"]')
    button_login = (By.XPATH, '//button[text()="Войти"]')
    field_email = (By.XPATH, '//label[text()="Email"]/parent::div/input')
    field_email_cl = (By.XPATH, '//label[text()="Email"]/parent::div')
    field_pass = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')

    @allure.step('open page')
    def open_page(self):
        self.driver_get(LoginPage.URL)

    @allure.step('click link recover')
    def click_link_recover(self):
        self.click_element(LoginPage.link_recover_pass)

    @allure.step('fill field email')
    def fill_field_email(self, t_data):
        self.ac_click_element(self.field_email_cl)
        self.fill_field(self.field_email, t_data)

    @allure.step('fill field pass')
    def fill_field_pass(self, t_data):
        self.ac_click_element(self.field_pass)
        self.fill_field(self.field_pass, t_data)

    @allure.step('wait button login')
    def wait_button_login(self):
        self.wait_element(self.button_login)

    @allure.step('click button login')
    def click_button_login(self):
        self.click_element(self.button_login)

    @allure.step('check self current url')
    def check_self_current_url(self):
        assert self.current_url() == LoginPage.URL
