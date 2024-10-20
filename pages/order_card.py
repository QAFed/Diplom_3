from selenium.webdriver.common.by import By

class OrderCardPage:
    order_number = (By.XPATH, '//section[contains(@class, "opened")]/div/div/p[contains(text(), "#")]')
    flag_window_is_active = (By.XPATH, '//section[contains(@class, "opened")]')