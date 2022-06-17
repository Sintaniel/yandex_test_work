from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CommonPage:

    def __init__(self, browser):
        self.browser: WebDriver = browser
        self._page_path = None
        self.wait = WebDriverWait(browser, 10)
        self.action_chains = ActionChains(browser)

    def wait_visible(self, search_data) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(search_data))

    def wait_clickable(self, search_data) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(search_data))

    def hover_on_element(self, search_data) -> WebElement:
        try:
            element = self.wait.until(EC.invisibility_of_element_located(search_data))
            self.action_chains.move_to_element(element).perform()
        finally:
            return self.wait_clickable(search_data)

    @property
    def page_path(self):
        return self._page_path

    @page_path.setter
    def page_path(self, page_path):
        self._page_path = page_path

    def go(self):
        if self._page_path is None:
            raise ValueError("no page path set")
        self.browser.get(self._page_path)
