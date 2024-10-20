from selenium.webdriver.common.by import By


class OrderHistoryPage:
    URL = 'https://stellarburgers.nomoreparties.site/account/order-history'
    load_message = (By.XPATH, '//div[text()="Загрузка..."]')