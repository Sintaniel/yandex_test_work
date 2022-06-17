import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


class WebClient:
    def __init__(self, driver_path):
        self.driver_path = driver_path

    def chrome(self) -> WebDriver:
        options = Options()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(f'{self.driver_path}/chromedriver', options=options)


@pytest.fixture(scope='function')
def browser():
    browser = WebClient(driver_path="../drivers").chrome()
    yield browser
    browser.quit()
