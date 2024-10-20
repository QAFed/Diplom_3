from selenium.webdriver.common.by import By


class HeaderElements:
    button_personal_account = (By.XPATH, '//p[text()="Личный Кабинет"]')
    button_constructor = (By.XPATH, '//p[text()="Конструктор"]')
    button_order_list = (By.XPATH, '//p[text()="Лента Заказов"]')
