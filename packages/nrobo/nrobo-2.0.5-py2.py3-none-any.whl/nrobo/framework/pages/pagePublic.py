from helpers.Page import Page
from selenium.webdriver.common.by import By


class PagePublic(Page):

    def __init__(self, driver, data={}, extra={}):
        super().__init__(driver)
        self.data = data
        self.extra = extra

        self.txt_username = (By.NAME, "user-name")
        self.txt_password = (By.NAME, "password")
        self.btn_login = (By.NAME, "login-button")

        # Validation messages
        self.msg_locked_out_user = (By.XPATH, '//h3["Epic sadface: Sorry, this user has been locked out."]')

    def type_username(self, username):
        self.log.info("Type username")
        self.type(*self.txt_username, username)

    def type_password(self, password):
        self.log.info("Type password")
        self.type(*self.txt_password, password)

    def click_button_login(self):
        self.log.info("Click on Login button")
        self.find_element_click(*self.btn_login)
