import pytest
from selenium import webdriver
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager

chromedriver_binary.add_chromedriver_to_path()
driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    # setup
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # run test
    yield

    # teardown
    driver.quit()
