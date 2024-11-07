import faker

from helpers import get_random_email
from pages.base_page import *

class ForgotPasswordPage(BasePage):

    @allure.step("Инициализируем браузер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Ожидаем видимости надписи 'Вспомнили пароль?'")
    def wait_for_remember_password_visible(self):
        self.wait_for_element_visible(ForgotPasswordLocators.REMEMBER_PASSWORD_BUTTON)

    @allure.step("Кликаем на поле email")
    def click_email_field(self):
        self.click_element(ForgotPasswordLocators.EMAIL_FIELD)

    @allure.step("Заполняем поле email")
    def fill_in_email_field(self):
        self.enter_text(ForgotPasswordLocators.EMAIL_FIELD_ACTIVE, "bebeabobo@gmail.com")

    @allure.step("Кликаем на кнопку 'Восстановить'")
    def click_reset_button(self):
        self.click_element(ForgotPasswordLocators.RESET_PASSWORD_BUTTON)