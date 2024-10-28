from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/login'
    link_recover_pass = (By.XPATH, '//a[text()="Восстановить пароль"]')
    button_login = (By.XPATH, '//button[text()="Войти"]')
    field_email = (By.XPATH, '//label[text()="Email"]/parent::div/input')
    field_pass = (By.XPATH, '//label[text()="Пароль"]/parent::div/input')

    # def __init__(self, driver):
    #     self.driver = driver

    def open_page(self):
        self.driver_get(LoginPage.URL)

    def click_link_recover(self):
        self.click_element(LoginPage.link_recover_pass)

    def wait_button_login(self):
        self.wait_element(self.button_login)


    def check_self_current_url(self):
        assert self.current_url() == LoginPage.URL
    # def wait_element(self, el_xpath):
    #     WebDriverWait(self.driver, 5).until(
    #         expected_conditions.visibility_of_element_located(el_xpath))

    # def click_element(self, el_xpath):
    #     self.wait_element(el_xpath)
    #     self.driver.find_element(*el_xpath).click()
    #
    # def ac_click_element(self, el_xpath):
    #     self.wait_element(el_xpath)
    #     element = self.driver.find_element(*el_xpath)
    #     actions = ActionChains(self.driver)
    #     actions.click(element).perform()
    #
    # def fill_field(self, el_xpath, load_data):
    #     self.wait_element(el_xpath)
    #     self.ac_click_element(el_xpath)
    #     self.driver.find_element(*el_xpath).send_keys(load_data)
