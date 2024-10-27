from selenium import webdriver
import pytest
from helpers import LoginPassName
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(params=["Chrome", "Firefox"])
# @pytest.fixture(params=["Firefox"])
def driver_factory(request):
    if request.param == "Chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif request.param == "Firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
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


@pytest.fixture
def driver_with_order(login_user):
    home_page = HomePage(login_user)
    home_page.open_page()
    order_number = home_page.create_new_order()
    return login_user, order_number


@pytest.fixture
def driver_with_two_orders(login_user):
    home_page = HomePage(login_user)
    home_page.open_page()
    home_page.create_new_order()
    home_page.open_page()
    home_page.create_new_order()
    return login_user
