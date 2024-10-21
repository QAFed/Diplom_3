import time

from pages.header_page import HeaderElements
from pages.order_list_page import OrderListPage
from pages.home_page import HomePage
from pages.ingredient_detail import IngrdientDetailsPage
from pages.order_accepted_page import OrderAcceptedPage

class TestMainFunctions:
    def test_open_page_constructor_from_button_in_header(self, driver_factory):
        action_page = OrderListPage(driver_factory)
        action_page.open_page()
        action_page.ac_click_element(HeaderElements.button_constructor)
        action_page.wait_element(HomePage.header_text)
        assert driver_factory.current_url == HomePage.URL

    def test_open_page_order_list_from_button_in_header(self, driver_factory):
        action_page = HomePage(driver_factory)
        action_page.open_page()
        action_page.ac_click_element(HeaderElements.button_order_list)
        action_page.wait_element(OrderListPage.header_text)
        assert driver_factory.current_url == OrderListPage.URL

    def test_open_page_inredient_details_if_click_icon_on_home_page(self, driver_factory):
        action_page = HomePage(driver_factory)
        action_page.open_page()
        action_page.ac_click_element(HomePage.icon_krator_bulka)
        action_page.wait_element(IngrdientDetailsPage.header_text)
        assert IngrdientDetailsPage.URLpart in driver_factory.current_url

    def test_close_ingredient_details_page_if_click_close_button_x(self, driver_factory):
        action_page = HomePage(driver_factory)
        action_page.open_page()
        action_page.ac_click_element(HomePage.icon_krator_bulka)
        action_page.ac_click_element(IngrdientDetailsPage.button_close_x)
        assert driver_factory.find_elements(*IngrdientDetailsPage.flag_window_is_active) == []

    def test_counter_ingredient_up_if_add_it_in_burger(self, driver_factory):
        home_page = HomePage(driver_factory)
        home_page.open_page()
        home_page.add_ingredient_in_burger(HomePage.icon_krator_bulka)
        home_page.check_counter_ingredient(HomePage.icon_krator_bulka, "2")

    def test_create_order_if_user_log_in(self, login_user):
        home_page = HomePage(login_user)
        home_page.open_page()
        home_page.add_ingredient_in_burger(HomePage.icon_krator_bulka)
        home_page.ac_click_element(HomePage.button_order)
        home_page.wait_element(OrderAcceptedPage.order_number)
        assert login_user.find_elements(*OrderAcceptedPage.flag_window_is_active) != []


