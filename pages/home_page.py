import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from pages.order_accepted_page import OrderAcceptedPage


class HomePage:
    URL = 'https://stellarburgers.nomoreparties.site/'
    button_order = (By.XPATH, '//button[text()="Оформить заказ"]')
    header_text = (By.XPATH, '//h1[text()="Соберите бургер"]')
    icon_krator_bulka = (By.XPATH, '//img[@alt="Краторная булка N-200i"]')
    icon_sous_spicy = (By.XPATH, '//img[@alt="Соус Spicy-X" and contains(@class, "BurgerIngredient")]')
    basket = (By.XPATH, '//section[contains(@class, "basket")]')
    loading_animation =(By.XPATH, '//div[contains(@class, "opened")]/img[@alt="loading animation"]')

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.URL)

    def wait_element(self, el_xpath):
        WebDriverWait(self.driver, 10).until(
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

    def wait_on_off_load_animation(self):
        self.wait_element(HomePage.loading_animation)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(HomePage.loading_animation))

    def create_new_order(self):
        self.add_ingredient_in_burger(HomePage.icon_krator_bulka)
        self.ac_click_element(HomePage.button_order)
        self.wait_on_off_load_animation()
        self.wait_element(OrderAcceptedPage.order_number)
        order_number = self.driver.find_element(*OrderAcceptedPage.order_number).text
        self.ac_click_element(OrderAcceptedPage.button_close_x)
        return order_number