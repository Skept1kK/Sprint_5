import pytest
import time
from selenium import webdriver
from urls import TestUrls

@pytest.fixture
def get_driver():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(TestUrls.MAIN_PAGE_URL)
        yield driver
        time.sleep(5)
        driver.quit()


