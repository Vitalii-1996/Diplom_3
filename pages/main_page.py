from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import data
import allure


class MainPage(BasePage):
    @allure.step('click my account button')
    def click_my_account(self):
        self.wait_overlay_disappear()
        self.click_on_element(MainPageLocators.MY_ACCOUNT_BUTTON)        

    @allure.step('wait for overlay disappear')
    def wait_overlay_disappear(self):
        self.wait_element_disappear(MainPageLocators.OVERLAY)

    @allure.step('click constructor button')
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTION_BUTTON)

    @allure.step('click order feed button')
    def click_order_feed_button(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('check assemble burger header is displayed')
    def check_assemble_burger_heading(self):
        return self.check_displaying_of_element(MainPageLocators.ASSEMBLE_BURGER_HEADING)
    
    @allure.step('click on ingredint with specific index')
    def click_ingredient(self, index):
        ingredient = self.find_elements_with_wait(MainPageLocators.INGREDIENTS)[index]
        self.perform_scroll(ingredient)
        self.perform_click(ingredient)

    @allure.step('get counter of ingerdient with specific index')
    def get_ingredient_count(self, index):
        ingredient = self.find_elements_with_wait(MainPageLocators.INGREDIENT_COUNTER)[index]
        return ingredient.text
    
    @allure.step('drag ingredient to the busket')
    def drag_ingredient(self, index):
        ingredient = self.find_elements_with_wait(MainPageLocators.INGREDIENTS)[index]
        basket = self.find_element_with_wait(MainPageLocators.BURGER_CONSTRACTION_BUSKET)
        self.drag_and_drop_element(ingredient, basket)

    @allure.step('check popup heading is displayed')
    def check_popup_modal_header(self):
        return self.check_displaying_of_element(MainPageLocators.POPUP_HEADER)
    
    @allure.step('click on close modal button')
    def click_close_modal_button(self):
        self.click_on_element(MainPageLocators.POPUP_CLOSE_BUTTON)

    @allure.step('check the modal not displayed anymore')
    def check_modal_close(self):
        return self.wait_element_disappear(MainPageLocators.POPUP_HEADER)
    
    @allure.step('click place order button')
    def click_place_order(self):
        self.click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)
    
    @allure.step('get order id')
    def get_order_id(self):
        locator = MainPageLocators.POPUP_HEADER
        self.wait_element_to_be_changed(locator, data.ORDER_ID_PLACEHOLDER)
        self.wait_element_disappear(MainPageLocators.POPUP_HEADER_PLACEHOLDER)
        return self.get_text_from_element(locator)
    
    @allure.step('create new order')
    def create_new_order(self, bun, ingredients):
        self.drag_ingredient(bun)
        for ingredient in ingredients:
            self.drag_ingredient(ingredient)
        self.click_place_order()
        self.wait_overlay_disappear()
        return self.get_order_id()
        