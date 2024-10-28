from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class IngrdientDetailsPage(BasePage):
    URLpart = 'https://stellarburgers.nomoreparties.site/ingredient/'
    header_text = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    button_close_x = (By.XPATH, '//section[contains(@class, "open")]//button[contains(@class,"close")]')
    flag_window_is_active = (By.XPATH, '//section[contains(@class, "open")]')

    @allure.step('wait header text')
    def wait_header_text(self):
        self.wait_element(self.header_text)

    @allure.step('check url part in current url')
    def check_url_part_in_current_url(self):
        assert IngrdientDetailsPage.URLpart in self.current_url()

    @allure.step('click button close x')
    def click_button_close_x(self):
        self.ac_click_element(self.button_close_x)