from tests.Pages.CommonPage import CommonPage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class YandexSearchPage(CommonPage):
    def __init__(self, browser):
        super().__init__(browser)
        self.page_path = 'https://yandex.ru'
        self.__input_search_path = '//input[@id="text"]'
        self.__find_button_path = '//div[@class="search2__button"]/button'
        self.__search_table_path = '//ul[@class="mini-suggest__popup-content"]'
        self.__pictures_path = '//div[text()="Картинки"]'
        self._input_search = None
        self._find_button = None
        self._search_table = None
        self._pictures = None

    @property
    def input_search(self) -> WebElement:
        if self._input_search is None:
            self._input_search = self.wait_visible((By.XPATH, self.__input_search_path))
        return self._input_search

    @property
    def find_button(self) -> WebElement:
        if self._find_button is None:
            self._find_button = self.wait_clickable((By.XPATH, self.__find_button_path))
        return self._find_button

    @property
    def search_table(self) -> WebElement:
        if self._search_table is None:
            self._search_table = self.wait_visible((By.XPATH, self.__search_table_path))
        return self._search_table

    @property
    def pictures(self) -> WebElement:
        if self._pictures is None:
            self._pictures = self.wait_clickable((By.XPATH, self.__pictures_path))
        return self._pictures
