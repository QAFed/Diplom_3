from pages.home_page import HomePage
from pages.header_page import HeaderElements
from pages.personal_page import PersonalPage


class TestLogiUserEvents:
    def test_open_personal_page_from_link_klick_on_home_page(self, login_user):
        home_page = HomePage(login_user)
        home_page.click_element(HeaderElements.button_personal_account)
        home_page.wait_element(PersonalPage.button_order_history)
        assert login_user.current_url == PersonalPage.URL



