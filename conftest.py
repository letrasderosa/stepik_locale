from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options
from selenium.webdriver.firefox.options import Options as Firefox_options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import pytest


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru")
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="function")
def language(request):
    """Определяем возможность выбора языка"""
    lang =  request.config.getoption("--language")
    if lang in ["en", "fr", "de", "es", "ru"]:
        return lang
    else:
        raise ValueError("Invalid language")


@pytest.fixture(scope="function")
def browser(request, language):
    """Определяем возможность выбора браузера"""
    if request.config.getoption("--browser") == "chrome":
        options = Chrome_options()
        options.add_argument('lang=' + language)
        driver= webdriver.Chrome(options=options)

    elif request.config.getoption("--browser") == "firefox":
        profile = FirefoxProfile()
        profile.set_preference('intl.accept_languages', language)
        options = Firefox_options()

        options.profile = profile
        driver= webdriver.Firefox(options=options)

    else:
        raise ValueError("Invalid browser")

    yield driver
    driver.quit()


