from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
    URL = 'https://stellarburgers.nomoreparties.site/'
    button_order = (By.XPATH, '//button[text()="Оформить заказ"]')
    header_text = (By.XPATH, '//h1[text()="Соберите бургер"]')
    icon_krator_bulka = (By.XPATH, '//img[@alt="Краторная булка N-200i"]')

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.URL)

    def wait_element(self, el_xpath):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(el_xpath))

    def click_element(self, el_xpath):
        self.wait_element(el_xpath)
        self.driver.find_element(*el_xpath).click()

    def ac_click_element(self, el_xpath):
        self.wait_element(el_xpath)
        element = self.driver.find_element(*el_xpath)
        actions = ActionChains(self.driver)
        actions.click(element).perform()