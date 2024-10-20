from selenium.webdriver.common.by import By

class IngrdientDetailsPage:
    URLpart = 'https://stellarburgers.nomoreparties.site/ingredient/'
    header_text = (By.XPATH, '//h2[text()="Детали ингредиента"]')