import allure
import pytest

from tests.Pages.YandexImagesCategoryPage import YandexImagesCategoryPage
from tests.Pages.YandexImagesResultPage import YandexImagesResultPage
from tests.Pages.YandexResultPage import YandexResultPage
from tests.Pages.YandexSearchPage import YandexSearchPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.testconfig import browser


@allure.feature('yandex tests')
@allure.story('yandex search test')
def test_yandex_search(browser):
    yandex_search_page = YandexSearchPage(browser)
    with allure.step("go to yandex"):
        yandex_search_page.go()
    with allure.step("search field displayed"):
        assert yandex_search_page.input_search.is_displayed()
    with allure.step("enter search text tensor"):
        yandex_search_page.input_search.send_keys('Тензор')
    with allure.step("assert hit table displayed"):
        assert yandex_search_page.search_table.is_displayed()
    yandex_result_page = YandexResultPage(browser)
    with allure.step("check search result"):
        yandex_search_page.input_search.send_keys(Keys.ENTER)
        assert len(yandex_result_page.search_result) > 0
    with allure.step("check tensor link"):
        yandex_result_page.search_result[0].find_element(By.XPATH, '//*[text()="Тензор"]').click()
        browser.switch_to.window(browser.window_handles[1])
        assert browser.current_url == "https://tensor.ru/"


@allure.story('yandex pictures test')
def test_yandex_pictures(browser):
    yandex_search_page = YandexSearchPage(browser)
    with allure.step("go to yandex"):
        yandex_search_page.go()
    with allure.step("assert pictures displayed"):
        assert yandex_search_page.pictures.is_displayed()
    with allure.step("got to pages"):
        yandex_search_page.pictures.click()
        browser.switch_to.window(browser.window_handles[1])
    yandex_images_category_page = YandexImagesCategoryPage(browser)
    with allure.step("assert images open"):
        assert yandex_images_category_page.page_path in browser.current_url
    first_category_name = yandex_images_category_page.get_popular_category_name(0)
    with allure.step("open first image category"):
        yandex_images_category_page.popular_req_list[0].click()
    yandex_images_result_page = YandexImagesResultPage(browser)
    with allure.step("assert category name"):
        assert first_category_name == yandex_images_result_page.images_search_input.get_attribute("value")
    with allure.step("go first image"):
        yandex_images_result_page.images_list[0].click()
    with allure.step("assert image appear"):
        assert yandex_images_result_page.open_image.is_displayed()
    first_image_link = yandex_images_result_page.open_image.get_attribute("src")
    with allure.step("click next image"):
        yandex_images_result_page.next_image_button.click()
    yandex_images_result_page.update_open_image()
    second_image_link = yandex_images_result_page.open_image.get_attribute("src")
    with allure.step("assert image changed"):
        assert first_image_link != second_image_link
    with allure.step("click previous image"):
        yandex_images_result_page.prev_image_button.click()
    with allure.step("assert first image link not changed"):
        yandex_images_result_page.update_open_image()
        assert first_image_link == yandex_images_result_page.open_image.get_attribute("src")
