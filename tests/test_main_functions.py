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
        order_list_page.click_button_constructor()
        home_page = HomePage(driver_factory)
        home_page.wait_header_text()
        home_page.check_self_current_url()

    @allure.title('test open page order list from button in header')
    def test_open_page_order_list_from_button_in_header(self, driver_factory):
        home_page = HomePage(driver_factory)
        home_page.open_page()
        home_page.click_button_order_list()
        order_list = OrderListPage(driver_factory)
        order_list.wait_header_text()
        order_list.check_self_current_url()

    @allure.title('test open page inredient details if click icon on home page')
    def test_open_page_inredient_details_if_click_icon_on_home_page(self, driver_factory):
        home_page = HomePage(driver_factory)
        home_page.open_page()
        home_page.click_button_crater_bulka()
        ingred_detail = IngrdientDetailsPage(driver_factory)
        ingred_detail.wait_header_text()
        ingred_detail.check_url_part_in_current_url()

    @allure.title('test close ingredient details page if click close button x')
    def test_close_ingredient_details_page_if_click_close_button_x(self, driver_factory):
        home_page = HomePage(driver_factory)
        home_page.open_page()
        home_page.click_button_crater_bulka()
        ingred_detail = IngrdientDetailsPage(driver_factory)
        ingred_detail.wait_header_text()
        ingred_detail.click_button_close_x()
        home_page.check_no_active_window_ingred_details()

    @allure.title('test counter ingredient up if add it in burger')
    def test_counter_ingredient_up_if_add_it_in_burger(self, driver_factory):
        home_page = HomePage(driver_factory)
        home_page.open_page()
        home_page.add_krat_bulka_in_burger()
        home_page.check_counter_krat_bulka()

    @allure.title('test create order if user log in')
    def test_create_order_if_user_log_in(self, login_user):
        home_page = HomePage(login_user)
        home_page.open_page()
        home_page.add_krat_bulka_in_burger()
        home_page.click_button_order()
        order_accept = OrderAcceptedPage(login_user)
        order_accept.wait_order_number()
        home_page.check_active_window_accept_order()
