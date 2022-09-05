from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC


class Sign_in_page(Base):
    """Страница авторизации, переход на страницу Addresses"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """LOCATORS"""
    sign_in_email_field = '//input[@id="email"]'
    password_field = '//input[@id="passwd"]'
    sign_in_button = '//button[@id="SubmitLogin"]'

    """GETTERS"""

    def get_sign_in_email_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_email_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_sign_in_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_button)))

    """ACTIONS"""

    def input_email(self, email):
        self.get_sign_in_email_field().send_keys(email)
        print("Input email")

    def input_password(self, password):
        self.get_password_field().send_keys(password)
        print("Input password")

    def click_sign_in_button(self):
        self.get_sign_in_button().click()
        print("Click_sign_in_button")

    """METHODS"""

    def sign_in(self):
        self.get_current_url()
        self.input_email("elena.42rus@yandex.ru")
        self.input_password("Test1234")
        self.click_sign_in_button()

