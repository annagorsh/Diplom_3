from selenium.webdriver.common.by import By

#Страница "Восстановить пароль"
class ForgotPasswordLocators:

    #поле "Email"
    EMAIL_FIELD = By.XPATH, "(//div[contains(.,'Email')])[5]"

    #Кнопка "Восстановить"
    RESET_PASSWORD_BUTTON = By.XPATH, "//button[contains(.,'Восстановить')]"

#Страница восстановления пароля с полем для ввода нового
class ResetPasswordLocators:

    #Поле "Пароль"
    NEW_PASSWORD_FIELD = By.XPATH, "//label[contains(.,'Пароль')]"

    #Иконка видимости пароля в виде глаза - открытый глаз, пароль закрыт точками
    VIEW_PASSWORD_BUTTON = By.CSS_SELECTOR, ".input__icon > svg: nth - child(1)"

    ###
    #!завязаться на type = text и type = password в поле ввода

#Страница логина
class LoginPageLocators:

    #Кнопка "Восстановить пароль"
    FORGOT_PASSWORD_BUTTON = By.XPATH, "//a[contains(.,'Восстановить пароль')]"



