from typing import List

from tests.Pages.CommonPage import CommonPage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class YandexResultPage(CommonPage):
    def __init__(self, browser):
        super().__init__(browser)
        self.__result_list_path = '//ul[@id="search-result"]'
        self._search_result = None

    @property
    def search_result(self) -> List[WebElement]:
        if self._search_result is None:
            self._search_result = self.wait_visible((By.XPATH, self.__result_list_path)).find_elements(By.XPATH, './li')
        return self._search_result
