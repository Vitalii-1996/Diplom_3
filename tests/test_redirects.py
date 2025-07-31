from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.order_feed_page import OrderFeedPage
from pages.reset_password_page import ResetPasswordPage
import pytest
import data
import allure


class TestRedirects:
    @allure.title('Test redirect from main page to account page')
    def test_redirect_to_my_account(self, login_user):
        main_pages = MainPage(login_user)        
        main_pages.click_my_account()
        main_pages.wait_for_page_change(data.MY_ACCOUNT_URL)
        account_page = AccountPage(login_user)
        assert account_page.check_profile_button_displayed()

    @allure.title('Test redirect from login page to main page')
    def test_constructor_button_redirect(self, driver):
        main_pages = MainPage(driver)   
        main_pages.go_to_url(data.LOGIN_PAGE_URL)     
        main_pages.click_constructor_button()
        main_pages.wait_for_page_change(data.MAIN_PAGE_URL)
        assert main_pages.check_assemble_burger_heading()

    @allure.title('Test redirect from main page to order feed page')
    def test_constructor_order_feed_redirect(self, driver):
        main_pages = MainPage(driver)   
        main_pages.go_to_url(data.MAIN_PAGE_URL)     
        main_pages.click_order_feed_button()
        main_pages.wait_for_page_change(data.ORDER_FEED_URL)
        order_feed = OrderFeedPage(driver)
        assert order_feed.check_order_feed_heading()

    @allure.title('Test redirect from login page to reset password page')
    def test_reset_password_redirect(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_url(data.LOGIN_PAGE_URL)
        login_page.click_reset_password()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_page_change(data.RESET_PASSWORD_URL)

        assert reset_password_page.check_reset_password_button_present()
