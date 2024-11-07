import allure

from links import ORDER_HISTORY_URL
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):

    @allure.step("Ожидаем перехода на страницу с историей заказов")
    def wait_until_url_is_order_history(self):
        self.wait_for_url_change(ORDER_HISTORY_URL)