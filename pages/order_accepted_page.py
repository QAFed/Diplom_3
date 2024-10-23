from selenium.webdriver.common.by import By

class OrderAcceptedPage:
    order_number = (By.XPATH, '//section[contains(@class, "opened")]/div/div/h2')
    flag_window_is_active = (By.XPATH, '//section[contains(@class, "opened")]')
    button_close_x = (By.XPATH, '//section[contains(@class, "open")]//button[contains(@class,"close")]')