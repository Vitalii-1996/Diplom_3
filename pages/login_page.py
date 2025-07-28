from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    @allure.step('click reset password link')
    def click_reset_password(self):
        self.scroll_to_element(LoginPageLocators.RESET_PASSWORD_LINK)
        self.click_on_element(LoginPageLocators.RESET_PASSWORD_LINK)

    @allure.step('input email')
    def set_email(self, email):
        self.add_text_to_element(LoginPageLocators.EMAIL_INPUT_FIELD, email)

    @allure.step('input password')
    def set_password(self, password):
        self.add_text_to_element(LoginPageLocators.PASSWORD_INPUT_FIELD, password)

    @allure.step('click login button')
    def click_login(self):
        self.click_on_element(LoginPageLocators.LOGIN_BUTTON)
