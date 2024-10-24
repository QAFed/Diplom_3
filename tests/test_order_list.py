import time

import pytest

from pages.order_list_page import OrderListPage
from pages.header_page import HeaderElements
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.personal_page import PersonalPage
from pages.home_page import HomePage


class TestOrderList:
    def test_open_details_order_card_if_click_order_card(self, driver_with_order):
        driver, order_number = driver_with_order
        order_list_page = OrderListPage(driver)
        order_list_page.open_page()
        WebDriverWait(driver, 5).until(
            expected_conditions.invisibility_of_element_located(OrderListPage.load_message))
        order_list_page.click_to_card_by_number(order_number)
        order_list_page.check_number_order_on_open_card(order_number)

    def test_number_from_history_exist_in_list_order(self, driver_with_two_orders):
        driver = driver_with_two_orders
        action_page = OrderListPage(driver)
        action_page.ac_click_element(HeaderElements.button_personal_account)
        action_page.wait_element(PersonalPage.button_order_history)
        action_page.ac_click_element(PersonalPage.button_order_history)
        all_number_from_history = action_page.get_all_numbers_list()
        # print("НОМЕРА", all_number_from_history)
        action_page.ac_click_element(HeaderElements.button_order_list)
        # action_page.wait_close(OrderListPage.load_message)
        action_page.wait_element(OrderListPage.all_time_counter)
        all_number_from_order_list = action_page.get_all_numbers_list()
        # print('номера', all_number_from_order_list)
        assert all(num in all_number_from_order_list for num in all_number_from_history)

    @pytest.mark.parametrize('counter',[
        OrderListPage.all_time_counter,
        OrderListPage.today_counter
    ])
    def test_counter_all_time_increment_if_add_order(self, driver_with_order, counter):
        driver, order_number = driver_with_order
        order_list_page = OrderListPage(driver)
        order_list_page.open_page()
        count_before=order_list_page.get_value(counter)
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.create_new_order()
        order_list_page.open_page()
        count_after = order_list_page.get_value(counter)
        assert count_after > count_before
