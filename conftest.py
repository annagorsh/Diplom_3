import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    browser = None
    if browser_name == "chrome":
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        ValueError("Can't create instance for this browser param")
    yield browser

    browser.quit()
