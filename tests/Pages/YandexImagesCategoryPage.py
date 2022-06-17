from typing import List

from tests.Pages.CommonPage import CommonPage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class YandexImagesCategoryPage(CommonPage):
    def __init__(self, browser):
        super().__init__(browser)
        self.page_path = 'https://yandex.ru/images/'
        self.__popular_req_list_path = '//div[@class="PopularRequestList"]'
        self._popular_req_list = None

    @property
    def popular_req_list(self) -> List[WebElement]:
        if self._popular_req_list is None:
            self._popular_req_list = self.wait_visible((By.XPATH, self.__popular_req_list_path)).find_elements(By.XPATH, './div')
        return self._popular_req_list

    def get_popular_category_name(self, index):
        return self.popular_req_list[index].find_element(By.XPATH, './/div[@class="PopularRequestList-SearchText"]').text
