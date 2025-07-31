from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    EMAIL_INPUT_FIELD = [By.XPATH, ".//fieldset/div/div/input[@name='name']"]
    RESET_PASSWORD_BUTTON = [By.XPATH, ".//form[contains(@class, 'Auth_form')]/button[text()='Восстановить']"]
    RESET_PASSWORD_LABEL = [By.XPATH, ".//fieldset/div/div/label[text()='Введите код из письма']"]
    SHOW_PASSWORD_BUTTON = [By.XPATH, ".//fieldset//div[contains(@class, 'input__icon')]"]
    PASSWORD_INPUT_CONTAINER_ACTIVE = [By.XPATH, ".//fieldset//label[text()='Пароль']/parent::div[contains(@class, 'input_status_active')]"]
