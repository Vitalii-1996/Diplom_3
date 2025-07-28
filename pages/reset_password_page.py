from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage
# import allure


class ResetPasswordPage(BasePage):
    def set_email(self, email):
        self.add_text_to_element(ResetPasswordPageLocators.EMAIL_INPUT_FIELD, email)

    def check_reset_password_label_present(self):
        return self.check_displaying_of_element(ResetPasswordPageLocators.RESET_PASSWORD_LABEL)
    
    def check_reset_password_button_present(self):
        return self.check_displaying_of_element(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)
    
    def click_show_password(self):
        self.click_on_element(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)
        
    def click_reset_password_button(self):
        self.click_on_element(ResetPasswordPageLocators.RESET_PASSWORD_BUTTON)

    def check_password_field_active(self):
        return self.check_displaying_of_element(ResetPasswordPageLocators.PASSWORD_INPUT_CONTAINER_ACTIVE)
    