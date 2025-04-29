# tests/test_search_button.py
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
import pytest


@pytest.fixture(scope="module")
def driver():
    # Setup ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_open_blazedemo(driver):
    driver.get("https://www.blazedemo.com")
    time.sleep(4)
