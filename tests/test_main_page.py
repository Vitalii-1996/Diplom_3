from pages.main_page import MainPage
from helpers import random_bun_index, random_ingerdient_index
import pytest
import data
import random


class TestMainPage:
    @pytest.mark.parametrize(
            'ingredient_index',
            [random.randint(0,data.INGREDIENT_COUNT)]
    )
    @pytest.mark.parametrize("driver", ["Chrome", "Firefox"], indirect=True)
    def test_ingredient_popup(self, driver, ingredient_index):
        main_pages = MainPage(driver)   
        main_pages.go_to_url(data.MAIN_PAGE_URL)     
        main_pages.click_ingredient(ingredient_index)
        assert main_pages.check_popup_modal_header()

    @pytest.mark.parametrize(
            'ingredient_index',
            [random.randint(0,data.INGREDIENT_COUNT)]
    )
    @pytest.mark.parametrize("driver", ["Chrome", "Firefox"], indirect=True)
    def test_close_ingredient_popup(self, driver, ingredient_index):
        main_pages = MainPage(driver)   
        main_pages.go_to_url(data.MAIN_PAGE_URL)     
        main_pages.click_ingredient(ingredient_index)
        main_pages.click_close_modal_button()
        assert main_pages.check_modal_close()

    @pytest.mark.parametrize(
            'ingredient_index',
            [random_ingerdient_index()]
    )
    @pytest.mark.parametrize("driver", ["Chrome", "Firefox"], indirect=True)
    def test_add_ingredient_increase_counter(self, driver, ingredient_index):
        main_pages = MainPage(driver)   
        main_pages.go_to_url(data.MAIN_PAGE_URL)
        count_before = main_pages.get_ingredient_count(ingredient_index) 
        main_pages.drag_ingredient(ingredient_index)
        count_after = main_pages.get_ingredient_count(ingredient_index) 
        assert count_after > count_before

    @pytest.mark.parametrize(
            'bun_index, ingredients',
            [
                [random_bun_index(), [random_ingerdient_index()]]
            ]
    )
    @pytest.mark.parametrize("driver", ["Chrome", "Firefox"], indirect=True)
    def test_place_order(self, login_user, bun_index, ingredients):
        main_pages = MainPage(login_user)   
        order = main_pages.create_new_order(bun_index, ingredients)
        assert order != data.ORDER_ID_PLACEHOLDER
        