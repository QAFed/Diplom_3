import pytest
from pages.order_list_page import OrderListPage
from pages.header_page import HeaderElements
from pages.personal_page import PersonalPage
from pages.home_page import HomePage
import allure

@allure.suite('Test Order List')
class TestOrderList:
    @allure.title('test open details order card if click order card')
    def test_open_details_order_card_if_click_order_card(self, driver_with_order):
        driver, order_number = driver_with_order
        order_list_page = OrderListPage(driver)
        order_list_page.open_page()
        # order_list_page.wait_element_off(OrderListPage.load_message)
        order_list_page.wait_load_message_off()
        order_list_page.click_to_card_by_number(order_number)
        order_list_page.check_number_order_on_open_card(order_number)

    @allure.title('test number from history exist in list order')
    def test_number_from_history_exist_in_list_order(self, driver_with_two_orders):
        driver = driver_with_two_orders
        order_list_page = OrderListPage(driver)
        # action_page.ac_click_element(HeaderElements.button_personal_account)
        order_list_page.click_button_person_accaunt()
        # action_page.wait_element(PersonalPage.button_order_history)
        pers_page = PersonalPage(driver)
        pers_page.wait_button_order_history()
        # action_page.ac_click_element(PersonalPage.button_order_history)
        pers_page.click_button_order_history()
        all_number_from_history = order_list_page.get_all_numbers_list()
        # action_page.ac_click_element(HeaderElements.button_order_list)
        pers_page.click_button_order_list()
        # action_page.wait_element(OrderListPage.all_time_counter)
        order_list_page.wait_all_time_counter()
        all_number_from_order_list = order_list_page.get_all_numbers_list()
        assert all(num in all_number_from_order_list for num in all_number_from_history)

    @allure.title('test counter all time increment if add order')
    @pytest.mark.parametrize('counter', [
        OrderListPage.all_time_counter,
        OrderListPage.today_counter
    ])
    def test_counter_all_time_increment_if_add_order(self, login_user, counter):
        driver = login_user
        order_list_page = OrderListPage(driver)
        order_list_page.open_page()
        count_before = order_list_page.get_value(counter)
        home_page = HomePage(driver)
        home_page.open_page()
        home_page.create_new_order()
        order_list_page.open_page()
        count_after = order_list_page.get_value(counter)
        assert count_after > count_before

    @allure.title('test created order add in ready list')
    def test_created_order_add_in_ready_list(self, driver_with_order):
        driver, order_number = driver_with_order
        home_page = HomePage(driver)
        # action_page.ac_click_element(HeaderElements.button_order_list)
        home_page.click_button_order_list()
        order_list = OrderListPage(driver)
        # order_list.wait_digits_after_change(OrderListPage.ready_order)
        order_list.wait_digits_after_change_ready_order()
        # num_on_ready = action_page.get_value(OrderListPage.ready_order)
        num_on_ready = order_list.get_value_ready_order()
        assert order_number in num_on_ready
