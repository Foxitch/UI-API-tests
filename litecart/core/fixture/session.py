import allure


class SessionHelper:

    def __init__(self, app):
        self.app = app

    @allure.step('Login process')
    def login(self, email: str, password: str, proto: str, url: str) -> None:
        self.app.wd.get(f'{proto}://{url}/')
        self.app.homepage.get_email_input_field().send_keys(email)
        self.app.homepage.get_password_input_field().send_keys(password)
        self.app.homepage.get_login_btn()

    @allure.step('Logout process')
    def logout(self, proto: str, url: str) -> None:
        self.app.wd.get(f'{proto}://{url}/')
        self.app.homepage.get_logout_btn()
