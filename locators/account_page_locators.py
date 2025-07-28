from selenium.webdriver.common.by import By


class AccountPageLocators:
    PROFILE_BUTTON = [By.XPATH, ".//nav/ul/li/a[contains(text(),'Профиль')]"]
    ORDER_HISTORY_BUTTON = [By.XPATH, ".//nav/ul/li/a[text()='История заказов']"]
    LOGOUT_BUTTON = [By.XPATH, ".//nav/ul/li/button[text()='Выход']"]
    ORDER_HISTORY_LAST_ORDER = [By.XPATH, ".//main//ul/li[last()]/a/div/p[contains(@class, 'text_type_digits')]"]
