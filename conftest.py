import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es, fr, en")


@pytest.fixture()
def browser(request):
    # Создаем объект на основе класса options
    options_chrome = Options()
    options_firefox = OptionsFirefox()
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if language == "es":
        language = "es"
    elif language == "en":
        language = "en"
    elif language == "fr":
        language = "fr"
    else:
        raise pytest.UsageError("--language 'es' or 'fr' or 'en'")
    # Вызываем метод созданного объекта и передаем значение языка
    options_chrome.add_experimental_option('prefs', {'intl.accept_languages': language})
    options_firefox.set_preference("intl.accept_languages", language)
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

#
# @pytest.fixture(scope="function")
# def browser_chrome():
#     print("\nstart browser for test..")
#     browser = webdriver.Chrome()
#     browser.implicitly_wait(15)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# @pytest.fixture(scope="function")
# def browser_firefox():
#     print("\nstart browser for test..")
#     browser = webdriver.Firefox()
#     browser.implicitly_wait(15)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
