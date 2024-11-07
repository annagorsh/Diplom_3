from pages.base_page import *
from locators import *

class LoginPage(BasePage):

    @allure.step("Инициализируем браузер")
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажимаем 'Восстановить пароль' на странице логина")
    def click_reset_password(self):
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON)

