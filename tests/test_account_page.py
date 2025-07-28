from pages.main_page import MainPage
from pages.account_page import AccountPage
import pytest
import data
import allure


class TestAccountPage:
    @allure.title('Go to accounts histor and check history section is active')
    @pytest.mark.parametrize("driver", ["Chrome", "Firefox"], indirect=True)
    def test_history(self, login_user):
        main_pages = MainPage(login_user) 
        main_pages.click_my_account()
        account_page = AccountPage(login_user)
        account_page.click_order_history()
        assert account_page.check_order_history_button_active()

    @allure.title('Test user success logout')
    @pytest.mark.parametrize("driver", ["Chrome", "Firefox"], indirect=True)
    def test_logout(self, login_user):
        main_pages = MainPage(login_user) 
        main_pages.click_my_account()
        account_page = AccountPage(login_user)
        account_page.click_logout()
        account_page.wait_for_page_change(data.LOGIN_PAGE_URL)
        assert account_page.check_profile_button_invisible()
        
        