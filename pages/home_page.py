from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

class HomePage:
    URL = 'https://stellarburgers.nomoreparties.site/'
    button_order = (By.XPATH, '//button[text()="Оформить заказ"]')
    header_text = (By.XPATH, '//h1[text()="Соберите бургер"]')
    icon_krator_bulka = (By.XPATH, '//img[@alt="Краторная булка N-200i"]')
    icon_sous_spicy = (By.XPATH, '//img[@alt="Соус Spicy-X" and contains(@class, "BurgerIngredient")]')
    basket = (By.XPATH, '//section[contains(@class, "basket")]')

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

    def add_ingredient_in_burger(self, el_xpath):
        self.wait_element(el_xpath)
        element = self.driver.find_element(*el_xpath)
        self.wait_element(HomePage.basket)
        basket = self.driver.find_element(*HomePage.basket)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element, basket).perform()


    def check_counter_ingredient(self, el_xpath, expect_count):
        counter_xpath = (By.XPATH, f'{el_xpath[1]}/parent::a/div/p[contains(@class, "counter")]')
        self.wait_element(counter_xpath)
        actual_count = self.driver.find_element(*counter_xpath).text
        assert actual_count == expect_count