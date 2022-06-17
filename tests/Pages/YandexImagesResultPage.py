from typing import List
from tests.Pages.CommonPage import CommonPage
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By


class YandexImagesResultPage(CommonPage):
    def __init__(self, browser):
        super().__init__(browser)
        self.__images_search_input_path = '//input[@class="input__control mini-suggest__input"]'
        self.__images_list_path = '//div[@role="list"]'
        self.__open_image_path = '//img[@class="MMImage-Preview"]'
        self.__next_image_button_path = '//div[contains(@class, "CircleButton") and contains(@class, "MediaViewer-ButtonNext")]'
        self.__prev_image_button_path = '//div[contains(@class, "CircleButton") and contains(@class, "MediaViewer-ButtonPrev")]'
        self._images_search_input = None
        self._images_list = None
        self._open_image = None
        self._next_image_button = None
        self._prev_image_button = None

    @property
    def images_search_input(self) -> WebElement:
        if self._images_search_input is None:
            self._images_search_input = self.wait_visible((By.XPATH, self.__images_search_input_path))
        return self._images_search_input

    @property
    def images_list(self) -> List[WebElement]:
        if self._images_list is None:
            self._images_list = self.wait_visible((By.XPATH, self.__images_list_path)).find_elements(By.XPATH, './div')
        return self._images_list

    @property
    def open_image(self) -> WebElement:
        if self._open_image is None:
            self._open_image = self.wait_visible((By.XPATH, self.__open_image_path))
        return self._open_image

    def update_open_image(self):
        self._open_image = self.wait_visible((By.XPATH, self.__open_image_path))

    @property
    def next_image_button(self):
        if self._next_image_button is None:
            self._next_image_button = self.hover_on_element((By.XPATH, self.__next_image_button_path))
        return self._next_image_button

    @property
    def prev_image_button(self):
        if self._prev_image_button is None:
            self._prev_image_button = self.hover_on_element((By.XPATH, self.__prev_image_button_path))
        return self._prev_image_button
