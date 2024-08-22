from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options
import pytest

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru")

@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("--language")
    options = Chrome_options()
    if lang == "en":
        options.add_argument("lang=en")
    elif lang == "fr":
        options.add_argument("lang=fr")
    elif lang == "de":
        options.add_argument("lang=de")
    elif lang == "es":
        options.add_argument("lang=es")
    elif lang == "ru":
        options.add_argument("lang=ru")
    else:
        raise ValueError("Invalid language")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
