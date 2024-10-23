from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class OrderListPage:
    URL = 'https://stellarburgers.nomoreparties.site/feed'
    header_text = (By.XPATH, '//h1[text()="Лента заказов"]')
    load_message = (By.XPATH, '//div[text()="Загрузка..."]')

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.URL)

    def wait_element(self, el_xpath):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(el_xpath))

    def ac_click_element(self, el_xpath):
        self.wait_element(el_xpath)
        element = self.driver.find_element(*el_xpath)
        actions = ActionChains(self.driver)
        actions.click(element).perform()

    def click_to_card_by_number(self, order_number):
        x_path = (By.XPATH, f'//li//p[contains(text(), "{order_number}")]')
        order_card = self.driver.find_element(*x_path)
        self.wait_element(x_path)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order_card)
        self.ac_click_element(x_path)

    def check_number_order_on_open_card(self, order_number):
        num_on_card_x = (By.XPATH, f'//section[contains(@class, "opened")]//p[contains(., "{order_number}")]')
        self.wait_element(num_on_card_x)
        assert order_number in self.driver.find_element(*num_on_card_x).text