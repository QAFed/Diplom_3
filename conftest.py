from selenium import webdriver
import pytest
from helpers import LoginPassName
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
# import pdb

# @pytest.fixture(params=["Chrome"])
# @pytest.fixture(params=["Chrome", "Firefox"])
@pytest.fixture(params=["Firefox"])
def driver_factory(request):
    # pdb.set_trace()
    if request.param == "Chrome":
        driver = webdriver.Chrome()
    elif request.param == "Firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
        print("Check driver_factory params, default now Chrome")
    yield driver
    driver.quit()

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

@pytest.fixture
def login_user(driver_factory):
    user = new_user(driver_factory)
    login_page = LoginPage(driver_factory)
    login_page.open_page()
    login_page.fill_field(login_page.field_email, user.email)
    login_page.fill_field(login_page.field_pass, user.password)
    login_page.ac_click_element(login_page.button_login)
    login_page.wait_element(HomePage.button_order)
    yield driver_factory
    driver_factory.quit()

