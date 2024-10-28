from datetime import datetime
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from conftest import driver_factory

class LoginPassName:
    def __init__(self):
        self.gen_id = datetime.now().strftime("%Y%m%d%H%M%S")
        self.name = f"name{self.gen_id}"
        self.email = f"FedorIdolenkov_{self.gen_id}@ya.ya"
        self.password = f"psswrd{self.gen_id}"


class Helpers:
    @staticmethod
    def new_user(driver_factory):
        user = LoginPassName()
        reg_page = RegisterPage(driver_factory)
        reg_page.open_page()
        reg_page.wait_element(reg_page.button_registrer)
        reg_page.fill_field(reg_page.field_name, user.name)
        reg_page.fill_field(reg_page.field_email, user.email)
        reg_page.fill_field(reg_page.field_pass, user.password)
        reg_page.click_element(reg_page.button_registrer)
        reg_page.wait_element(LoginPage.button_login)
        return user