from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from selenium.webdriver.support import expected_conditions as EC


class Summary_page(Base):
    """Страница подтверждения товаров в корзине, переход на страницу авторизации"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """LOCATORS"""
    proceed_to_checkout_btn = '//*[@id="center_column"]/p[2]/a[1]'

    """GETTERS"""

    def get_proceed_to_checkout_btn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.proceed_to_checkout_btn)))

    """ACTIONS"""

    def click_proceed_to_checkout_btn(self):
        self.get_proceed_to_checkout_btn().click()
        print("Clicked proceed_to_checkout_btn on Summary page")

    """METHODS"""

    def confirm_shopping_cart_summary(self):
        self.get_current_url()
        self.click_proceed_to_checkout_btn()
