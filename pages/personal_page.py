from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.header_page import HeaderElements
import allure


class PersonalPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/account/profile'
    button_order_history = (By.XPATH, '//a[text()="История заказов"]')
    button_logout = (By.XPATH, '//button[text()="Выход"]')

    @allure.step('wait button order history')
    def wait_button_order_history(self):
        self.wait_element(self.button_order_history)

    @allure.step('click button order history')
    def click_button_order_history(self):
        self.ac_click_element(self.button_order_history)

    @allure.step('click button logout')
    def click_button_logout(self):
        self.ac_click_element(self.button_logout)

    @allure.step('click button order list')
    def click_button_order_list(self):
        self.ac_click_element(HeaderElements.button_order_list)

    @allure.step('check self current url')
    def check_self_current_url(self):
        assert self.current_url() == PersonalPage.URL
