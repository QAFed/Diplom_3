from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderHistoryPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/account/order-history'
    load_message = (By.XPATH, '//div[text()="Загрузка..."]')

    def wait_load_message_off(self):
        self.wait_element_off(self.load_message)

    def check_self_current_url(self):
        assert self.current_url() == OrderHistoryPage.URL

