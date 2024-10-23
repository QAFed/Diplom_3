import time

from pages.order_list_page import OrderListPage
from pages.header_page import HeaderElements
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestOrderList:
    def test_open_details_order_card_if_click_order_card(self, driver_with_order):
        driver, order_number = driver_with_order
        order_list_page = OrderListPage(driver)
        order_list_page.open_page()
        WebDriverWait(driver, 5).until(
            expected_conditions.invisibility_of_element_located(OrderListPage.load_message))
        order_list_page.click_to_card_by_number(order_number)
        order_list_page.check_number_order_on_open_card(order_number)

