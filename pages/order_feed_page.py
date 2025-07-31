from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage
import allure


class OrderFeedPage(BasePage):
    @allure.step('check order feed heading is displayed')
    def check_order_feed_heading(self):
        return self.check_displaying_of_element(OrderFeedPageLocators.ORDER_FEED_HEADING)
    
    @allure.step('click on the last order')
    def click_latest_order(self):
        self.click_on_element(OrderFeedPageLocators.ORDER_FEED_LATEST_ORDER)

    @allure.step('check modal is diplayed')
    def check_order_composition_preset(self):
        return self.check_displaying_of_element(OrderFeedPageLocators.ORDER_MODAL_COMPOSITION)

    def check_displayed_order(self, order_id, locator):
        by, format_locator = locator
        format_locator = format_locator.format(order_id=order_id)
        print(format_locator)
        return self.check_displaying_of_element([by, format_locator])
    
    @allure.step('check order is displayed in order feed list')
    def check_displayed_order_feed(self, order_id):
        return self.check_displayed_order(order_id, OrderFeedPageLocators.ORDER_FEED_ORDER_BY_ID)
    
    @allure.step('check order displayed in inprogress list')
    def check_displayed_order_in_progress(self, order_id):
        return self.check_displayed_order(order_id, OrderFeedPageLocators.ORDER_FEED_IN_PROGRESS_LIST)
    