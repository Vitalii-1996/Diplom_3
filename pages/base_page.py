from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(
            EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def wait_element_to_be_changed(self, locator, default_value):
        return self.wait.until_not(
            EC.text_to_be_present_in_element(locator, default_value)
        )
    
    def check_element_is_clickable(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)
    
    def wait_element_disappear(self, locator):
        return self.wait.until_not(
            EC.visibility_of_element_located(locator)
        )

    def click_on_element(self, locator):
        target = self.check_element_is_clickable(locator)
        self.perform_click(target)

    def perform_click(self, target):
        click = ActionChains(self.driver)
        click.move_to_element(target).click().perform()

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def format_locator(self, base_locator, num):
        method, locator = base_locator 
        locator = locator.format(num)

        return (method, locator)

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.perform_scroll(element)

    def perform_scroll(self, element):
        self.driver.execute_script("""
            arguments[0].scrollIntoView({block: "center", inline: "nearest"});
        """, element)

    def wait_for_page_change(self, url):
        self.wait.until(EC.url_matches(url))

    def find_elements_with_wait(self, locator):
        self.wait.until(
            EC.visibility_of_all_elements_located(locator))
        return self.driver.find_elements(*locator) 
    
    def get_element_attribute(self, locator, attribute):
        return self.find_element_with_wait(locator).get_attribute(attribute)

    def check_displaying_of_element(self, locator):
        target = self.find_element_with_wait(locator)
        return target.is_displayed()
    
    def check_element_not_present(self, locator):
        return self.wait.until(EC.invisibility_of_element_located((locator)))
    
    def drag_and_drop_element(self, source_element, target_element):
        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);

                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);
             var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
            """
        self.driver.execute_script(script, source_element, target_element)
        