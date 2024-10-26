from selenium.webdriver.common.by import By


class IngrdientDetailsPage:
    URLpart = 'https://stellarburgers.nomoreparties.site/ingredient/'
    header_text = (By.XPATH, '//h2[text()="Детали ингредиента"]')
    button_close_x = (By.XPATH, '//section[contains(@class, "open")]//button[contains(@class,"close")]')
    flag_window_is_active = (By.XPATH, '//section[contains(@class, "open")]')
