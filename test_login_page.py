from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.should_be_login_page()      # проверим что действительно страница логина