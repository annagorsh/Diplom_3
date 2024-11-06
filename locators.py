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

    #Поле "Пароль" - дефолтное состояние
    pass
    #Поле "Пароль" - активное состояние
    pass
    #скрытие пароля - можно завязаться на type = text и type = password в поле ввода
    #активность поля - можно завязаться на input_status_default и input_status_active

#Страница логина
class LoginPageLocators:

    #Кнопка "Восстановить пароль"
    FORGOT_PASSWORD_BUTTON = By.XPATH, "//a[contains(.,'Восстановить пароль')]"

#Главная страница
class MainPageLocators:

    #Кнопка "Личный кабинет"
    GO_TO_PROFILE_BUTTON = By.XPATH, "//p[contains(.,'Личный Кабинет')]"

    #Кнопка "Лента заказов"
    GO_TO_ORDER_FEED_BUTTON = By.XPATH, "//p[contains(.,'Лента Заказов')]"

#Личный кабинет
class ProfileLocators:

    #Кнопка в хедере для перехода в раздел "История заказов"
    ORDER_HISTORY_BUTTON = By.XPATH, "//a[contains(.,'История заказов')]"

    #Кнопка "Выход"
    LOGOUT_BUTTON = By.XPATH, "//button[@type='button'][contains(.,'Выход')]"

#Страница ленты заказов
class OrderFeedLocators:

    #Кнопка в хедере для перехода в раздел "Конструктор"
    GO_TO_CONSTRUCTOR_BUTTON = By.XPATH, "//p[contains(.,'Конструктор')]"





