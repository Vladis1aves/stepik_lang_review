from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.go_to_login_page()          # открываем страницу логина по кнопке
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()