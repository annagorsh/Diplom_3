from links import *
from pages.ingredient_popup_page import IngredientPopupPage
from pages.main_page import MainPage
from pages.order_feed_page import *


class TestMainFunctions:

    @allure.title("Проверяем переход на главную по клику на 'Конструктор'")
    def test_go_to_constructor_page(self, driver):
        order_feed = OrderFeedPage(driver)
        order_feed.navigate(ORDER_FEED_URL)
        order_feed.click_constructor_button()
        main = MainPage(driver)
        main.wait_until_url_main()
        expected_url = MAIN_URL
        assert driver.current_url == expected_url

    @allure.title("Проверяем переход на ленту заказов по клику на 'Лента заказов'")
    def test_go_to_order_feed_page(self, driver):
        main = MainPage(driver)
        main.navigate(MAIN_URL)
        main.click_order_feed_button()
        order_feed = OrderFeedPage(driver)
        order_feed.wait_for_order_feed_url()
        expected_url = ORDER_FEED_URL
        assert driver.current_url == expected_url

    @allure.title("Проверяем открытие и закрытие попапа с информацией об ингредиенте")
    def test_open_ingredient_info(self, driver):
        main = MainPage(driver)
        main.navigate(MAIN_URL)
        main.wait_for_bun()
        main.click_bun()
        popup = IngredientPopupPage(driver)
        popup.wait_until_popup_header_visible()
        assert "ingredient" in driver.current_url
        popup.close_popup()
        popup.wait_until_popup_invisible()