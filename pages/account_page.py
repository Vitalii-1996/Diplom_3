from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    def check_profile_button_displayed(self):
        return self.check_displaying_of_element(AccountPageLocators.PROFILE_BUTTON)

    def click_order_history(self):
        self.click_on_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    def check_order_history_button_active(self):
        return "Account_link_active" in self.get_element_attribute(AccountPageLocators.ORDER_HISTORY_BUTTON, 'class')

    def click_logout(self):
        self.click_on_element(AccountPageLocators.LOGOUT_BUTTON)

    def check_profile_button_invisible(self):
        return self.check_element_not_present(AccountPageLocators.PROFILE_BUTTON)
    
    def get_last_order_id(self):
        self.click_order_history()
        self.scroll_to_element(AccountPageLocators.ORDER_HISTORY_LAST_ORDER)
        return self.get_text_from_element(AccountPageLocators.ORDER_HISTORY_LAST_ORDER)
    