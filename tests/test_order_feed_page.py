from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.account_page import AccountPage
from helpers import random_bun_index, random_ingerdient_index
from locators.order_feed_page_locators import OrderFeedPageLocators
import pytest
import data


class TestAccountPage:
    @pytest.mark.parametrize("driver", ["Chrome", "Firefox"], indirect=True)
    def test_order_feed_modal_details(self, driver):
        order_feed = OrderFeedPage(driver)   
        order_feed.go_to_url(data.ORDER_FEED_URL)     
        order_feed.click_latest_order()
        assert order_feed.check_order_composition_preset()

    @pytest.mark.parametrize("driver", ["Chrome", "Firefox"], indirect=True)
    def test_order_feed_order_from_history_present(self, login_user):
        main_page = MainPage(login_user)
        main_page.click_my_account()
        history = AccountPage(login_user)
        order_id = history.get_last_order_id()
        main_page.click_order_feed_button() 
        order_feed = OrderFeedPage(login_user)
        assert order_feed.check_displayed_order_feed(order_id)

    @pytest.mark.parametrize(
            'counter_locator',
            [OrderFeedPageLocators.ORDER_FEED_TOTAL_COUNTER, OrderFeedPageLocators.ORDER_FEED_DAILY_COUNTER]
    )
    @pytest.mark.parametrize(
            'bun_index, ingredients',
            [
                [random_bun_index(), [random_ingerdient_index()]]
            ]
    )
    @pytest.mark.parametrize("driver", ["Chrome", "Firefox"], indirect=True)
    def test_order_feed_total_counter(self, login_user, bun_index, ingredients, counter_locator):
        main_pages = MainPage(login_user)
        order_feed = OrderFeedPage(login_user)
        order_feed.go_to_url(data.ORDER_FEED_URL)
        count_before = order_feed.get_text_from_element(counter_locator)   
        main_pages.click_constructor_button()
        main_pages.create_new_order(bun_index, ingredients)
        order_feed.go_to_url(data.ORDER_FEED_URL)
        count_after = order_feed.get_text_from_element(counter_locator)   
        assert count_after > count_before

    @pytest.mark.parametrize(
            'bun_index, ingredients',
            [
                [random_bun_index(), [random_ingerdient_index()]]
            ]
    )
    @pytest.mark.parametrize("driver", ["Chrome", "Firefox"], indirect=True)
    def test_order_feed_new_order_in_progress(self, login_user, bun_index, ingredients):
        main_pages = MainPage(login_user)
        order_feed = OrderFeedPage(login_user)
        order_id = main_pages.create_new_order(bun_index, ingredients)
        order_feed.go_to_url(data.ORDER_FEED_URL)
        assert order_feed.check_displayed_order_in_progress(order_id)
        