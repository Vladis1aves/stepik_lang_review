from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url == self.url, f"Incorrect login url, factual {self.browser.current_url}, actual {self.url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form is not presented"

    def register_new_user(self, email, password):
        self.go_to_login_page()
        email_input = self.find(*LoginPageLocators.registration_email_input)
        email_input.send_keys(email)
        password1 = self.find(*LoginPageLocators.registration_password_input)
        password1.send_keys(password)
        password2 = self.find(*LoginPageLocators.confirm_password_input)
        password2.send_keys(password)
        button = self.find(*LoginPageLocators.register_button)
        button.click()


