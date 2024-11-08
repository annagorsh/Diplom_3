import allure

from locators import OrderPopupLocators
from pages.base_page import BasePage


class OrderPopupPage(BasePage):

    @allure.step("Ожидаем видимости текста в попапе")
    def wait_until_popup_text_visible(self):
        self.wait_for_element_visible(OrderPopupLocators.POPUP_TEXT)