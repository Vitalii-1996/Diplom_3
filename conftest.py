from selenium import webdriver
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage
from helpers import generate_random_email
from locators.main_page_locators import MainPageLocators
import pytest
import data

@pytest.fixture(params=["Chrome", "Firefox"])
def driver(request):
    mode = request.param
    if mode == 'Chrome':
        driver = webdriver.Chrome()
    if mode == 'Firefox':
        driver = webdriver.Firefox()

    yield driver
    
    driver.quit()

@pytest.fixture
def reset_password(driver):
    reset_password_page = ResetPasswordPage(driver)
    reset_password_page.go_to_url(data.RESET_PASSWORD_URL)
    random_email = generate_random_email()
    reset_password_page.set_email(random_email)
    reset_password_page.click_reset_password_button()
    return driver

@pytest.fixture
def login_user(driver):
    main_pages = MainPage(driver)
    main_pages.go_to_url(data.MAIN_PAGE_URL)
    main_pages.click_my_account()
    login_page = LoginPage(driver)
    login_page.set_email(data.TEST_EMAIL)
    login_page.set_password(data.TEST_PASSWORD)
    login_page.click_login()
    main_pages.check_displaying_of_element(MainPageLocators.ASSEMBLE_BURGER_HEADING)
    return driver
