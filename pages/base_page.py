from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from locators import *
import allure
from selenium.common import NoSuchElementException

class BasePage:
    @allure.step("Инициализируем браузер")
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step("Открываем нужный URL")
    def navigate (self, url):
        self.driver.get(url)

    @allure.step("Ищем нужный элемент")
    def find_element(self, locator, timeout=999):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Ищем нужные элементы")
    def find_elements(self, locator, timeout = 999):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step("Кликаем по нужному элементу")
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step("Заполняем поле нужным значением")
    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step("Ждём, пока элемент станет видимым")
    def wait_for_element_visible(self, locator, timeout = 999):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ждём, пока элемент станет кликабельным")
    def wait_for_element_clickable(self, locator, timeout = 999):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидаем изменения URL на нужный")
    def wait_for_url_change(self, expected_url, timeout=999):
            return WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))