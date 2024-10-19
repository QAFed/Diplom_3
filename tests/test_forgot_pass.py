import time

from pages.forgot_pass_page import ForgotPage
from pages.login_page import LoginPage
from pages.reset_pass_page import ResetPage


class TestForgotPass:
    def test_open_forgot_pass_page_if_click_button_recover(self, driver_factory):
        login_page = LoginPage(driver_factory)
        login_page.open_page()
        login_page.click_element(login_page.link_recover_pass)
        login_page.wait_element(ForgotPage.button_recovery)
        assert driver_factory.current_url == ForgotPage.URL

    def test_open_reset_pass_page_if_fill_email_and_click_button(self, driver_factory):
        forgot_pass = ForgotPage(driver_factory)
        forgot_pass.open_page()
        forgot_pass.fill_field(forgot_pass.field_email, 'fedtest@disp.ru')
        forgot_pass.click_element(forgot_pass.button_recovery)
        forgot_pass.wait_element(ResetPage.button_save)
        assert driver_factory.current_url == ResetPage.URL

    def test_field_pass_activate_if_cklick_button_pass_visible(self, driver_factory):
        reset_pass = ResetPage(driver_factory)
        reset_pass.open_page()
        reset_pass.ac_click_element(ResetPage.button_pass_visible)
        reset_pass.assert_field_pass_active()