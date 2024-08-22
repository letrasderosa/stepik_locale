from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_options
import pytest

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="ru")

@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("--language")
    options = Chrome_options()
    if lang in ["en", "fr", "de", "es", "ru"]:
        options.add_argument("lang="+lang)
    else:
        raise ValueError("Invalid language")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
