from pages.home_page import HomePage
from pages.header_page import HeaderElements
from pages.personal_page import PersonalPage
from pages.order_history_page import OrderHistoryPage
from pages.login_page import LoginPage


class TestLogiUserEvents:
    def test_open_personal_page_from_link_klick_on_home_page(self, login_user):
        action_page = HomePage(login_user)
        action_page.ac_click_element(HeaderElements.button_personal_account)
        action_page.wait_element(PersonalPage.button_order_history)
        assert login_user.current_url == PersonalPage.URL

    def test_open_history_page_from_button_on_personal_page(self, login_user):
        action_page = HomePage(login_user)
        action_page.ac_click_element(HeaderElements.button_personal_account)
        action_page.wait_element(PersonalPage.button_order_history)
        action_page.ac_click_element(PersonalPage.button_order_history)
        action_page.wait_element_off(OrderHistoryPage.load_message)
        assert login_user.current_url == OrderHistoryPage.URL

    def test_open_login_page_from_logout_button_on_personal_page(self, login_user):
        action_page = HomePage(login_user)
        action_page.ac_click_element(HeaderElements.button_personal_account)
        action_page.wait_element(PersonalPage.button_order_history)
        action_page.ac_click_element(PersonalPage.button_logout)
        action_page.wait_element(LoginPage.button_login)
        assert login_user.current_url == LoginPage.URL
