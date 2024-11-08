import allure

from links import ORDER_FEED_URL
from locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Кликаем на кнопку Конструктор в шапке сайта")
    def click_constructor_button(self):
        self.click_element(OrderFeedLocators.GO_TO_CONSTRUCTOR_BUTTON)

    @allure.step("Ожидаем смены URL на страницу с лентой заказов")
    def wait_for_order_feed_url(self):
        self.wait_for_url_change(ORDER_FEED_URL)
