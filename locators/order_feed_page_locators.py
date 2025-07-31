from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED_HEADING = By.XPATH, ".//main/div/h1[text()='Лента заказов']"
    ORDER_FEED_LATEST_ORDER = By.XPATH, ".//main/div/div/ul/li/a[1]"
    ORDER_MODAL_COMPOSITION = By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]/div/div/p[text()='Cостав']"
    ORDER_FEED_ORDER_BY_ID = By.XPATH, ".//p[contains(@class, 'text_type_digits') and contains(text(), '{order_id}')]"
    ORDER_FEED_TOTAL_COUNTER = By.XPATH, ".//div[contains(@class, 'undefined')]/p[contains(@class, 'OrderFeed_number')]"
    ORDER_FEED_DAILY_COUNTER = By.XPATH, ".//div[not(@class)]/p[contains(@class, 'OrderFeed_number')]"
    ORDER_FEED_IN_PROGRESS_LIST = By.XPATH, ".//div/ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(., '{order_id}')]"
    