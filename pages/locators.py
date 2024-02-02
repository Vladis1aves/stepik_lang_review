from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    register_form = (By.CSS_SELECTOR, '#register_form')
    login_form = (By.CSS_SELECTOR, '#login_form')

