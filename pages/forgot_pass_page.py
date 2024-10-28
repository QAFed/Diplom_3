from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class ForgotPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/forgot-password'
    button_recovery =  (By.XPATH, '//button[text()="Восстановить"]')
    field_email = (By.XPATH, '//label[text()="Email"]/parent::div/input')

    def open_page(self):
        self.driver_get(ForgotPage.URL)

    def wait_button_recovery(self):
        self.wait_element(ForgotPage.button_recovery)

    def check_self_current_url(self):
        assert self.current_url() == ForgotPage.URL

    def fill_email_test_data(self):
        # self.wait_element(ForgotPage.field_email)
        self.fill_field(ForgotPage.field_email, 'fedtest@disp.ru')

    def click_button_recovery(self):
        self.click_element(ForgotPage.button_recovery)


    # def __init__(self, driver):
    #     self.driver = driver

    # def open_page(self):
    #     self.driver.get(self.URL)

    # def wait_element(self, el_xpath):
    #     WebDriverWait(self.driver, 5).until(
    #         expected_conditions.visibility_of_element_located(el_xpath))

    # def click_element(self, el_xpath):
    #     self.wait_element(el_xpath)
    #     self.driver.find_element(*el_xpath).click()

    # def ac_click_element(self, el_xpath):
    #     self.wait_element(el_xpath)
    #     element = self.driver.find_element(*el_xpath)
    #     actions = ActionChains(self.driver)
    #     actions.click(element).perform()

    # def fill_field(self, el_xpath, load_data):
    #     self.wait_element(el_xpath)
    #     self.driver.find_element(*el_xpath).click()
    #     self.driver.find_element(*el_xpath).send_keys(load_data)
