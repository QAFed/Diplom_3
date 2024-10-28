import time

from pages.header_page import HeaderElements
from pages.order_list_page import OrderListPage
from pages.home_page import HomePage
from pages.ingredient_detail import IngrdientDetailsPage
from pages.order_accepted_page import OrderAcceptedPage
import allure

@allure.suite('Test Main Functions')
class TestMainFunctions:
    @allure.title('test open page constructor from button in header')
    def test_open_page_constructor_from_button_in_header(self, driver_factory):
        order_list_page = OrderListPage(driver_factory)
        order_list_page.open_page()
        # action_page.ac_click_element(HeaderElements.button_constructor)
        order_list_page.click_button_constructor()
        # action_page.wait_element(HomePage.header_text)
        home_page = HomePage(driver_factory)
        home_page.wait_header_text()
        # assert driver_factory.current_url == HomePage.URL
        home_page.check_self_current_url()

    @allure.title('test open page order list from button in header')
    def test_open_page_order_list_from_button_in_header(self, driver_factory):
        home_page = HomePage(driver_factory)
        home_page.open_page()
        # action_page.ac_click_element(HeaderElements.button_order_list)
        home_page.click_button_order_list()
        # action_page.wait_element(OrderListPage.header_text)
        order_list = OrderListPage(driver_factory)
        order_list.wait_header_text()
        # assert driver_factory.current_url == OrderListPage.URL
        order_list.check_self_current_url()

    @allure.title('test open page inredient details if click icon on home page')
    def test_open_page_inredient_details_if_click_icon_on_home_page(self, driver_factory):
        home_page = HomePage(driver_factory)
        home_page.open_page()
        # action_page.ac_click_element(HomePage.icon_krator_bulka)
        home_page.click_button_crater_bulka()
        # action_page.wait_element(IngrdientDetailsPage.header_text)
        ingred_detail = IngrdientDetailsPage(driver_factory)
        ingred_detail.wait_header_text()
        # assert IngrdientDetailsPage.URLpart in driver_factory.current_url
        ingred_detail.check_url_part_in_current_url()

    @allure.title('test close ingredient details page if click close button x')
    def test_close_ingredient_details_page_if_click_close_button_x(self, driver_factory):
        home_page = HomePage(driver_factory)
        home_page.open_page()
        # action_page.ac_click_element(HomePage.icon_krator_bulka)
        home_page.click_button_crater_bulka()
        # action_page.ac_click_element(IngrdientDetailsPage.button_close_x)
        ingred_detail = IngrdientDetailsPage(driver_factory)
        ingred_detail.wait_header_text()
        ingred_detail.click_button_close_x()
        # assert driver_factory.find_elements(*IngrdientDetailsPage.flag_window_is_active) == []
        home_page.check_no_active_window_ingred_details()

    @allure.title('test counter ingredient up if add it in burger')
    def test_counter_ingredient_up_if_add_it_in_burger(self, driver_factory):
        home_page = HomePage(driver_factory)
        home_page.open_page()
        # home_page.add_ingredient_in_burger(HomePage.icon_krator_bulka)
        home_page.add_krat_bulka_in_burger()
        # home_page.check_counter_ingredient(HomePage.icon_krator_bulka, "2")
        home_page.check_counter_krat_bulka()

    @allure.title('test create order if user log in')
    def test_create_order_if_user_log_in(self, login_user):
        home_page = HomePage(login_user)
        home_page.open_page()
        # home_page.add_ingredient_in_burger(HomePage.icon_krator_bulka)
        home_page.add_krat_bulka_in_burger()
        # home_page.ac_click_element(HomePage.button_order)
        home_page.click_button_order()
        # home_page.wait_element(OrderAcceptedPage.order_number)
        order_accept = OrderAcceptedPage(login_user)
        order_accept.wait_order_number()
        # assert login_user.find_elements(*OrderAcceptedPage.flag_window_is_active) != []
        home_page.check_active_window_accept_order()
