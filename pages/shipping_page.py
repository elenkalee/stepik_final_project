from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC


class Shipping_page(Base):
    """Страница Shipping, переход на страницу Payment"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """LOCATORS"""
    terms_of_service_checkbox = '//div[@id="uniform-cgv"]'
    proceed_to_checkout_btn = '//*[@id="form"]/p/button'

    """GETTERS"""
    def get_terms_of_service_checkbox(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.terms_of_service_checkbox)))

    def get_proceed_to_checkout_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.proceed_to_checkout_btn)))

    """ACTIONS"""

    def check_terms_of_service_checkbox(self):
        self.get_terms_of_service_checkbox().click()
        print("Checked terms_of_service_checkbox")

    def click_proceed_to_checkout_btn(self):
        self.get_proceed_to_checkout_btn().click()
        print("Click proceed_to_checkout_btn on Shipping page")

    """METHODS"""

    def confirm_shipping_info(self):
        self.get_current_url()
        self.check_terms_of_service_checkbox()
        self.click_proceed_to_checkout_btn()
