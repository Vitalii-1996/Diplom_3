from selenium.webdriver.common.by import By


class MainPageLocators:
    MY_ACCOUNT_BUTTON = [By.XPATH, ".//header/nav/a[@href='/account']"]
    OVERLAY = [By.XPATH, "//*[contains(@class,  'Modal_modal__loading')]/following::div[@class='Modal_modal_overlay__x2ZCr']"]
    CONSTRUCTION_BUTTON = [By.XPATH, ".//nav//p[text()='Конструктор']/parent::a"]
    ASSEMBLE_BURGER_HEADING = [By.XPATH, ".//main/section/h1[text()='Соберите бургер']"]
    ORDER_FEED_BUTTON = [By.XPATH, ".//nav//p[text()='Лента Заказов']/parent::a"]
    INGREDIENTS = [By.XPATH, ".//div/ul/a[@draggable='true']"]
    INGREDIENT_COUNTER = [By.XPATH, ".//div/ul/a[@draggable='true']/div[contains(@class,'counter_counter')]/p"]
    POPUP_HEADER = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]/div/div/h2[contains(@class, 'Modal_modal__title')]"]
    POPUP_HEADER_PLACEHOLDER = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]/div/div/h2[contains(@class, 'Modal_modal__title') and contains(text(), '9999')]"]
    POPUP_CLOSE_BUTTON = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]/div/button[contains(@class, 'Modal_modal__close')]"]
    BURGER_CONSTRACTION_BUSKET = [By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]"]
    PLACE_ORDER_BUTTON = [By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]//button"]
    