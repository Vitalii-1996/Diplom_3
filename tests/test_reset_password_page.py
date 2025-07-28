from pages.reset_password_page import ResetPasswordPage
from helpers import generate_random_email
import pytest
import data
import allure


class TestResetPasswordPage:
    @allure.title('Test input email and click reset password')
    @pytest.mark.parametrize("driver", ["Chrome", "Firefox"], indirect=True)
    def test_reset_password_success_flow(self, driver):
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.go_to_url(data.RESET_PASSWORD_URL)
        random_email = generate_random_email()
        reset_password_page.set_email(random_email)
        reset_password_page.click_reset_password_button()

        assert reset_password_page.check_reset_password_label_present()

    @allure.step('Test show password button activate input field')
    @pytest.mark.parametrize("driver", ["Chrome", "Firefox"], indirect=True)
    def test_click_show_password(self, reset_password):
        login_page = ResetPasswordPage(reset_password)
        login_page.click_show_password()
        assert login_page.check_password_field_active()
          