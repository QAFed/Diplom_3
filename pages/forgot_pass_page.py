from selenium.webdriver.common.by import By

class ForgotPage:
    URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
    button_recovery =  [By.XPATH, '//button[text()="Восстановить"]']

    def __init__(self, driver):
        self.driver = driver

