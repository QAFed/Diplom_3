import allure

from pages.forgot_pass_page import ForgotPage
from pages.login_page import LoginPage
from pages.reset_pass_page import ResetPage


@allure.suite('Test Forgot Pass')
class TestForgotPass:
    @allure.title('test open forgot pass page if click button recover')
    def test_open_forgot_pass_page_if_click_button_recover(self, driver_factory):
        login_page = LoginPage(driver_factory)
        login_page.open_page()
        login_page.click_link_recover()
        forgot_page = ForgotPage(driver_factory)
        forgot_page.wait_button_recovery()
        forgot_page.check_self_current_url()

    @allure.title('test open reset pass page if fill email and click button')
    def test_open_reset_pass_page_if_fill_email_and_click_button(self, driver_factory):
        forgot_pass = ForgotPage(driver_factory)
        forgot_pass.open_page()
        forgot_pass.fill_email_test_data()
        forgot_pass.click_button_recovery()
        reset_pass_page = ResetPage(driver_factory)
        reset_pass_page.wait_button_save()
        reset_pass_page.check_self_current_url()

    @allure.title('test field pass activate if cklick button pass visible')
    def test_field_pass_activate_if_cklick_button_pass_visible(self, driver_factory):
        reset_pass = ResetPage(driver_factory)
        reset_pass.open_page_by_click()
        reset_pass.click_button_pass_visible()
        reset_pass.assert_field_pass_active()
