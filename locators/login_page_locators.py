from selenium.webdriver.common.by import By


class LoginPageLocators:
    RESET_PASSWORD_LINK = [By.XPATH, ".//div/p/a[contains(text(), 'Восстановить пароль')]"]
    EMAIL_INPUT_FIELD = [By.XPATH, ".//fieldset/div/div/input[@name='name']"]
    PASSWORD_INPUT_FIELD = [By.XPATH, ".//fieldset/div/div/input[@name='Пароль']"]
    LOGIN_BUTTON = [By.XPATH, ".//form/button[text()='Войти']"]
    