from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
from pages.header_page import HeaderElements

class PersonalPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/account/profile'
    button_order_history = (By.XPATH, '//a[text()="История заказов"]')
    button_logout = (By.XPATH, '//button[text()="Выход"]')


    def wait_button_order_history(self):
        self.wait_element(self.button_order_history)

    def click_button_order_history(self):
        self.ac_click_element(self.button_order_history)

    def click_button_logout(self):
        self.ac_click_element(self.button_logout)

    def click_button_order_list(self):
        self.ac_click_element(HeaderElements.button_order_list)

    def check_self_current_url(self):
        assert self.current_url() == PersonalPage.URL

    # def __init__(self, driver):
    #     self.driver = driver
    #
    # def wait_element(self, el_xpath):
    #     WebDriverWait(self.driver, 5).until(
    #         expected_conditions.visibility_of_element_located(el_xpath))
    #
    # def click_element(self, el_xpath):
    #     self.wait_element(el_xpath)
    #     self.driver.find_element(*el_xpath).click()
