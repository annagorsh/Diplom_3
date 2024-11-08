import allure

from links import MAIN_URL
from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Ожидаем видимости кнопки 'Оформить заказ'")
    def wait_order_button_visible(self):
        self.wait_for_element_visible(MainPageLocators.ORDER_BUTTON)

    @allure.step("Кликаем на кнопку 'Личный кабинет' в хедере сайта")
    def click_profile_button(self):
        self.click_element(MainPageLocators.GO_TO_PROFILE_BUTTON)

    @allure.step("Ожидаем смены URL на главную")
    def wait_until_url_main(self):
        self.wait_for_url_change(MAIN_URL)

    @allure.step("Кликаем на кнопку 'Лента заказов' в хедере сайта")
    def click_order_feed_button(self):
        self.click_element(MainPageLocators.GO_TO_ORDER_FEED_BUTTON)

    @allure.step("Кликаем на ингредиент(Флюоресцентная булка) на главной странице")
    def click_bun(self):
        self.click_element(MainPageLocators.FLUO_BUN)

    @allure.step("Ожидаем видимости карточки ингредиента с булкой")
    def wait_for_bun(self):
        self.wait_for_element_clickable(MainPageLocators.FLUO_BUN)