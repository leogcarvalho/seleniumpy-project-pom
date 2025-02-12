import pytest
from selenium import webdriver
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chromedriver_binary.add_chromedriver_to_path()
driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    # setup
    global driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # run test
    yield

    # teardown
    driver.quit()
