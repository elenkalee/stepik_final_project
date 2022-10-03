from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import Logger


class Addresses_page(Base):
    """Cтраница Addreses, переход на страницу Shipping"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """LOCATORS"""
    proceed_to_checkout_btn = '//*[@id="center_column"]/form/p/button'

    """GETTERS"""

    def get_proceed_to_checkout_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.proceed_to_checkout_btn)))

    """ACTIONS"""

    def click_proceed_to_checkout_btn(self):
        self.get_proceed_to_checkout_btn().click()
        print("Click proceed_to_checkout_btn on Addresses page")

    """METHODS"""

    def confirm_address(self):
        # with allure.step("sign_in"):
        Logger.add_start_step(method="confirm_address")
        self.get_current_url()
        self.click_proceed_to_checkout_btn()
        Logger.add_end_step(url=self.driver.current_url, method="confirm_address")
