from selenium import webdriver
import pytest


@pytest.fixture(params=["Chrome", "Firefox"])
def driver_factory(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome()
    elif request.param == "Firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
        print("Check driver_factory params, default now Chrome")
    yield driver
    driver.quit()
