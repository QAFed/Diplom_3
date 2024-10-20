from pages.header_page import HeaderElements
from pages.order_list_page import OrderListPage
from pages.home_page import HomePage
from pages.ingredient_detail import IngrdientDetailsPage

class TestMainFunctions:
    def test_open_page_constructor_from_button_in_header(self, driver_factory):
        current_page = OrderListPage(driver_factory)
        current_page.open_page()
        current_page.ac_click_element(HeaderElements.button_constructor)
        current_page.wait_element(HomePage.header_text)
        assert driver_factory.current_url == HomePage.URL

    def test_open_page_order_list_from_button_in_header(self, driver_factory):
        current_page = HomePage(driver_factory)
        current_page.open_page()
        current_page.ac_click_element(HeaderElements.button_order_list)
        current_page.wait_element(OrderListPage.header_text)
        assert driver_factory.current_url == OrderListPage.URL

    def test_open_page_inredient_details_if_click_icon_on_home_page(self, driver_factory):
        current_page = HomePage(driver_factory)
        current_page.open_page()
        current_page.ac_click_element(HomePage.icon_krator_bulka)
        current_page.wait_element(IngrdientDetailsPage.header_text)
        assert IngrdientDetailsPage.URLpart in driver_factory.current_url
