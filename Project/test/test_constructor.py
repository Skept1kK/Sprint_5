import pytest
from locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from data import TestData

@pytest.mark.usefixtures("get_driver")


class TestConstructor:
    # Проверка вкладки "Булки"
    def test_roll_tab(self, get_driver):
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_PROFILE_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.AUTH_PAGE_LOGIN_FIELD).send_keys(TestData.LOGIN_NAME)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.PROFILE_PAGE_CONSTRUCTOR_LINK))
        driver.find_element(*locators.PROFILE_PAGE_CONSTRUCTOR_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_SOUCES_TAB))
        driver.find_element(*locators.MAIN_PAGE_SOUCES_TAB).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_ROLLS_TAB))
        driver.find_element(*locators.MAIN_PAGE_ROLLS_TAB).click()
        assert driver.find_element(*locators.MAIN_PAGE_ROLLS_CLASS).is_displayed()

    # Проверка вкладки "Соусы"
    def test_souse_tab(self, get_driver):
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_PROFILE_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.AUTH_PAGE_LOGIN_FIELD).send_keys(TestData.LOGIN_NAME)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.PROFILE_PAGE_CONSTRUCTOR_LINK))
        driver.find_element(*locators.PROFILE_PAGE_CONSTRUCTOR_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_FILLINGS_TAB))
        driver.find_element(*locators.MAIN_PAGE_FILLINGS_TAB).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_SOUCES_TAB))
        driver.find_element(*locators.MAIN_PAGE_SOUCES_TAB).click()
        assert driver.find_element(*locators.MAIN_PAGE_SOUCES_CLASS).is_displayed()

    # Проверка вкладки "Начинка"
    def test_fillings_tab(self, get_driver):
        driver = get_driver
        driver.find_element(*locators.MAIN_PAGE_PROFILE_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.REG_BUTTON))
        driver.find_element(*locators.AUTH_PAGE_LOGIN_FIELD).send_keys(TestData.LOGIN_NAME)
        driver.find_element(*locators.USER_PASSWORD_INPUT).send_keys(TestData.USER_PASSWORD)
        driver.find_element(*locators.AUTH_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.PROFILE_PAGE_CONSTRUCTOR_LINK))
        driver.find_element(*locators.PROFILE_PAGE_CONSTRUCTOR_LINK).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_SOUCES_TAB))
        driver.find_element(*locators.MAIN_PAGE_SOUCES_TAB).click()
        WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located(locators.MAIN_PAGE_FILLINGS_TAB))
        driver.find_element(*locators.MAIN_PAGE_FILLINGS_TAB).click()
        assert driver.find_element(*locators.MAIN_PAGE_FILLINGS_CLASS).is_displayed()