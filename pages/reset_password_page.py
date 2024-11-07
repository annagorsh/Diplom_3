import allure

from locators import ResetPasswordLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step("Инициализируем браузер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидаем видимости поля для ввода кода из имейла")
    def wait_until_email_code_field_is_visible(self):
        self.wait_for_element_visible(ResetPasswordLocators.EMAIL_CODE_FIELD)