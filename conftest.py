from selenium import webdriver
import pytest
from helpers import Helpers
from pages.login_page import LoginPage
from pages.home_page import HomePage
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["Chrome", "Firefox"])
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


@pytest.fixture
def login_user(driver_factory):
    user = Helpers.new_user(driver_factory)
    login_page = LoginPage(driver_factory)
    login_page.open_page()
    login_page.fill_field_email(user.email)
    login_page.fill_field_pass(user.password)
    login_page.click_button_login()
    home_page = HomePage(driver_factory)
    home_page.wait_button_order()
    yield driver_factory


@pytest.fixture
def driver_with_order(login_user):
    home_page = HomePage(login_user)
    home_page.open_page()
    order_number = home_page.create_new_order()
    return login_user, order_number


@pytest.fixture
def driver_with_two_orders(driver_with_order):
    login_user, order_number = driver_with_order
    home_page = HomePage(login_user)
    home_page.open_page()
    home_page.create_new_order()
    return login_user
