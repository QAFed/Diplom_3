from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class OrderHistoryPage:
    URL = 'https://stellarburgers.nomoreparties.site/account/order-history'
    load_message = (By.XPATH, '//div[text()="Загрузка..."]')
