from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from pages.order_accepted_page import OrderAcceptedPage
from pages.header_page import HeaderElements
from pages.ingredient_detail import IngrdientDetailsPage
import re
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/'
    button_order = (By.XPATH, '//button[text()="Оформить заказ"]')
    header_text = (By.XPATH, '//h1[text()="Соберите бургер"]')
    icon_krator_bulka = (By.XPATH, '//img[@alt="Краторная булка N-200i"]')
    icon_sous_spicy = (By.XPATH, '//img[@alt="Соус Spicy-X" and contains(@class, "BurgerIngredient")]')
    basket = (By.XPATH, '//section[contains(@class, "basket")]')
    loading_animation = (By.XPATH, '//div[contains(@class, "opened")]/img[@alt="loading animation"]')

    def open_page(self):
        self.driver_get(HomePage.URL)

    def click_button_personal_account(self):
        self.ac_click_element(HeaderElements.button_personal_account)

    def click_button_order_list(self):
        self.ac_click_element(HeaderElements.button_order_list)

    def click_button_order(self):
        self.ac_click_element(self.button_order)

    def click_button_crater_bulka(self):
        self.ac_click_element(self.icon_krator_bulka)

    def wait_header_text(self):
        self.wait_element(self.header_text)

    def check_self_current_url(self):
        assert self.current_url() == HomePage.URL
    # def __init__(self, driver):
    #     self.driver = driver

    # def open_page(self):
    #     self.driver.get(self.URL)

    # def wait_element(self, el_xpath):
    #     WebDriverWait(self.driver, 10).until(
    #         expected_conditions.visibility_of_element_located(el_xpath))

    # def wait_element_off(self, el_xpath):
    #     WebDriverWait(self.driver, 10).until(
    #         expected_conditions.invisibility_of_element_located(el_xpath))

    # def click_element(self, el_xpath):
    #     self.wait_element(el_xpath)
    #     self.driver.find_element(*el_xpath).click()

    def get_value(self, x_path):
        self.wait_element(x_path)
        return self.driver.find_element(*x_path).text

    # def ac_click_element(self, el_xpath):
    #     self.wait_element(el_xpath)
    #     element = self.driver.find_element(*el_xpath)
    #     actions = ActionChains(self.driver)
    #     actions.click(element).perform()

    def add_ingredient_in_burger(self, el_xpath):
        self.wait_element(el_xpath)
        element = self.driver.find_element(*el_xpath)
        self.wait_element(HomePage.basket)
        basket = self.driver.find_element(*HomePage.basket)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element, basket).perform()

    def add_krat_bulka_in_burger(self):
        self.add_ingredient_in_burger(self.icon_krator_bulka)

    def check_counter_ingredient(self, el_xpath, expect_count):
        counter_xpath = (By.XPATH, f'{el_xpath[1]}/parent::a/div/p[contains(@class, "counter")]')
        self.wait_element(counter_xpath)
        actual_count = self.driver.find_element(*counter_xpath).text
        assert actual_count == expect_count

    def wait_on_off_load_animation(self):
        self.wait_element(HomePage.loading_animation)
        self.wait_element_off(HomePage.loading_animation)

    def create_new_order(self):
        self.add_ingredient_in_burger(HomePage.icon_krator_bulka)
        self.ac_click_element(HomePage.button_order)
        self.wait_on_off_load_animation()
        self.wait_element(OrderAcceptedPage.order_number)
        order_number = self.driver.find_element(*OrderAcceptedPage.order_number).text
        self.ac_click_element(OrderAcceptedPage.button_close_x)
        return order_number

    # def wait_digits_after_change(self, x_path):
    #     return WebDriverWait(self.driver, 10).until(
    #         lambda d: re.match(r'^\d+$', d.find_element(*x_path).text) is not None)

    def check_no_active_window_ingred_details(self):
        assert self.find_elements(IngrdientDetailsPage.flag_window_is_active) == []

    def check_active_window_accept_order(self):
        assert self.find_elements(OrderAcceptedPage.flag_window_is_active) != []