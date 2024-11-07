import allure

from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Ожидаем видимости кнопки 'Оформить заказ'")
    def wait_order_button_visible(self):
        self.wait_for_element_visible(MainPageLocators.ORDER_BUTTON)

    @allure.step("Кликаем на кнопку 'Личный кабинет' в хедере сайта")
    def click_profile_button(self):
        self.click_element(MainPageLocators.GO_TO_PROFILE_BUTTON)