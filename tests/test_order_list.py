import time

from pages.order_list_page import OrderListPage
from pages.header_page import HeaderElements

class TestOrderList:
    def test_open_details_order_card_if_click_order_card(self, driver_with_order):
        driver, order_number = driver_with_order
        order_list_page = OrderListPage(driver)
        order_list_page.open_page()
        time.sleep(10)
        order_list_page.click_to_card_by_number(order_number)
        time.sleep(10)
        order_list_page.check_number_order_on_open_card(order_number)