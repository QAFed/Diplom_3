from selenium.webdriver.common.by import By
from pages.forgot_pass_page import ForgotPage
from pages.base_page import BasePage
import allure


class ResetPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/reset-password'
    button_save = (By.XPATH, '//button[text()="Сохранить"]')
    field_pass = (By.XPATH, '//input[@name="Введите новый пароль"]/parent::div')
    button_pass_visible = (By.XPATH, '//div[contains(@class, "password")]/div')

    @allure.step('open page by click')
    def open_page_by_click(self):
        self.driver_get(ForgotPage.URL)
        self.ac_click_element(ForgotPage.button_recovery)

    @allure.step('wait button save')
    def wait_button_save(self):
        self.wait_element(ResetPage.button_save)

    @allure.step('assert field pass active')
    def assert_field_pass_active(self):
        assert 'active' in self.find_element(self.field_pass).get_attribute("class")

    @allure.step('check self current url')
    def check_self_current_url(self):
        assert self.current_url() == ResetPage.URL

    @allure.step('click button pass visible')
    def click_button_pass_visible(self):
        self.ac_click_element(self.button_pass_visible)
