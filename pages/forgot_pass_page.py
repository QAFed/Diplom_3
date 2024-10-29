import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ForgotPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
    button_recovery = (By.XPATH, '//button[text()="Восстановить"]')
    field_email = (By.XPATH, '//label[text()="Email"]/parent::div/input')

    @allure.step('open page')
    def open_page(self):
        self.driver_get(ForgotPage.URL)

    @allure.step('wait button recovery')
    def wait_button_recovery(self):
        self.wait_element(ForgotPage.button_recovery)

    @allure.step('check self current url')
    def check_self_current_url(self):
        assert self.current_url() == ForgotPage.URL

    @allure.step('fill email test data')
    def fill_email_test_data(self):
        self.fill_field(ForgotPage.field_email, 'fedtest@disp.ru')

    @allure.step('click button recovery')
    def click_button_recovery(self):
        self.click_element(ForgotPage.button_recovery)
