from pages.home_page import HomePage
from pages.header_page import HeaderElements
from pages.personal_page import PersonalPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.order_history_page import OrderHistoryPage

class TestLogiUserEvents:
    def test_open_personal_page_from_link_klick_on_home_page(self, login_user):
        action_page = HomePage(login_user)
        action_page.click_element(HeaderElements.button_personal_account)
        action_page.wait_element(PersonalPage.button_order_history)
        assert login_user.current_url == PersonalPage.URL

    def test_open_history_page_from_button_on_personal_page(self, login_user):
        action_page = HomePage(login_user)
        action_page.ac_click_element(HeaderElements.button_personal_account)
        action_page.wait_element(PersonalPage.button_order_history)
        action_page.ac_click_element(PersonalPage.button_order_history)
        WebDriverWait(login_user, 5).until(
            expected_conditions.invisibility_of_element_located(OrderHistoryPage.load_message))
        assert login_user.current_url == OrderHistoryPage.URL


