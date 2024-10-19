from pages.forgot_pass_page import ForgotPage
from pages.login_page import LoginPage

class TestForgotPass:
    def test_open_forgot_pass_page_if_click_button_recover(self,driver_factory):
        login_page = LoginPage(driver_factory)
        login_page.open_page()
        login_page.click_element(login_page.link_recover_pass)
        login_page.wait_element(ForgotPage.button_recovery)
        assert driver_factory.current_url == ForgotPage.URL
