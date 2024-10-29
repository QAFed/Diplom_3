from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.header_page import HeaderElements
import allure


class OrderListPage(BasePage):
    URL = 'https://stellarburgers.nomoreparties.site/feed'
    header_text = (By.XPATH, '//h1[text()="Лента заказов"]')
    load_message = (By.XPATH, '//div[text()="Загрузка..."]')
    list_numbers_all_orders = (By.XPATH, '//ul//li//p[contains(text(),"#")]')
    all_time_counter = (By.XPATH, '//p[contains(text(), "за все время")]/parent::div/p[contains(@class, "Order")]')
    today_counter = (By.XPATH, '//p[contains(text(), "за сегодня")]/parent::div/p[contains(@class, "Order")]')
    ready_order = (By.XPATH, '//ul[contains(@class, "Ready")]/li')

    @allure.step('open page')
    def open_page(self):
        self.driver_get(OrderListPage.URL)

    @allure.step('wait header text')
    def wait_header_text(self):
        self.wait_element(self.header_text)

    @allure.step('wait load message off')
    def wait_load_message_off(self):
        self.wait_element_off(self.load_message)

    @allure.step('wait all time counter')
    def wait_all_time_counter(self):
        self.wait_element_off(self.all_time_counter)

    @allure.step('click button constructor')
    def click_button_constructor(self):
        self.ac_click_element(HeaderElements.button_constructor)

    @allure.step('click button person accaunt')
    def click_button_person_accaunt(self):
        self.ac_click_element(HeaderElements.button_personal_account)

    @allure.step('wait digits after change ready order')
    def wait_digits_after_change_ready_order(self):
        self.wait_digits_after_change(self.ready_order)

    @allure.step('check self current url')
    def check_self_current_url(self):
        assert self.current_url() == OrderListPage.URL

    @allure.step('click to card by number')
    def click_to_card_by_number(self, order_number):
        x_path = (By.XPATH, f'//li//p[contains(text(), "{order_number}")]')
        order_card = self.driver.find_element(*x_path)
        self.wait_element(x_path)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order_card)
        self.ac_click_element(x_path)

    @allure.step('check number order on open card')
    def check_number_order_on_open_card(self, order_number):
        num_on_card_x = (By.XPATH, f'//section[contains(@class, "opened")]//p[contains(., "{order_number}")]')
        self.wait_element(num_on_card_x)
        assert order_number in self.driver.find_element(*num_on_card_x).text

    @allure.step('get all numbers list')
    def get_all_numbers_list(self):
        self.wait_element_off(self.load_message)
        list_el = self.driver.find_elements(*OrderListPage.list_numbers_all_orders)
        list_num = [x.text for x in list_el]
        return list_num

    @allure.step('get value ready order')
    def get_value_ready_order(self):
        return self.get_value(self.ready_order)
