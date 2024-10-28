from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
class OrderHistoryPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/account/order-history'
    load_message = (By.XPATH, '//div[text()="Загрузка..."]')

    @allure.step('wait load message off')
    def wait_load_message_off(self):
        self.wait_element_off(self.load_message)

    @allure.step('check self current url')
    def check_self_current_url(self):
        assert self.current_url() == OrderHistoryPage.URL

